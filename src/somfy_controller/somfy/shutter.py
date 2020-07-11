#! /usr/bin/python3.7
from dataclasses import dataclass


@dataclass
class Shutter:
    shutter_id: str
    position: int
    time_to_complete: int
    rolling_code: int
