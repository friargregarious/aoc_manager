import os
import sys
from glob import glob
from my_utils import MyConfigParser as cParser
from datetime import datetime
import aocd
import platform
from urllib.parse import quote
import requests
import browser_cookie3


# grabbing some path information
local_cfg = get_cfg("local")

# this is the cwd
app_root = local_cfg.get("paths", "app_root")

# this is a child folder of here
cfg_path = app_root + local_cfg.get("paths", "cfg_path")

# this is the root of the games folder
games_root = local_cfg.get("paths", "games_root")


def get_cfg(cfg_name: str):
    """quick cfg loader"""

    if not (cfg_name == "local"):
        # when cParser is being used outside the application folder
        # we need to let it know where to find the cfg files.
        cParser.cfg_path = cfg_path

        found = glob("*.ini", root_dir=cfg_path)
        available = [x.split("\\")[1].split(".")[0] for x in found]

        if cfg_name in available:
            this_cfg = cParser()
            this_cfg.read(  ,  f"{cfg_path}/{cfg_name}.ini")
            return this_cfg
        raise FileNotFoundError
    this_cfg = cParser()
    this_cfg.read(f"./{cfg_name}.ini")
    return this_cfg

def get_puzzle_data(year, day, token):
    """ """

    user = aocd.models.User(token=token)
    puzzle = aocd.models.Puzzle(year, day, user)
        
    # useremail = "greg.denyes@gmail.com"
    #     ":useremail:": useremail,

    return_data = {
        "instructions" : aocd.get_data(token, day, year),
        "examples" : puzzle.examples,
        "my_stats" : user.get_stats(),
        ":input_url:" : puzzle.input_data_url,
        ":games_root:" : games_root,
        ":title:": puzzle.title.title(),
        ":year:": str(year),
        ":day:": str(day),
        ":pyversion:": platform.python_version(),
    }

    return return_data

def build_instructions(inst_text:str, new_day_path:str):
    newfilename = new_day_path + "/instructions.md"

    try:
        open(newfilename, "w", encoding="utf-8").write(inst_text)
    except FileExistsError as e:
        return e
    return os.path.isfile(newfilename)


def build_examples(example_text:str, new_day_path:str):
    newfilename = new_day_path + "/example.txt"

    try:
        open(newfilename, "w", encoding="utf-8").write(inst_text)
    except FileExistsError as e:
        return e
    return os.path.isfile(newfilename)


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