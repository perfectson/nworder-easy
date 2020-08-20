from urllib.request import urlopen

def getHtmlContent(url):
    page = urlopen(url)
    html_bytes = page.read()
    print(html_bytes)
    html = html_bytes.decode("utf-8")
    print(html)
