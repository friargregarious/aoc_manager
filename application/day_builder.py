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
import build_utils
from datetime import datetime

import platform
from urllib.parse import quote
import requests
import browser_cookie3

###############################################################################
os.system("cls")


env_cfg = build_utils.get_cfg("env")  # cParser()
user_cfg = build_utils.get_cfg("users")  # cParser()

env_cfg["paths"]["games_path"] = "C:/Advent of Code"
env_cfg["paths"]["app_path"] = os.getcwd().replace("\\", "/")
env_cfg.save_me("env")

# print("APP ROOT:", app_root)
# print("user_cfg hard path:  ", "C:/GitHub/aoc_manager/application/configs/users.ini")
# print("user_cfg found path: ", user_cfg_file)
user_cfg.read("users")


###############################################################################

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
###############################################################################
print(f"|<{' ' * (80-4)}>|")


def pad(day: int) -> str:
    return str(day).rjust(2, "0")


def parse_info(user, puzzle):
    """ """
    homename, username, userid = user.id.split(".")
    userhome = f"github.com/{username}"
    usersource_url = f"~/Advent-of-Code/AOC {puzzle.year}/Day {pad(puzzle.day)}"

    return {
        ":userhome:": userhome,
        ":username:": username,
        ":usersource:": usersource_url,
    }


def get_token():
    """pulls token information from cookiejar...
    unfortuantely only works if Chrome is NOT running."""
    cj = browser_cookie3.chrome(domain_name="adventofcode.com")
    my_cookies = requests.utils.dict_from_cookiejar(cj)
    return my_cookies["session"]


###############################################################################


try:
    token = get_token()

except PermissionError:
    u_home, u_id, token = user_cfg.getlist("current_users", "friargregarious")
    u_id = int(u_id)

aoc_user, aoc_puzzle = build_utils.get_puzzle_data(year, day, token)

homename, username, userid = aoc_user.id.split(".")

# user_cfg.putlist("current_users", username, [homename, userid, token])
# user_cfg.save_me("users")


input_url = f"https://adventofcode.com/{year}/day/{day}/input"
bannerline = "#" * 79
useremail = "greg.denyes@gmail.com"
game_root = "C:/Advent of Code"


replacements = {
    ":title:": aoc_puzzle.title.title(),
    ":year:": str(year),
    ":day:": str(day),
    ":useremail:": useremail,
    ":pyversion:": platform.python_version(),
}

replacements.update(parse_info(aoc_user, aoc_puzzle))


def banner(title):
    new_banner = [
        bannerline,
        f"# {title.upper().strip()} {bannerline}"[:79],
        bannerline,
    ]
    return "\n" + "\n".join(new_banner) + "\n"


# default_imports =


header_lines = [
    bannerline,
    "ADVENT OF CODE | :year: | :title:",
    "adventofcode.com/:year:/day/:day:",
    ["SOLVER:", ":username:"],
    ["CONTACT:", ":useremail:"],
    ["HOME:", ":userhome:"],
    ["SOURCE:", ":usersource:"],
    ["WRITTEN AND TESTED IN:", "PYTHON VER :pyversion:"],
]

outputs = []

for line in header_lines:
    if line == bannerline:
        new_line = line

    elif isinstance(line, str):
        new_line = line
        for lookfor, replacewith in replacements.items():
            if lookfor in line:
                new_line = new_line.replace(lookfor, replacewith)
        new_line = f"#{new_line.center(77)}#"

    else:  # left/right lists
        left, right = line

        for lookfor, replacewith in replacements.items():
            if lookfor in right:
                right = right.replace(lookfor, str(replacewith))

        center_on = f"{left} ".ljust(24, "-") + f" {right}".rjust(50, "-")
        new_line = f"#{center_on.center(77)}#"

    outputs.append(new_line)


imports = [
    banner("imports"),
    "import os",
    "from my_utils import MyConfigParser as MyCfg",
    "import math",
    "from datetime import datetime",
    "from termcolor import colored",
    "import aocd",
    "\n\n",
]


for line in imports:
    # if line == bannerline:
    outputs.append(line)


declarations = [
    "__version__ = 0.0.0\n",
    "__example_answer__ = \n",
]

for line in declarations:
    # if line == bannerline:
    outputs.append(line)


gather_tools = [
    banner("gather tools"),
    "def parse_input(source:str='input.txt') -> list:\n",
    "\t# For parsing source string into usable content\n",
    "\tpass",
    "\n\n\n\n",
]


for line in gather_tools:
    # if line == bannerline:
    outputs.append(line)


parts = [
    banner("solve part :part:"),
    "def solve_:part:(data):\n",
    f"\t# For solving PART :part: of day {day}'s puzzle.\n",
    "\tpass",
    "\n\n",
]


main_entry = [
    banner("main entry point for submitting and benchmarking"),
    "\n\n",
    "def main(source):\n",
    "\t# Main entry point\n",
    "\tsolution = Solve_:part:(source)\n",
    "\n",
]


running_from_home = [
    banner("running from home"),
    "if __name__ == '__main__':\n",
    "\tmy_utils.version_increment(':part:', sml=1)\n",
    "\tif __run_on_example__ :\n",
    "\t\tanswer = main(parse('example.txt'), __example_answer__)\n",
    "\telse:\n",
    "\t\tanswer = main(parse('input.txt'))\n",
    "\tmy_utils.version_increment('a', sml=1)",
    "\tmy_utils.solve_me(answer, ':part:')",
    "\n\n",
]


# here is where the two "Solve" files become a little different
outputs_b = outputs.copy()

for line in parts:
    outputs.append(line.replace(":part:", "a"))
    outputs_b.append(line.replace(":part:", "b"))

for line in main_entry:
    outputs.append(line.replace(":part:", "a"))
    outputs_b.append(line.replace(":part:", "b"))

for line in running_from_home:
    outputs.append(line.replace(":part:", "a"))
    outputs_b.append(line.replace(":part:", "b"))


new_day_path = f"{game_root}/AOC {year}/Day {pad(day)}"

if not os.path.isdir(new_day_path):
    os.mkdirs(new_day_path, exist_ok=True)

a_txt = "\n".join(outputs)
b_txt = "\n".join(outputs_b)

a_file_name = f"{new_day_path}/Solve{year}_{pad(day)}_a.py"
if not os.path.isfile(a_file_name):
    open(a_file_name, "w", encoding="utf-8").write(a_txt)
else:
    raise FileExistsError(filename=a_file_name)


b_file_name = f"{new_day_path}/Solve{year}_{pad(day)}_b.py"
if not os.path.isfile(b_file_name):
    open(b_file_name, "w", encoding="utf-8").write(b_txt)
else:
    raise FileExistsError(filename=b_file_name)


open(f"{new_day_path}/Solve{year}_{pad(day)}_b.py", "w", encoding="utf-8").write(b_txt)


# Setting the source and the destination folders
src = os.getcwd().replace("\\", "/")
dst = new_day_path

# copy the common utilities over from here to "new day"
orig = open("my_utils.py", "r").read()
orig = orig.replace(":config_path:", cfg_root)
open(dst + "/" + "my_utils.py", "w").write(orig)

# write the input.txt
data_src = aoc_puzzle.input_data
open(dst + "/" + "input.txt", "w").write(data_src)


path_2_black_from = "/".join(new_day_path.split("/")[:-1])
path_2_black = "/" + new_day_path.split("/")[-1]

os.chdir(path_2_black_from)
black_cmd = "black " + f'"./Day {pad(day)}/"' + " -W 2 -q --fast"

os.system(black_cmd)
print("All Done")
