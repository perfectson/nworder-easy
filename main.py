from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
print(html_bytes)
html = html_bytes.decode("utf-8")
print(html)
#https://realpython.com/python-web-scraping-practical-introduction/
#https://support.zendesk.com/hc/en-us/community/posts/360029389614-Extracting-chats-details-with-API-measuring-C-sat-request-rate
