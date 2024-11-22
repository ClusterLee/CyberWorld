import os
import logging

# 设置日志记录器
logger = logging.getLogger('ComfyFog')

try:
    # 1. 设置Web目录
    WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")
    
    # 确保web目录存在
    if not os.path.exists(WEB_DIRECTORY):
        os.makedirs(WEB_DIRECTORY)
        
    # 确保js目录存在
    js_dir = os.path.join(WEB_DIRECTORY, "js")
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)

    # 2. 导入核心组件
    from .fog_server import ROUTES
    from .fog_manager import FogManager  # 新的管理类

    # 3. 初始化fog管理器
    fog_manager = FogManager()

    # 4. 导出必要的变量
    __all__ = ['WEB_DIRECTORY', 'ROUTES', 'fog_manager']

except Exception as e:
    logger.error(f"Error initializing ComfyFog: {e}")
    WEB_DIRECTORY = ""
    ROUTES = []
