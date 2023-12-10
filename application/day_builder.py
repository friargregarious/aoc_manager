"""usage:

import day_builder
daybuilder.main(year, day) -> json

{
    "instructions.md": contents,
    "solve2023_10_a.py": contents,
    "solve2023_10_b.py": contents,
    "input.txt": contents,
    "local_utils.py": contents,
    "setup.py": contents,
    "readme.md": contents
}

"""
import os
import sys
from configparser import ConfigParser
from datetime import datetime
import aocd
import urllib3
import platform
import my_utilities

arg_keys = sys.argv[1:]
arg_dict = {x.lower(): y for x, y in zip(arg_keys[0::2], sys.argv[1::2])}

if "-y" in arg_dict:
    year = int(arg_dict["-y"])
else:
    year = datetime.now().year

if "-d" in arg_dict:
    day = int(arg_dict["-d"])
else:
    day = datetime.now().day


def pad(day: int) -> str:
    return str(day).rjust(2, "0")


# if "-e" in arg_dict:
#     EXAMPLE = True
#     correct_example_a, correct_example_b = arg_dict["-e"].split(",")
# else:
#     EXAMPLE = False
#     correct_example_a, correct_example_b = None, None

username = "FriarGreg"
useremail = "greg.denyes@gmail.com"
userhome = "https://github.com/friargregarious"
usersource = urllib3.util.parse_url(
    f"{userhome}/Advent-of-Code/tree/main/AOC {year}/Day {pad(day)}"
)
pyversion = platform.python_version()
input_url = f"https://adventofcode.com/{year}/day/{day}/input"
token = urllib3.request(method="GET", url=input_url).json()["cookies"]["session"]


user = aocd.models.User(token=token)
puzzle = aocd.models.Puzzle(year, day, user)

game_root = "C:/Advent of Code"
new_day_path = f"{game_root}/AOC {year}/Day {pad(day)}"


replacements = {
    "{title}": puzzle.title.title(),
    "{year}": str(year),
    "{day}": str(day),
    "{username}": "",
    "{useremail}": "",
    "{userhome}": "",
    "{usersource}": "",
    "{pyversion}": "",
}

bannerline = f"#{'-'*80}"[:80]


def banner(title):
    new_banner = [
        bannerline,
        f"# {title.upper().strip()} {bannerline}"[:80],
        bannerline,
    ]
    return "\n" + "\n".join(new_banner) + "\n"


# default_imports =


header_lines = [
    bannerline,
    "ADVENT OF CODE | {year} | {title}",
    "https://adventofcode.com/{year}/day/{day}",
    ["SOLVER:", "{username} ({useremail})"],
    ["HOME:", "{userhome}"],
    ["SOURCE:", "{usersource}"],
    ["WRITTEN AND TESTED IN", "PYTHON VER {pyversion}"],
]


imports = [
    bannerline,
    banner("imports"),
    bannerline,
    "import os",
    "from configparser import ConfigParser",
    "import math",
    "from datetime import datetime",
    "from termcolor import colored",
    "import aocd",
    "\n\n",
]

gather_tools = [
    bannerline,
    banner("gather tools"),
    bannerline,
    "\n\n",
]

part_a = [
    bannerline,
    banner("part a"),
    bannerline,
    "\n\n",
]

part_b = [
    bannerline,
    banner("part b"),
    bannerline,
    "\n\n",
]


main_entry = [
    bannerline,
    banner("main entry point for submitting and benchmarking"),
    bannerline,
    "\n\n",
]


running_from_home = [
    bannerline,
    banner("running from home"),
    bannerline,
    "\n\n",
]
