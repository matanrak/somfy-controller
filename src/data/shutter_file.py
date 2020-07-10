#! /usr/bin/python3.7

from pathlib import Path
from typing import Any
from dataclasses import asdict
import json

from src.data import SHUTTER_DIR
from src.data import init_dirs, load_json_file
from src.somfy import Shutter


def get_shutter_file_path(shutter_id: str) -> Path:
    return SHUTTER_DIR / f'{shutter_id}.json'


def load_shutter(shutter_id: str) -> Shutter:
    """ Loads a shutter from a shutter file """
    if not SHUTTER_DIR.exists():
        init_dirs()

    shutter_file_path: Path = get_shutter_file_path(shutter_id)

    if not shutter_file_path.exists():
        raise Exception(f'Shutter "{shutter_id}" does not exist.')

    return Shutter(**load_json_file())


def create_shutter(shutter_id: str, position: int, time_to_complete: int, rolling_code: int):
    """ Creates a new shutter object and file """
    shutter_file_path: Path = get_shutter_file_path(shutter_id)

    if shutter_file_path.exists():
        raise Exception(f'The shutter {shutter_id} already exists.')

    shutter = Shutter(
        shutter_id=shutter_id,
        position=position,
        time_to_complete=time_to_complete,
        rolling_code=rolling_code
    )

    shutter_file_path.touch(mode=0o666)
    shutter_file_path.write_text(json.dumps(asdict(shutter)))


def update_shutter_value(key: str, value: Any, shutter: Shutter):
    """ Updates a shutter value in the config """
    shutter_data: dict = asdict(shutter)
    shutter_data[key] = value

    shutter_file_path: Path = get_shutter_file_path(shutter.shutter_id)
    shutter_file_path.write_text(json.dumps(shutter_data))
