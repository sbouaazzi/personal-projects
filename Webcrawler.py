from bs4 import BeautifulSoup
import requests
from itertools import islice


def main():
    starter_url = "https://www.google.com/search?ei=2FW6W_j0FMXesAWa34vgAQ&q=oasis+band&oq=Oasis&gs_l=psy-ab.1.2.0i71l8.0.0..3348...0.0..0.0.0.......0......gws-wiz.1i0s2JWyKz8"
    r = requests.get(starter_url)

    data = r.text
    soup = BeautifulSoup(data)

    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            print(link_str)
            if 'Oasis' in link_str or 'oasis' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    f.write(link_str + '\n')

    print('---------------------------------------------------')

    # Scrape the first 25 relevent urls
    with open("urls.txt", "r") as myfile:
        head = list(islice(myfile, 25))

    # initialize a file called readurls which will store the contents of files to be read
    with open("readurls.txt", "w") as f2:
        for item in head:
            f2.write(item)





if __name__ == "__main__":
    main()
