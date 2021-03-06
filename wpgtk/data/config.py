import configparser
import shutil
import os
import logging

__version__ = '5.8.0'

parser = None

HOME = os.path.expanduser("~")
WPG_DIR = os.path.join(HOME, ".config/wpg")
CONF_FILE = os.path.join(WPG_DIR, "wpg.conf")
MODULE_DIR = os.path.abspath(os.path.join(__file__, "../../"))
CONF_BACKUP = os.path.join(MODULE_DIR, "misc/wpg.conf")
WALL_DIR = os.path.join(WPG_DIR, "wallpapers")
SAMPLE_DIR = os.path.join(WPG_DIR, "samples")
SCHEME_DIR = os.path.join(WPG_DIR, "schemes")
FORMAT_DIR = os.path.join(WPG_DIR, "formats")
OPT_DIR = os.path.join(WPG_DIR, "templates")
FILE_DIC = {
    'icon-step1': os.path.join(HOME, ".icons/flattrcolor/scripts"
                               "/replace_folder_file.sh"),
    'icon-step2': os.path.join(HOME, ".icons/flattrcolor/scripts"
                               "/replace_script.sh")
}


def write_conf(config_path=CONF_FILE):
    global parser

    with open(config_path, 'w') as config_file:
        parser.write(config_file)


def load_sections():
    """reads the sections of the config file"""
    global parser

    parser = configparser.ConfigParser()
    parser.optionxform = str
    parser.read(CONF_FILE)

    return [parser['settings'], parser['keywords']]


def load_settings():
    os.makedirs(WALL_DIR, exist_ok=True)
    os.makedirs(SAMPLE_DIR, exist_ok=True)
    os.makedirs(SCHEME_DIR, exist_ok=True)
    os.makedirs(FORMAT_DIR, exist_ok=True)
    os.makedirs(OPT_DIR, exist_ok=True)

    try:
        return load_sections()
    except Exception:
        logging.error("not a valid config file")
        logging.info("copying default config file")

        shutil.copy(CONF_BACKUP, CONF_FILE)
        return load_sections()


settings, user_keywords = load_settings()
