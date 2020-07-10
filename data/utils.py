#! /usr/bin/python3.7

from typing import Optional
from pathlib import Path
import json

from data.paths import DATA_DIR, SHUTTER_DIR


def init_dirs():
    """ Initiates the data and shutters directory if they were'nt already created """

    if not DATA_DIR.exists():
        DATA_DIR.mkdir(mode=0o776)

    if not SHUTTER_DIR.exists():
        DATA_DIR.mkdir(mode=0o776)


def load_json_file(path: Optional[Path] = None) -> dict:
    """ Reads a json file and returns it as a dict """
    if path is not None and not path.is_file():
        raise Exception(f'Failed because "{path}" is not a file.')

    if path is None or not path.exists():
        raise FileNotFoundError(f'Failed to find json file at {path}')

    file_contents: str = path.read_text()

    try:
        return json.loads(file_contents)
    except json.JSONDecodeError as exc:
        raise Exception('Failed to parse file {path} to json, contents: "{file_contents}"') from exc
