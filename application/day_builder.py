"""usage:

import day_builder
daybuilder.main(year, day) -> files

{
    "instructions.md": contents,        
    "solve2023_10_a.py": contents,      X
    "solve2023_10_b.py": contents,
    "example.txt: contents,             X
    "input.txt": contents,              X
    "local_utils.py": contents,
    "setup.py": contents,
    "readme.md": contents
}

"""
import os
import sys
import puzzlestuff
import pathfile
import timestuff


###############################################################################
# incoming arguments if this is run from commandline
###############################################################################
os.system("cls")

arg_keys = sys.argv[1:]
# print(sys.argv)
# print(arg_keys)


arg_dict = {x.lower(): int(y) for x, y in zip(arg_keys[0::2], arg_keys[1::2])}

# print(__file__)
# print(arg_dict)


# sys.exit()

if "-y" in arg_dict:
    year = arg_dict["-y"]
else:
    year = timestuff.year_now()

if "-d" in arg_dict:
    day = arg_dict["-d"]
else:
    day = timestuff.day_now()


print("did we get a year and day from args?", year, day)

USER_NAME = "friargregarious"

puzzle_fn = f"{year}-{day:02}.aocd"
cfg = pathfile.get_cfg()  # "./application/configs/users.ini"

games_loc = cfg.get("game_paths", "games_root")

puzzle_loc = cfg.path_to("game_paths", "puzzle_path")

PUZZLE_PATH = pathfile.path(puzzle_loc, puzzle_fn)
# user_path = build_utils.path(puzzle_loc, "user.aocd")

user_email, user_home, user_id, token = cfg.getlist("current_users", USER_NAME)


if os.path.isfile(PUZZLE_PATH):
    our_puzzle = pathfile.unpickle_me(PUZZLE_PATH)
    our_user = our_puzzle.user
else:
    our_puzzle = puzzlestuff.refresh_puzzle(year, day, token)
    our_user = our_puzzle.user
    pathfile.pickle_me(PUZZLE_PATH, our_puzzle)

if "-b" in arg_keys:  # force an update of our puzzle file.
    print("Forcing update of puzzle data due to solving of A.")
    our_puzzle = puzzlestuff.refresh_puzzle(year, day, token, force=True)
    our_user = our_puzzle.user
    pathfile.pickle_me(PUZZLE_PATH, our_puzzle)

return_file_data, return_rep_data = puzzlestuff.get_puzzle_data(our_puzzle)


# user_email, user_home, user_id, token
format_data = {
    "git_home": user_home,
    "user_name": USER_NAME,
    "user_email": user_email,
}

format_data.update(return_rep_data)
format_data.update(return_file_data)

# format_data.update(return_rep_data)
# format_data.update(return_file_data)

if our_puzzle.answered_a:  # build B
    format_data["example_ans"] = format_data["examples"][0].answer_b
    format_data["part"] = "b"

else:  # if not our_puzzle.answered_a:  # build A
    format_data["example_ans"] = format_data["examples"][0].answer_a
    format_data["part"] = "a"

today_path = puzzlestuff.today_path(year, day)

solve_file_text = puzzlestuff.SolveHeader(format_data).text
solve_file_text += puzzlestuff.Solvebody(format_data).text
solve_file_text = solve_file_text.replace("\t", "    ")

if not os.path.isdir(today_path):
    os.makedirs(today_path, exist_ok=True)

# files = [filepath, content] for bulking the write jobs
files = []

if not our_puzzle.answered_a:
    # format_data["year"] = str(year)
    format_data["year"] = year
    print("############", format_data["year"])
    if "year" in format_data:
        # write the utilties file
        U_PATH = pathfile.path(today_path, "my_utilities.py")
        u_text = open("my_utils.py", encoding="utf-8").read()
        u_text = u_text.format(format_data)
        files.append([U_PATH, u_text])

    # write the example.txt
    E_PATH = pathfile.path(today_path, "example.txt")
    e_text = format_data["examples"][0].input_data
    files.append([E_PATH, e_text])

    # write the inputs.txt
    I_PATH = pathfile.path(today_path, "inputs.txt")
    i_text = format_data["input_data"]
    files.append([I_PATH, i_text])

    # create and write the .env file for this puzzle
    env_text = f"[puzzle]\npfname = {PUZZLE_PATH}\n"
    files.append([pathfile.path(today_path, ".env"), env_text])

# write the instructions.md
I_PATH = pathfile.path(today_path, "instructions.md")
i_text = format_data["instructions"]
files.append([I_PATH, i_text])

# write the solve bp
y_path = puzzlestuff.solve_file_name(year, day, format_data["part"])
files.append([y_path, solve_file_text])

for fname, content in files:
    open(fname, "w", encoding="utf8").write(content)

os.system(f'black "{today_path}" -q --safe')
