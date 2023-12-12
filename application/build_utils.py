import os

# import sys
from glob import glob

# https://betterprogramming.pub/load-fast-load-big-with-compressed-pickles-5f311584507e
import pickle
import bz2
from configparser import NoOptionError, NoSectionError
from time import sleep
from my_utils import MyConfigParser as cParser
# from datetime import datetime

import platform
from urllib.parse import quote

# import requests
# https://github.com/borisbabic/browser_cookie3
# import browser_cookie3
import aocd
import aoc_to_markdown as a2m

# https://github.com/astrowonk/aoc_dashboard

from app_utils import path


def compressed_pickle(title, data):
    """Saves the "data" with the "title" and adds the .pickle"""

    # with open(title + ".aocd", "wb") as pikd:
    #     pickle.dump(data, pikd)
    if not title.endswith(".aocd"):
        title += ".aocd"

    with bz2.BZ2File(title, "w") as f:
        pickle.dump(data, f)


def loosen(file):
    """loads and returns a pickled objects"""
    # with open(file, 'rb') as pikd:
    # data = pickle.load(pikd)
    if file.endswith(".aocd"):
        data = bz2.BZ2File(file, "rb")
        data = pickle.load(data)
        return data
    raise TypeError


def get_cfg(cfg_name: str):
    """quick cfg loader"""

    if not (cfg_name == "local"):
        # when cParser is being used outside the application folder
        # we need to let it know where to find the cfg files.
        cParser.cfg_path = cfg_path

        found = glob("*.ini", root_dir=cfg_path)
        # available = [x.split("\\")[1].split(".")[0] for x in found]
        available = [x.split(".")[0] for x in found]

        if cfg_name in available:
            this_cfg = cParser()
            # cool new way to just load it all!!!
            # this_cfg.read(found:list)
            cfg_file = f"{cfg_path}/{cfg_name}.ini"
            print(cfg_file)
            this_cfg.read(cfg_file)
            return this_cfg
        raise FileNotFoundError
    this_cfg = cParser()
    this_cfg.read(f"./{cfg_name}.ini")
    return this_cfg


# grabbing some path information
local_cfg = get_cfg("local")

# this is the cwd
app_root = local_cfg.get("paths", "app_root")

# this is a child folder of here
cfg_path = app_root + local_cfg.get("paths", "cfg_path")

# this is the root of the games folder
games_root = local_cfg.get("paths", "games_root")


def refresh_user(token):
    try:
        pickled_user_loc = local_cfg.get("paths", "user_aocd")
    except NoOptionError:
        print("That location was not found in local configs.")
        print("rebuilding element.")
        pickled_user_loc = path(games_root, "user.aocd")
        # local_cfg.get("paths", "games_root")
        local_cfg["paths"]["user_aocd"] = pickled_user_loc
        local_cfg.save_me("./local.ini")
        print("Local configs updated.")

    # now to open the file and get the object out of it.
    if os.path.isfile(pickled_user_loc):
        waiting = "Pulling Local User data ".rjust(30) + "." * 5
        user = loosen(pickled_user_loc)
        waiting += "." * 5 + " Got User Data"
    else:
        waiting = "Pulling User data ".rjust(30)
        user = aocd.models.User(token=token)
        for _ in range(10):
            waiting += "."
            os.system("cls")
            print(waiting)
            sleep(1)
        waiting += " Got User Data"

    return user


def refresh_stats(token):
    user = refresh_user(token)

    try:
        pickled_stats_loc = local_cfg.get("paths", "stats_aocd")
    except NoOptionError:
        print("That location was not found in local configs.")
        print("rebuilding element.")
        pickled_stats_loc = path(games_root, "stats.aocd")
        local_cfg["paths"]["stats_aocd"] = pickled_stats_loc
        local_cfg.save_me("./local.ini")
        print("Local configs updated.")

    # now to open the file and get the object out of it.
    if os.path.isfile(pickled_stats_loc):
        waiting = "Pulling Local stats data ".rjust(30) + "." * 5
        stats = loosen(pickled_stats_loc)
        waiting += "." * 5 + " Got stats Data"
    else:
        waiting = "Pulling stats data ".rjust(30)
        print(waiting)
        stats = user.get_stats()
        for _ in range(10):
            waiting += "."
            os.system("cls")
            print(waiting)
            sleep(1)
        waiting += " Got stats Data"
        print("Saving Stats data")
        compressed_pickle(pickled_stats_loc, stats)
        print("Saved Stats to file.")

    return stats


def refresh_puzzle(year:int, day:int, token:str):
    """default placeholder """

    user = refresh_user(token)
    solve_path = path(games_root, f"AOC {year}", f"Day {day:02}")
    pickled_game_loc = path(solve_path, f"/P{year}_{day}.aocd")

    try:
        pickled_game_loc = local_cfg.get("paths", "stats_aocd")
    except NoOptionError:
        print("That location was not found in local configs.")
        print("rebuilding element.")
        pickled_game_loc = path(games_root, "puzzle.aocd")
        local_cfg["paths"]["stats_aocd"] = pickled_game_loc
        local_cfg.save_me("./local.ini")
        print("Local configs updated.")

    if os.path.isfile(pickled_game_loc):
        puzzle = loosen(pickled_game_loc)
        print("Got Local Puzzle Data")

    else:
        print("pulling Puzzle data ")
        puzzle = aocd.models.Puzzle(year, day, user)
        sleep(10)
        print("pulling Puzzle data ")

        compressed_pickle(solve_path + f"/P{year}_{day}", puzzle)

    print("done downloading!!")
    return puzzle


def example_file(year: int, day: int):
    # Example(
    #   input_data='...\n#...#.....',
    #   answer_a='374',
    #   answer_b=None,
    #   extra=None
    # )
    pass


