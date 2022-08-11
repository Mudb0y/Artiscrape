# Import dependencies.
import os
from time import sleep
import requests
import bs4 as bs

for i in range(1, 40882393):
    url = "https://archiveofourown.org/works/" + str(i)
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, "html.parser")
    if soup.title.text == "Artemis Fowl - Eoin Colfer":
        with open("valid-urls.txt", "a") as f:
            f.write(url + "\n")
        print ("Valid URL found.")
    else:
        pass
    sleep(1)