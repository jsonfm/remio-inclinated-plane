"""Settings file."""
from decouple import AutoConfig
from utils.processing import processing
from server.routes import *

# ENV PATH
config = AutoConfig(search_path=".")
# ------------------------ SERVER SETTINGS ------------------------------------

serverSettings = {
    # "address": config("address", default="http://localhost:3000", cast=str),
    "address": "http://0.0.0.0:3000/",
    "request_timeout": 10,
}

# ------------------------- STREAM SETTINGS -----------------------------------

streamSettings = {
    "endpoint": EXPERIMENT_STREAMS_VIDEO_SERVER,
    "quality": 40,
    "fps": 12,
    "colorspace": "bgr",
    "colorsubsampling": "422",
    "fastdct": True,
    "enabled": True,
}

# ------------------------- CAMERA SETTINGS ------------------------------------

cameraSettings = {
    "webcam": {
        "src": 0,
        "fps": None,
        "size": [600, 400],
        "flipX": True,
        "flipY": False,
        "emitterIsEnabled": False,
        "backgroundIsEnabled": True,
        "processing": processing,
        "processingParams": {},
        "encoderIsEnable": False,
    },
}

# --------------------------- SERIAL SETTINGS ------------------------------

serialSettings = {
    "arduino": {
        "port": "/dev/cu.usbserial-1430",
        "baudrate": 9600,
        "timeout": 1.0,
        "reconnectDelay": 5,
        "portsRefreshTime": 5,
        "emitterIsEnabled": True,
        "emitAsDict": True,
    },
}