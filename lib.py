from pathlib import Path
import requests

YEAR = 2020
ROOT_PATH = Path(__file__).parents[0]


def load_input(day):
    path = Path(ROOT_PATH, get_filename(day))
    if not path.exists():
        download_input(day)
    return path.read_text()


def download_input(day):
    Path(ROOT_PATH, "inputs").mkdir(exist_ok=True)
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    req = requests.get(url, cookies={"session": Path(ROOT_PATH, f"credentials.secret").read_text().strip()})
    Path(ROOT_PATH, get_filename(day)).write_bytes(req.content)


def get_filename(day):
    return f"inputs/day{str(day).zfill(2)}.txt"


if __name__ == '__main__':
    download_input(1)
