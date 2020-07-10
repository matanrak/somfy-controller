#! /usr/bin/python3.7

from typing import Optional
from pathlib import Path
import json

from src.data import CONFIG_PATH
from src.data import load_json_file, init_dirs

KEY_INITIAL_SHUTTER_POSITION = 'initial_shutter_position'
KEY_TXGPIO = 'TXPGPIO'

DEFAULT_CONFIG = {
    KEY_TXGPIO: 4,
    KEY_INITIAL_SHUTTER_POSITION: 100,
}


def create_initial_config(override_current: bool = True):
    """ Creates the initial config file if the current one does not exist """
    init_dirs()

    if not CONFIG_PATH.exists() or override_current:
        CONFIG_PATH.touch(mode=0o666)
        CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG))


def get_config() -> dict:
    if not CONFIG_PATH.exists():
        create_initial_config()

    try:
        return load_json_file(CONFIG_PATH)
    except FileNotFoundError as exc:
        raise Exception(f'Failed to find / create default config file at {CONFIG_PATH}') from exc


def update_config(updated_config: dict, path: Optional[Path] = None):
    """ Insert a key and a value to a json file """

    if path is None:
        path = CONFIG_PATH

    if not path.is_file():
        raise Exception(f'Failed because "{path}" is not a file.')

    try:
        path.write_text(json.dumps(updated_config))
    except OSError as exc:
        raise Exception(f'Failed to insert {json.dumps(updated_config)} into json file located at: "{path}"') from exc
