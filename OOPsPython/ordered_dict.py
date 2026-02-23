from collections import OrderedDict
from termcolor import colored
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(colored("Ordered dictionary as you have insert, according to insertion order is maintained: ", "light_cyan"), colored(str(ordered_dict), "green"))