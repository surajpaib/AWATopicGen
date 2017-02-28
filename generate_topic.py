import pickle
from random import choice

from clint import arguments
from clint.textui import colored, puts
from scrapingmodule.ets_scrape import Issue, Argument
def input_flags():
    args = arguments.Args()
    return str(args.flags[0])

def load_issue():
    # Read File
    with open('./scrapingmodule/issue_pool.pkl', 'rb') as f:
        issues = pickle.load(f)

    random_choice = choice(issues)
    puts(colored.green(random_choice))
    puts(colored.blue("Topics Remaining: {0}".format(len(issues))))
    for i, content in enumerate(issues):
        if random_choice == content:
            break
    issues.remove(issues[i])

    # Write File

    with open('./scrapingmodule/issue_pool.pkl', 'wb') as fp:
        pickle.dump(issues, fp)




def load_arg():
    with open('./scrapingmodule/argument_pool.pkl', 'rb') as f:
        arg = pickle.load(f)

    random_choice = choice(arg)
    puts(colored.red(choice(arg)))
    puts(colored.blue("Topics Remaining: {0}".format(len(arg))))
    for i, content in enumerate(arg):
        if random_choice == content:
            break
    arg.remove(arg[i])
    # Write File

    with open('./scrapingmodule/argument_pool.pkl', 'wb') as fp:
        pickle.dump(arg, fp)


def reload_files():
    issue = Issue()
    issue.scrape_issue()
    issue.save()
    arg = Argument()
    arg.scrape_argument()
    arg.save()

def run():

    if input_flags() == "--issue":
        load_issue()
    if input_flags() == "--argument":
        load_arg()
    if input_flags() == "--reset":
        reload_files()




if __name__ == "__main__":
    run()