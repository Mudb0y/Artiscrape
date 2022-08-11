# Import dependencies.
import os
from time import sleep
import requests
import bs4 as bs

print ("Building list of valid links. This will take a long time...")
for i in range(1, 40882393):
    url = "https://archiveofourown.org/works/" + str(i)
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, "html.parser")
    if soup.title.text == "Artemis Fowl - Eoin Colfer":
        with open("valid-urls.txt", "a") as f:
            f.write(url + "\n")
        print ("Valid URL found.")
    else:
        with open("invalid-urls.txt", "a") as f:
            f.write(url + "\n")
    sleep(1)