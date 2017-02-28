import requests
from bs4 import BeautifulSoup

def scrape():
    """
    
    :return: 
    """
    issue_webpage = requests.get('http://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool')
    argument_webpage = requests.get('http://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool')
    issue_topics = BeautifulSoup(issue_webpage.content)
    issue_topics = issue_topics.find_all('p')
    for issue in issue_topics:
        print(issue)
        i = BeautifulSoup(str(issue))
        i = i.find('p').getText()
        print(i)
        break

if __name__ == "__main__":
    scrape()