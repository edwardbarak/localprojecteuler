from bs4 import BeautifulSoup
from sys import argv
import os
import requests

# variables
url = 'https://projecteuler.net/problem='

# get 
urlpage = requests.get(url + str(argv[1]))
soup = BeautifulSoup(urlpage.text, 'html.parser')

# extract page data
header = soup.h2.text
p = soup.p(attr={'class': 'problem_content'})

# format page data as markdown
markdown = '# %s\n## %s\n%s\nAnswer: ' % (header, str(argv[1]), '\n'.join(p))
if len(argv) == 3:
    markdown += str(argv[2])

# create/access problem's folder
path = '%s/%s' % (os.getcwd(), str(argv[1]))
if not os.path.exists(path):
    os.mkdir(path)

# write readme
with open(path + '/README.md', 'w') as f:
    f.write(markdown)
