import pickle
import smtplib
from random import choice

from clint import arguments
from clint.textui import colored, puts
from scrapingmodule.ets_scrape import Issue, Argument

def send_mail(recipients, subject, message):
    header = 'From: surajballambat@gmail.com\n'
    header += 'To: {0}\n'.format(",".join(recipients))
    header += 'Subject: {0}\n'.format(subject)
    message = header + message

    # Replace with username and password of the account you want to send the mail from
    username = pickle.loads('credentials.pkl')
    username = username[0]
    password = username[1]
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    problems = server.sendmail('surajballambat@gmail.com', recipients, message)
    server.quit()

def input_flags():
    args = arguments.Args()
    return str(args.flags[0])

def load_issue():
    # Read File
    with open('./scrapingmodule/issue_pool.pkl', 'rb') as f:
        issues = pickle.load(f)

    random_choice = choice(issues)
    puts(colored.green(random_choice))
    send_mail(['surajballambat@gmail.com'], 'Issue Topic', random_choice)
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
    send_mail(['surajballambat@gmail.com'], 'Argument Topic', random_choice)
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