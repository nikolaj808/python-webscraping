from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#my_url = 'https://sharkgaming.dk/gaming-computere/shark-series'
my_url = 'https://sharkgaming.dk/gaming-computere/mighty-shark-series'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("li", {"class":"item"})
print(containers)

for container in containers:
    product_name_html = container.findAll("h2", {"class":"product-name"})
    product_name = product_name_html[0].text.strip()

    product_specs_html = container.findAll("div", {"class": "desc std std2"})
    product_specs = product_specs_html[0].text.strip()

    product_price_html = container.findAll("span", {"class": "price"})
    product_price = product_price_html[0].text.strip()

    product_delivery_html = container.findAll("p", {"class": "availability"})
    product_delivery = product_delivery_html[0].text.strip()

    print(product_name)
    print(product_specs)
    print(product_price)
    print(product_delivery)
    print("\n")