def get_puzzle_data(year, day, token):
    """ placeholder """
    puzzle = refresh_puzzle(year, day, token)

    for i in puzzle.examples:
        print(i)


    return_file_data = {
        "instructions": a2m.get_markdown(year, day),
        "examples": puzzle.examples[0],
        # "my_stats": _stats,
        "input_data": puzzle.input_data
        }
    return_rep_data = {
        ":input_url:": puzzle.input_data_url,
        ":games_root:": games_root,
        ":title:": puzzle.title.title(),
        ":year:": str(year),
        ":day:": str(day),
        ":pyversion:": platform.python_version(),
        ":config_path:": ""
        }


    return return_file_data, return_rep_data


# def build_instructions(inst_text: str, new_day_path: str):
#     newfilename = new_day_path + "/instructions.md"

#     try:
#         open(newfilename, "w", encoding="utf-8").write(inst_text)
#     except FileExistsError as e:
#         return e
#     return os.path.isfile(newfilename)


# def build_examples(example_text: str, new_day_path: str):
#     newfilename = new_day_path + "/example.txt"

#     try:
#         open(newfilename, "w", encoding="utf-8").write(inst_text)
#     except FileExistsError as e:
#         return e
#     return os.path.isfile(newfilename)


# # copied from rename_data.py and hasn't
# # been converted for this module yet

# def write_setup(year, day):
#     """placeholder statement"""
#     name = f"Solve_{year}_{str(day).rjust(2,'0')}"

#     work_source = "C:\\AOC 2023\\example of new puzzle\\setup.py"
#     work_target = "setup.py"

#     raw = open(work_source).read()
#     raw = raw.replace("{#YEAR}", str(year), 99)
#     raw = raw.replace("{#DAY}", str(day), 99)
#     raw = raw.replace("{#NAME}", str(name), 99)
#     open(work_target, "w", encoding="UTF-8").write(raw)

###############################################################################
# def print_inputs_and_readme(year, day):
#     """placeholder statement"""
#     # markdown_cmd = f"aoc-to-markdown -y {year} -d {day} -o readme.md -i"
#     markdown_cmd = f"aoc-to-markdown -y {year} -d {day} -o mkd -i"
#     print(f"now running {markdown_cmd}")
#     os.system(markdown_cmd)
#     # -s/day-24/

#     dstr = str(day).rjust(2, "0")

#     atm_files = [f"mkd/day-{dstr}/input.txt", f"mkd/day-{dstr}/readme.md"]
#     for wrong_file in atm_files:
#         if os.path.isfile(wrong_file):
#             temp = open(wrong_file).read()

#             if wrong_file.endswith(".txt"):
#                 open("input.txt", "w", encoding="UTF-8").write(temp)

#             if wrong_file.endswith(".md"):
#                 open("readme.md", "w", encoding="UTF-8").write(temp)

#             os.remove(wrong_file)

#     os.removedirs(f"mkd/day-{dstr}/")

# if __name__ == "__main__":
#     # Prep lines
#     ROOT = "c:/Advent of Code"
#     if not os.path.exists(ROOT):
#         print(f"{ROOT} does not exist, making the folder.")
#         os.mkdir(ROOT)

#     mefile = get_me(ROOT + "/me.aocd")

#     # get year
#     get_year = aocd.get.most_recent_year()
#     MSG = "Enter the 4 digit YEAR (earliest is 2015) for the puzzles "
#     MSG += f"you'd like.\nLeave empty for most recent event year [{get_year}]\n  --> "

#     # year = datetime.now().year
#     response = input(MSG)
#     if response.isnumeric():
#         year = int(response)
#     else:
#         year = get_year

#     # get day
#     get_day = aocd.get.current_day()
#     MSG = "Enter the DAY number (1-25) for the puzzles you'd like.\n"
#     MSG += f"Leave empty for today or day 1. [{get_day}]  \n--> "
#     response = input(MSG)
#     if response.isnumeric():
#         day = int(response)
#     else:
#         day = get_day

#     # get decision
#     MSG = "1) Populate entire folder or,\n2) Just part 'B' \n--> "
#     decision = int(input(MSG))

#     if decision not in [1, 2]:
#         print("you gotta pick a number, 1 or 2. It's not that hard.")
#         os.sys.exit()

#     elif decision == 2:
#         work_folder = day_dir(year_dir(ROOT, year), day)
#         os.chdir(work_folder)
#         print_inputs_and_readme(year, day)

#     elif decision == 1:
#         for year, day in gen_dates(year, day):
#             # build the year folder if it doesn't exist already
#             work_folder = day_dir(year_dir(ROOT, year), day)

#             print(f"Our workfolder is: {work_folder}")

#             if not os.path.exists(work_folder):
#                 print(f"{work_folder+'/'} does not exist, making the folder.")
#                 print(f"os.path.dirname = {os.path.dirname(work_folder+'/')}")
#                 os.makedirs(os.path.dirname(work_folder + "/"), exist_ok=True)
#             #     os.mkdir(work_folder)
#             os.chdir(work_folder)

#             # PUZZLEFILE = work_folder + "\\puzzle.aocd"
#             PUZZLEFILE = "puzzle.aocd"

#             if os.path.isfile(PUZZLEFILE):
#                 try:
#                     puzzle = pickle.load(open(PUZZLEFILE, "rb"))
#                 except EOFError:
#                     time.sleep(5)
#                     puzzle = aocd.models.Puzzle(year, day, mefile)

#             else:
#                 time.sleep(5)
#                 puzzle = aocd.models.Puzzle(year, day, mefile)

#             pickle.dump(puzzle, open(PUZZLEFILE, "wb"))

#             write_work(year, day, puzzle)
#             write_setup(year, day)

#             print_inputs_and_readme(year, day)
