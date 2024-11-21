import logging

logger = logging.getLogger('ComfyFog')

def fog_status(req):
    """
    获取节点当前状态
    
    请求方式：GET /fog/status
    
    响应格式：
    {
        "status": {
            "enabled": bool,            # 节点是否启用
            "current_task": {
                "id": str,              # 当前任务ID，如果没有则为null
                "status": str           # "processing" 或 "idle"
            },
            "schedule": [               # 调度时间段列表
                {
                    "start": "HH:MM",   # 开始时间
                    "end": "HH:MM"      # 结束时间
                }
            ],
            "last_error": str          # 最近的错误信息，如果没有则为null
        }
    }
    """
    try:
        node = req.node
        status = node.get_status()
        logger.debug(f"Status requested: {status}")
        return {"status": status}
    except Exception as e:
        logger.error(f"Error getting status: {e}")
        return {"error": str(e)}

def fog_update_config(req):
    """
    更新节点配置
    
    请求方式：POST /fog/config
    
    请求格式：
    {
        "enabled": bool,               # 是否启用节点
        "schedule": [                  # 调度时间段列表
            {
                "start": "HH:MM",      # 开始时间
                "end": "HH:MM"         # 结束时间
            }
        ],
        "task_center_url": str        # 任务中心URL
    }
    
    响应格式：
    {
        "status": "success",           # 操作状态
        "config": {                    # 更新后的完整配置
            "enabled": bool,
            "schedule": [...],
            "task_center_url": str
        }
    }
    """
    try:
        node = req.node
        config_data = req.json
        result = node.update_config(config_data)
        logger.info("Config updated via API")
        return result
    except Exception as e:
        logger.error(f"Error updating config: {e}")
        return {"error": str(e)}

def fog_history(req):
    """
    获取任务执行历史
    
    请求方式：GET /fog/history?limit=10
    
    查询参数：
    - limit: int, 可选，默认10，返回的历史记录数量
    
    响应格式：
    {
        "history": [
            {
                "task_id": str,         # 任务ID
                "status": str,          # "completed" 或 "failed"
                "timestamp": str,       # ISO格式的时间戳
                "error": str           # 如果失败，则包含错误信息
            }
        ]
    }
    """
    try:
        node = req.node
        limit = int(req.query.get("limit", 10))
        history = node.get_history(limit)
        logger.debug(f"History requested, limit: {limit}")
        return {"history": history}
    except Exception as e:
        logger.error(f"Error getting history: {e}")
        return {"error": str(e)}

def fog_clear_history(req):
    """
    清除历史记录
    
    请求方式：POST /fog/history/clear
    
    响应格式：
    {
        "status": "success"            # 操作状态
    }
    
    错误响应：
    {
        "error": str                   # 错误信息
    }
    """
    try:
        node = req.node
        node.clear_history()
        logger.info("History cleared via API")
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error clearing history: {e}")
        return {"error": str(e)}

# ComfyUI路由定义
ROUTES = [
    ("fog/status", fog_status),                    # GET 获取状态
    ("fog/config", fog_update_config, ["POST"]),   # POST 更新配置
    ("fog/history", fog_history),                  # GET 获取历史
    ("fog/history/clear", fog_clear_history, ["POST"])  # POST 清除历史
]

# 导出必要的变量
__all__ = ['ROUTES']