from bs4 import BeautifulSoup
import urllib.request
import re

def main():
    # Open the read urls file and iterate over the first 8 links and designate them into their own urls
    url_list = open("readurls.txt", "r").read().split("\n")
    a = 1
    for url in url_list:
        filename = "text" + str(a) + ".txt"
        my_url = url
        html = urllib.request.urlopen(my_url)
        soup = BeautifulSoup(html)
        data = soup.findAll(text=True)
        result = filter(visible, data)
        temp_list = list(result)
        temp_str = ' '.join(temp_list)
        with open(filename, "w") as f2:
            f2.write(str((temp_str).encode("utf-8")))

        a += 1


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

if __name__ == '__main__':
    main()