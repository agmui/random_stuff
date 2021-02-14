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

USERNAME = "Morshu",
PASSWORD = "kumar4567"


URL = "https://ahs-fusd-ca.schoolloop.com/portal/login?etarget=login_form"

def main():
    session = requests.session()

    # Get login csrf token
    result = session.get(URL)
    tree = html.fromstring(result.text)
    form_data_id = list(set(tree.xpath("//input[@name='form_data_id']/@value")))[0]

    tree = html.fromstring(result.text)
    return_url = list(set(tree.xpath("//input[@name='return_url']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "form_data_id": form_data_id,
        "return_url": return_url
    }

    session.post(URL, payload)

    session = session.get(URL)

    sys.stdout = open('output.html', 'wt')
    print(session.text)

if __name__ == '__main__':
    main()
