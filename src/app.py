import sys
import os

path_config = './config/MiniBot.conf'

try:
    import configparser
except:
    print("configparser: import error")
    exit()
else:
    print("configparser: imported")

if not os.path.exists(path_config):
    print("configparser: error path to config")
    exit()
else:
    config = configparser.ConfigParser()
    config.read(path_config)
    print("configparser: load config")

try:
    from libs.logger import logger
    lg = logger(log_mode=bool(config.get("LOGGING", "logging")), path_to_log=config.get("LOGGING", "path"), time_print=bool(config.get("LOGGING", "time")), debug_mode=bool(config.get("LOGGING", "debug")), format='%'+str(config.get("LOGGING", "timeformat")))
except:
    print("logger: import error or init error")
    exit()
else:
    lg.out("logger: ok", 'd')

if (bool(config.get("LOGGING", "autoclean"))):
    lg.clean_log()

try:
    import cv2 as cv
except:
    lg.out("opencv: import error", 'e')
    exit()
else: 
    lg.out("opencv: imported", 'd')

try:
    import imutils
except:
    lg.out("imutils: import error", 'e')
    exit()
else:
    lg.out("imutils: imported", 'd')

try:
    import scipy
except:
    lg.out("scipy: import error", 'e')
    exit()
else:
    lg.out("scipy: imported", 'd')

try:
    import PIL 
except:
    lg.out("pillow: import error", 'e')
    exit()
else:
    lg.out("pillow: imported", 'd')

try:
    import numpy as np
except:
    lg.out("numpy: import error", 'e')
    exit()
else:
    lg.out("numpy: imported", 'd')