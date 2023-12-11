"""common tools or extentions of regular tools that
I like to use in this application
"""
import os
from configparser import ConfigParser
import aocd

__config_path__ = ":config_path:"
__puzzle_year__, __puzzle_day__ = ":year:", ":day:"

def solve_file_names(part):
    return f"Solve{__puzzle_year__}_{__puzzle_day__}{part}.py"


class MyConfigParser(ConfigParser):
    """regular configparser doesn't make lists easy"""

    cfg_path = ""

    def getlist(self, section, option):
        """pulls a list from a config element"""
        value = self.get(section, option)
        # return list(filter(None, (x.strip() for x in value.splitlines())))
        return list(value.strip().split(","))

    def getlistint(self, section, option):
        """pulls a list of ints from a config element"""
        return [int(x) for x in self.getlist(section, option)]

    def putlist(self, section, option, content):
        """puts a list into an element as a str"""
        self[section][option] = ",".join([f"{x}" for x in content])

    def save_me(self, cfg_name: str):
        """saves config file incase we changed anything"""
        save_to = self.cfg_path + cfg_name + ".ini"
        try:
            with open(save_to, "w", encoding="utf-8") as cfgsave:
                self.write(cfgsave)
            return os.path.isfile(save_to)
        except FileNotFoundError as e:
            sys.exit(e)


def version_increment(file: str, big: int = 0, med: int = 0, sml: int = 0):
    file_to_increment = solve_file_names[file]
    file_text = open(file_to_increment, encoding="utf-8").read().splitlines()

    new_text = []

    for line in file_text:
        if line.startswith("__version__"):
            new_line, old_version = line.split(" = ")
            o_big, o_med, o_sml = [int(x) for x in old_version.strip().split(".")]
            n_big = o_big + big
            n_med = o_med + med
            n_sml = o_sml + sml
            new_vers = f" = {n_big}.{n_med}.{n_sml}"
            new_text.append(new_line + new_vers)
        else:
            new_text.append(line)

    open(file_to_increment, "w", encoding="utf-8").write("\n".join(new_text))

def solve_me(part:str, answer=None):
    if answer is not None:
        
    