import os
import sys
from envparse import env
from HexzyBot import LOGGER

DEFAULTS = {
    "LOAD_MODULES": True,
}

CONFIG_PATH = "data/bot_conf.yaml"
if os.name == "nt":
    log.debug("Detected Windows, changing config path...")
    CONFIG_PATH = os.getcwd() + "\\data\\bot_conf.yaml"

if os.path.isfile(CONFIG_PATH):
    log.info(CONFIG_PATH)
    for item in (
        data := yaml.load(open("data/bot_conf.yaml", "r"), Loader=yaml.CLoader)
    ):
        DEFAULTS[item.upper()] = data[item]
else:
    log.info("Using env vars")
def get_str_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.str(name, default=default)) and not required:
        LOGGER.warn("No str key: " + name)
        return None
    elif not data:
        LOGGER.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data

def get_int_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.int(name, default=default)) and not required:
        LOGGER.warn("No int key: " + name)
        return None
    elif not data:
        LOGGER.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data
