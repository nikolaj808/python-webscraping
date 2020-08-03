from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#my_url = 'https://sharkgaming.dk/gaming-computere/shark-series'
my_url = 'https://da.wikipedia.org/wiki/Sebastian_Vettel'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab each product
trs = page_soup.findAll("tr")
info = []

for tr in trs:
    if (tr.th != None and tr.td != None):
        left = tr.th.text.strip()
        right = tr.td.text.strip()
        print(left + ": " + right + "\n")
    elif (tr.th != None and tr.td == None):
        left = tr.th.text.strip()
        if (tr.find("th", colspan="2") != None):
            print(left + "(Overskrift)" + "\n")
        else:
            print(left + "\n")
    elif (tr.th == None and tr.td != None):
        right = tr.td.text.strip()
        print(right + "\n")

'''
for tr in trs:
    insertion = ""
    if (tr.th != None):
        left_html = tr.th.text.strip('\n')
        insertion = (left_html)
    if (tr.td != None):
        right_html = tr.td.text.strip('\n')
        if (tr.th != None):
            insertion += (": " + right_html)
    info.append(insertion)

print(info)
'''
