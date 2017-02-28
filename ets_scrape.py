from bs4 import BeautifulSoup
import pickle
import requests



class Issue(object):
    def __init__(self):
        self.issue = []

    def __iter__(self):
        return self.issue

    def scrape_issue(self):
        """
        Scrape
        :return: Scrape ETS Website for Issue Pool
        """
        issue_page = requests.get('http://www.ets.org/gre/'
                                  'revised_general/prepare/'
                                  'analytical_writing/issue/pool')
        soup = BeautifulSoup(issue_page.content, "lxml")
        divider_tag = soup.find("div", "divider-50")
        divider_tag = divider_tag.next_siblings
        content = " "
        for tag in divider_tag:
            tag = BeautifulSoup(str(tag), "lxml")

            if tag.p is not None:
                issue_content = tag.p.getText()
            else:
                issue_content = ""

            if tag.div is not None:
                specification_tag = str(tag.div['class'][0])
                if specification_tag == "divider-50":
                    self.issue.append(content)
                    content = " "

            content += issue_content + "\n"

    def save(self):
        """
        Save to pickle
        :return: Save to pickle
        """
        with open('issue_pool.pkl', 'wb') as f:
            pickle.dump(self.issue, file=f)


class Argument(object):
    def __init__(self):
        self.argument = []

    def __iter__(self):
        return self.argument

    def scrape_argument(self):
        """
        Scrape
        :return: Scrape ETS Website for Argument Pool
        """
        argument_page = requests.get('http://www.ets.org/gre/'
                                     'revised_general/prepare/'
                                     'analytical_writing/argument/pool')
        soup = BeautifulSoup(argument_page.content, "lxml")
        # Divider Tag with class "divider-50" separates each topic
        divider_tag = soup.find("div", "divider-50")
        # Gets all tags on the same level as div tag.
        # All topics are on the same level as divider 50 tag
        divider_tag = divider_tag.next_siblings
        content = " "
        for tag in divider_tag:
            tag = BeautifulSoup(str(tag), "lxml")

            if tag.p is not None:
                issue_content = tag.p.getText()
            else:
                issue_content = ""

            if tag.div is not None:
                specification_tag = str(tag.div['class'][0])
                if specification_tag == "divider-50":
                    # Append and advance to the new topic
                    self.argument.append(content)
                    content = " "

            content += issue_content + "\n"

    def save(self):
        """
        Save to pickle
        :return: Save to pickle
        """
        with open('argument_pool.pkl', 'wb') as fp:
            pickle.dump(self.argument, fp)


def scrape():
    """
    Main function
    :return: 
    """
    issue = Issue()
    issue.scrape_issue()
    issue.save()
    argument = Argument()
    argument.scrape_argument()
    argument.save()

if __name__ == "__main__":
    scrape()
