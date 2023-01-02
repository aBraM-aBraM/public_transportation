import json
import subprocess
from pathlib import Path

from structs import Station, Position, Line, Node, Blueprint

GSDB_PATH = Path("GSDB")
DATA_PATH = GSDB_PATH / "data"


def main():
    first_station = Station("Odivelas", Position(38.79326, -9.1730002))
    second_station = Station("Senhor Roubado", Position(38.7856422, -9.1718447))
    line = Line(name="Amarela",
                color="#F4BC18",
                shiftCoords=[0, 0],
                nodes=[Node([20, 20], 'W', first_station.name), Node([30, 30], 'W', second_station.name)])

    blueprint = Blueprint([first_station, second_station], [line])

    with open(DATA_PATH / "new_map.json", "w") as new_map_fd:
        json.dump(blueprint.to_dict(), new_map_fd)

    watch = subprocess.Popen("npm run watch", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GSDB_PATH)
    subprocess.Popen("npm run webpack", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GSDB_PATH)

    watch.wait()



if __name__ == '__main__':
    main()
