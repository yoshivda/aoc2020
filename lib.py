from pathlib import Path
import requests

YEAR = 2020
ROOT_PATH = Path(__file__).parents[0]


def load_input(day, part=""):
    path = Path(ROOT_PATH, get_filename(day, part))
    if not path.exists():
        if not part:
            download_input(day)
        else:
            raise FileNotFoundError(f"File {path} does not exist")
    return path.read_text()


def download_input(day):
    Path(ROOT_PATH, "inputs").mkdir(exist_ok=True)
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    req = requests.get(url, cookies={"session": Path(ROOT_PATH, f"credentials.secret").read_text().strip()})
    Path(ROOT_PATH, get_filename(day)).write_bytes(req.content)


def get_filename(day, part):
    if part:
        return f"inputs/day{str(day).zfill(2)}_{part}.txt"
    return f"inputs/day{str(day).zfill(2)}.txt"


if __name__ == '__main__':
    download_input(1)
