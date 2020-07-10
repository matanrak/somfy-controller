#! /usr/bin/python3.7

from pathlib import Path

DATA_DIR: Path = Path('/etc/somfy-controller')

SHUTTER_DIR: Path = DATA_DIR / 'shutters'
CONFIG_PATH: Path = DATA_DIR / 'config.json'
