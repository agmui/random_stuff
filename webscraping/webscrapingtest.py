from bs4 import BeautifulSoup
import requests
import sys
from lxml import html

"""sys.stdout = open('output.html', 'wt')
res = requests.get('https://ahs-fusd-ca.schoolloop.com/portal/login')

print(str(res.text))

soup = BeautifulSoup(res.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# print the result
#print(page_title)
"""

USERNAME = "amui",  # "Morshu",
PASSWORD = "momand123"  # "kumar4567"

URL = "https://ahs-fusd-ca.schoolloop.com/portal/login?etarget=login_form"


def main():
    session = requests.session()

    # Get login csrf token
    result = session.get(URL)
    tree = html.fromstring(result.text)
    form_data_id = list(set(tree.xpath("//input[@name='form_data_id']/@value")))[0]

    # Create payload
    payload = {
        "login_name": USERNAME,
        "password": PASSWORD,
        "form_data_id": form_data_id,
        "event_override": "login"
    }

    session.post(URL, payload)
    session = session.get("https://ahs-fusd-ca.schoolloop.com/portal/student_home")

    #sys.stdout = open('output.html', 'wt')
    #print(session.text)

    soup = BeautifulSoup(session.content, 'html.parser')
    output = findTag(soup, 'div', 'class', 'ajax_accordion_row')
    soup = BeautifulSoup(str(output), 'html.parser')
    print(output)
    #print(findTag(soup, 'td', 'class', 'column padding_5'))

def findTag(soup, tag, type, name):
    _break = False
    l = ""
    for i in soup.find_all(tag):
        # print(i)
        try:
            if i.get(type)[0] == name:
                # print(i)
                l += i + "\n"
                _break = True
        except:
            pass
        if _break:
            pass#break
    return l

if __name__ == '__main__':
    main()
