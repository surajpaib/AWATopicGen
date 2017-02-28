import requests
from bs4 import BeautifulSoup

class Issue(object):
    def __init__(self):
        self.issue = []

    def __iter__(self):
        return self.issue

    def scrape_issue(self):
        """
        
        :return: Scrape ETS Website for Issue Pool
        """
        issue_page = requests.get('http://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool')
        soup = BeautifulSoup(issue_page.content, "lxml")
        divider_tag = soup.find("div", "divider-50")
        divider_tag = divider_tag.next_siblings
        content = " "
        for tag in divider_tag:
            tag = BeautifulSoup(str(tag),"lxml")

            if tag.p is not None:
                issue_content = tag.p.getText()
            else:
                issue_content = ""

            if tag.div is not None:
                specification_tag = str(tag.div['class'][0])
                if specification_tag == "divider-50":
                    self.issue.append(content)
                    content = " "


            content += issue_content +"\n"


def scrape():
    """
    
    :return: 
    """
    issue = Issue()
    issue.scrape_issue()


if __name__ == "__main__":
    scrape()