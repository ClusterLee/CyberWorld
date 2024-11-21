import os
import logging

# 设置日志记录器
logger = logging.getLogger('ComfyFog')

try:
    # 1. 设置Web目录 - ComfyUI会自动加载这个目录下的js文件
    WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")
    
    # 确保web目录存在
    if not os.path.exists(WEB_DIRECTORY):
        os.makedirs(WEB_DIRECTORY)
        logger.info(f"Created web directory: {WEB_DIRECTORY}")
        
    # 确保js目录存在
    js_dir = os.path.join(WEB_DIRECTORY, "js")
    if not os.path.exists(js_dir):
        os.makedirs(js_dir)
        logger.info(f"Created js directory: {js_dir}")

    # 2. 导入核心组件
    from .fog_nodes import FogControlNode
    from .fog_server import ROUTES

    # 3. 注册节点
    NODE_CLASS_MAPPINGS = {
        "FogControl": FogControlNode
    }

    NODE_DISPLAY_NAME_MAPPINGS = {
        "FogControl": "Fog Control"
    }

    # 4. 导出必要的变量
    __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY', 'ROUTES']

except Exception as e:
    logger.error(f"Error initializing ComfyFog: {e}")
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    WEB_DIRECTORY = ""
    ROUTES = []
