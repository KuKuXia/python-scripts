"""
Get all links from a webpage
"""

import re
import requests

# get url
url = input('Enter a url, include: http://')

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall(r'"((http|ftp)s?://.*?)"', html)

# output links
for link in links:
    print(link[0])
