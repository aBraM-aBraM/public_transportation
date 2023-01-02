from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Position:
    lat: float
    lon: float


@dataclass
class Station:
    def __init__(self, name: str, position: Position):
        self.name = name
        self.label = name
        self.position = position
        self.id = id(self)

    id: int
    name: str
    label: str
    position: Position

    def to_dict(self):
        this_dict = self.__dict__
        this_dict['position'] = self.position.__dict__
        return this_dict


@dataclass
class Node:
    coords: List[int, int]
    labelPos: str  # N, E, S, W
    name: str


@dataclass
class Line:
    name: str
    color: str
    shiftCoords: List[int, int]
    nodes: List[Node]

    def to_dict(self):
        this_dict = self.__dict__
        this_dict['nodes'] = [node.__dict__ for node in self.nodes]
        return this_dict


@dataclass
class Blueprint:
    stations: List[Station]
    lines: List[Line]

    def to_dict(self):
        this_dict = self.__dict__
        this_dict['stations'] = {station.name: station.to_dict() for station in self.stations}
        this_dict['lines'] = [line.to_dict() for line in self.lines]
        return this_dict
