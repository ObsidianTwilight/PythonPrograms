from collections import Counter
from colorama import Fore, Style, init
init(autoreset=True)
from termcolor import colored

a = "aaaaaabbbbbbbbcc"

my_counter =Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
#Most common element in counter dictionary
print("-----------------------------------------------------------------------------------------")
print("This is from termcolor:🌈")
print(colored("Most common elements:🤗 ", "blue"), colored(str(my_counter.most_common()), "green"))
print(colored("Two most common elements:👀 ", "light_green"), colored(str(my_counter.most_common(2)), "green"))
print(colored("Indexwise most common elements:👉🏻 ", "light_red"), colored(str(my_counter.most_common(2)[0]), "green"))
print(colored("Only most common element:1️⃣ ", "light_cyan"), colored(str(my_counter.most_common(2)[0][0]), "green"))
print(colored("most common keys: ", "light_cyan"), colored(str(my_counter.elements()), "green"))
