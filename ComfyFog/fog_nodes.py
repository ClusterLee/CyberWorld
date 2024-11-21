import threading
import json
import time
import os
import logging
from .fog_client import FogClient
from .fog_scheduler import FogScheduler
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='comfyfog.log'
)
logger = logging.getLogger('ComfyFog')

class FogControlNode:
    """ComfyUI的Fog控制节点，负责管理远程任务的获取和执行"""
    
    # 1. ComfyUI节点接口定义
    @classmethod
    def INPUT_TYPES(cls):
        """定义ComfyUI节点的输入类型"""
        return {
            "required": {},  # 无需输入参数
            "optional": {
                "enabled": ("BOOLEAN", {"default": False}),  # 可选的启用开关
                "task_center_url": ("STRING", {"default": ""})  # 可选的任务中心URL
            }
        }
    
    RETURN_TYPES = ()  # 无返回值
    FUNCTION = "process"  # 处理函数名称
    CATEGORY = "ComfyFog"  # 节点分类
    OUTPUT_NODE = False  # 不是输出节点
    
    def __init__(self):
        """初始化Fog控制节点"""
        try:
            # 1. 初始化基础路径
            self.base_path = self._init_base_path()
            
            # 2. 初始化配置
            self.config = self._load_and_validate_config()
            
            # 3. 初始化组件
            self.client = self._init_client()
            self.scheduler = self._init_scheduler()
            
            # 4. 初始化线程安全锁
            self.lock = threading.Lock()
            
            # 5. 启动监控线程
            self.running = True
            self._start_monitor_thread()
            
            logger.info("FogControlNode initialized successfully")
            
        except Exception as e:
            logger.error(f"FogControlNode initialization failed: {e}")
            self.running = False
            raise
    
    def _init_base_path(self):
        """初始化并验证基础路径"""
        base_path = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(base_path):
            try:
                os.makedirs(base_path)
                logger.info(f"Created base directory: {base_path}")
            except Exception as e:
                raise RuntimeError(f"Failed to create base directory: {e}")
        return base_path
    
    def _load_and_validate_config(self):
        """加载并验证配置"""
        config = self._load_config()
        return self._validate_config(config)
    
    def _init_client(self) -> FogClient:
        """
        初始化FogClient
        
        Returns:
            FogClient: 初始化好的FogClient实例
            
        Raises:
            ValueError: 配置缺失或无效
            RuntimeError: 初始化失败
        """
        try:
            task_center_url = self.config.get('task_center_url')
            if not task_center_url:
                raise ValueError("task_center_url is required in config")
            
            client = FogClient(task_center_url)
            
            # 测试连接
            if not client.test_connection():
                raise RuntimeError("Failed to connect to task center")
            
            return client
            
        except Exception as e:
            logger.error(f"Failed to initialize FogClient: {e}")
            raise
    
    def _init_scheduler(self):
        """初始化FogScheduler"""
        if not hasattr(self, 'client'):
            raise RuntimeError("FogClient must be initialized before FogScheduler")
        return FogScheduler(self.client)
    
    def _start_monitor_thread(self):
        """启动监控线程"""
        self.monitor_thread = threading.Thread(
            target=self._monitor_queue,
            name="FogMonitor",
            daemon=True
        )
        self.monitor_thread.start()
        logger.info("Monitor thread started")
    
    def __del__(self):
        """清理资源"""
        try:
            self.running = False
            if hasattr(self, 'monitor_thread'):
                self.monitor_thread.join(timeout=1)
            if hasattr(self, 'client'):
                self.client.session.close()
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
    
    def _monitor_queue(self):
        """持续监控队列的主循环，定期检查是否有新任务需要处理"""
        while self.running:
            try:
                with self.lock:  # 使用锁保护配置访问
                    if self.config.get("enabled", False):
                        self.scheduler.process_task()
            except Exception as e:
                logger.error(f"Error in monitor queue: {e}")
            time.sleep(5)  # 避免过于频繁的检查
    
    def _load_config(self):
        """加载配置文件"""
        try:
            config_path = os.path.join(self.base_path, 'config.json')
            with open(config_path, 'r') as f:
                return json.load(f)
        except:
            # 返回默认配置
            return {"enabled": False, "schedule": [], "task_center_url": ""}
    
    def process(self):
        """ComfyUI调用的处理函数"""
        return ()
    
    def _validate_config(self, config):
        """验证配置文件格式，确保所有必要的配置项都存在且格式正确"""
        required_fields = ['enabled', 'task_center_url', 'schedule']
        for field in required_fields:
            if field not in config:
                config[field] = self._get_default_value(field)
        
        # 验证schedule格式
        if not isinstance(config['schedule'], list):
            config['schedule'] = []
        
        # 验证每个时间段的格式
        for schedule in config['schedule']:
            if not isinstance(schedule, dict) or 'start' not in schedule or 'end' not in schedule:
                config['schedule'] = self._get_default_value('schedule')
                break
                
        return config
    
    def _get_default_value(self, field):
        """获取配置项的默认值"""
        defaults = {
            'enabled': False,
            'task_center_url': '',
            'schedule': [],
            'max_tasks_per_day': 100,
            'min_gpu_memory_available': 4000,
            'retry_interval': 5,
            'max_retries': 3
        }
        return defaults.get(field)
    
    def update_config(self, new_config):
        """更新配置，线程安全的配置更新"""
        with self.lock:
            self.config.update(new_config)
            self._save_config()
            logger.info("Configuration updated")
    
    def get_status(self):
        """获取节点当前状态，包括：启用状态、当前任务、队列状态、最近历史"""
        with self.lock:
            return {
                "enabled": self.config.get("enabled", False),
                "schedule": self.config.get("schedule", []),
                "current_task": {
                    "id": self.scheduler.current_task.get("id") if self.scheduler.current_task else None,
                    "status": "processing" if self.scheduler.current_task else "idle"
                },
                "queue_status": self.scheduler.queue_status,
                "history": self.scheduler.task_history[-10:],  # 最近10条历史
                "last_error": self.last_error if hasattr(self, 'last_error') else None
            }
    
    def _update_status(self, error=None):
        """更新节点状态，如果有错误发生，记录错误信息"""
        try:
            if error:
                self.last_error = {
                    "message": str(error),
                    "timestamp": datetime.now().isoformat()
                }
            self._save_status()
        except Exception as e:
            logger.error(f"Error updating status: {e}")
    
    def get_history(self, limit=10):
        """获取任务执行历史，Args: limit (int): 返回的记录数量，Returns: list: 历史记录列表"""
        with self.lock:
            history = self.scheduler.task_history[-limit:] if self.scheduler.task_history else []
            return [
                {
                    "task_id": item.get("task_id"),
                    "status": item.get("status"),
                    "timestamp": item.get("timestamp"),
                    "error": item.get("error") if item.get("status") == "failed" else None
                }
                for item in history
            ]
    
    def clear_history(self):
        """清除任务历史，Returns: dict: 操作结果"""
        with self.lock:
            try:
                self.scheduler.task_history = []
                self.scheduler._save_history()  # 保存到文件
                return {"status": "success"}
            except Exception as e:
                logger.error(f"Error clearing history: {e}")
                raise
    
    def _save_config(self):
        """保存配置到文件"""
        try:
            config_path = os.path.join(self.base_path, 'config.json')
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving config: {e}")
            raise
