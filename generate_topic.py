from clint.textui import colored, indent, puts
from clint import arguments
from random import choice
import pickle

def input_flags():
    args = arguments.Args()
    return str(args.flags[0])

def load_issue():
    with open('issue_pool.pkl', 'rb') as f:
        issues = pickle.load(f)

    puts(colored.green(choice(issues)))

def load_arg():
    with open('argument_pool.pkl', 'rb') as f:
        arg = pickle.load(f)

    puts(colored.red(choice(arg)))

def run():

    if input_flags() == "--issue":
        load_issue()
    if input_flags() == "--argument":
        load_arg()




if __name__ == "__main__":
    run()