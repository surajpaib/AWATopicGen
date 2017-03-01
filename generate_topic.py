"""
Generate Topics
"""
import pickle
import smtplib
from random import choice
from clint import arguments
from clint.textui import colored, puts
from scrapingmodule.ets_scrape import Issue, Argument


def send_mail(recipients, subject, message):
    """
    Sends Mail
    :param recipients: List of recipients
    :param subject: Subject of the mail
    :param message: Message Body
    :return: Sends mail to the IDs
    """
    header = 'From: surajballambat@gmail.com\n'
    header += 'To: {0}\n'.format(",".join(recipients))
    header += 'Subject: {0}\n'.format(subject)
    message = header + message
    # Replace with username and password of the account you want to send the mail from
    with open('credentials.pkl', "rb") as fp:
        username = pickle.load(fp)
    login = username[0]
    password = username[1]
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(login, password)
    server.sendmail('surajballambat@gmail.com', recipients, message)
    server.quit()


def input_flags():
    """
    Input flags
    :return: Returns the input flags
    """
    args = arguments.Args()
    return str(args.flags[0])


def load(topic_type, recipient_list):
    """
    Load Module
    :param recipient_list: Mail recipient list
    :return: Sends mail and displays topic
    """
    # Read File
    with open('./scrapingmodule/{0}_pool.pkl'.format(topic_type), 'rb') as f:
        topics = pickle.load(f)

    random_choice = choice(topics)
    if topic_type == "issue":
        puts(colored.green(random_choice))
        send_mail(recipient_list, 'Issue Topic', random_choice)
    elif topic_type == "argument":
        puts(colored.red(random_choice))
        send_mail(recipient_list, 'Argument Topic', random_choice)

    for i, content in enumerate(topics):
        if random_choice == content:
            break
    topics.remove(topics[i])
    puts(colored.blue('Topics Remaining: {0}'.format(len(topics))))
    # Write File
    with open('./scrapingmodule/{0}_pool.pkl'.format(topic_type), 'wb') as fp:
        pickle.dump(topics, fp)


def reload_files():
    """
    Load Classes from ets_scrape
    :return: pkl files
    """
    issue = Issue()
    issue.scrape_issue()
    issue.save()
    arg = Argument()
    arg.scrape_argument()
    arg.save()


def run():
    """
    Main
    :return: runs the program
    """
    recipient_list = ['surajballambat@gmail.com']
    if input_flags() == "--issue":
        load("issue", recipient_list=recipient_list)
    if input_flags() == "--argument":
        load("argument", recipient_list=recipient_list)
    if input_flags() == "--reset":
        reload_files()


if __name__ == "__main__":
    run()
