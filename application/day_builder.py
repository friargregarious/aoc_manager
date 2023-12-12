"""usage:

import day_builder
daybuilder.main(year, day) -> files

{
    "instructions.md": contents,
    "solve2023_10_a.py": contents,
    "solve2023_10_b.py": contents,
    "example.txt: contents,
    "input.txt": contents,
    "local_utils.py": contents,
    "setup.py": contents,
    "readme.md": contents
}

"""
import os
import sys
from datetime import datetime

import platform
from urllib.parse import quote
import requests
import browser_cookie3
import build_utils
from build_utils import path


###############################################################################
os.system("cls")


# env_cfg = build_utils.get_cfg("env")  # cParser()
env_cfg = build_utils.get_cfg("local")  # cParser()
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
# print(f"|<{' ' * (80-4)}>|")


def parse_info(user, puzzle):
    """ """
    homename, username, userid = user.id.split(".")
    userhome = f"github.com/{username}"
    usersource_url = f"~/Advent-of-Code/AOC {puzzle.year}/Day {puzzle.day:02}"

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
    u_emali, u_home, u_id, token = user_cfg.getlist("current_users", "friargregarious")
    u_id = int(u_id)

# aoc_user, aoc_puzzle = build_utils.get_puzzle_data(year, day, token)
# now this is a dict of final answers

file_data, rep_data = build_utils.get_puzzle_data(year, day, token)
# return_file_data, return_rep_data

# input_url = rep_data[]
bannerline = "#" * 79
# useremail = "greg.denyes@gmail.com"
game_root = env_cfg["paths"]["games_path"]


# return_data = {
#     "file_data": {
#         "instructions": a2m.get_markdown(year, day),
#         "examples": puzzle.examples[0],
#         # "my_stats": _stats,
#         "input_data": puzzle.input_data
#         },
#     "rep_data": {
#         ":input_url:": puzzle.input_data_url,
#         ":games_root:": games_root,
#         ":title:": puzzle.title.title(),
#         ":year:": str(year),
#         ":day:": str(day),
#         ":pyversion:": platform.python_version(),
#         }
# }

def banner(title):
    new_banner = [
        bannerline,
        f"# {title.upper().strip()} {bannerline}"[:79],
        bannerline,
    ]
    return "\n" + "\n".join(new_banner) + "\n"


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
        # for lookfor, replacewith in replacements.items():
            # if lookfor in line:
        new_line = new_line.format(**rep_data)
        new_line = f"#{new_line: ^78}#"

    else:  # left/right lists
        left, right = line

        # for lookfor, replacewith in replacements.items():
            # if lookfor in right:
        right = right.format(**rep_data)

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

outputs.extend(parts)
outputs.extend(main_entry)
outputs.extend(running_from_home)
rep_data[":part:"]="a"
a_output_text = "\n".join(outputs).format(**rep_data)

outputs_b.extend(parts)
outputs_b.extend(main_entry)
outputs_b.extend(running_from_home)
rep_data[":part:"]="b"
b_output_text = "\n".join(outputs_b).format(**rep_data)


# for line in parts:
#     outputs.append(line.format(**rep_data))
#     outputs_b.append(line.format(**rep_data))

# for line in main_entry:
#     outputs.append(line.format(**rep_data))
#     outputs_b.append(line.format(**rep_data))

# for line in running_from_home:
#     outputs.append(line.format(**rep_data))
#     outputs_b.append(line.format(**rep_data))


###############################################################################
# bring together all the files to write #######################################
###############################################################################

# build common utilities file over from here to "new day" #####################
orig_util = open("my_utils.py", "r").read()

# Setting the source folders ##################################################
src = os.getcwd().replace("\\", "/")  # Here

# create dst ##################################################################
dst = path(game_root, f"AOC {year}", f"Day {day:02}")  # There

if not os.path.isdir(dst):
    os.makedirs(dst)

os.chdir(dst)

# Setting up the file names and content for mass I/O ##########################
files_to_write = []  # [path+filename, content]

# common_ini = path(env_cfg.get("paths", "games_root"), ".ini")
rep_data[":config_path:"] = path(env_cfg.get("paths", "games_root"), ".ini")
# .replace(":config_path:", common_ini)
orig_util = orig_util.format(**rep_data)

files_to_write.append(["my_utils.py", orig_util])

# solve file A
files_to_write.append([f"Solve{year}_{day:02}_a.py",
                       a_output_text
                       ])
# solve file b
files_to_write.append([f"Solve{year}_{day:02}_b.py", b_output_text])

# write the input.txt
# data_src = aoc_puzzle.input_data
files_to_write.extend(
    [
        ["input.txt", rep_data["input_data"]],
        ["instructions.md", rep_data["instructions"]],
        ["example.txt", str(rep_data["examples"])],
    ]
)

for filename, content in files_to_write:
    path = path(dst, content)
    print(path)
    open(path, "w", encoding="utf-8").write(content)


path_2_black_from = "/".join(dst.split("/")[:-1])
path_2_black = "/" + dst.split("/")[-1]

os.chdir(path_2_black_from)
black_cmd = "black " + f'"./Day {day:02}/"' + " -W 2 -q --fast"

os.system(black_cmd)
print("All Done")
