# Import dependencies.
import os
import requests
import beautifulsoup4 as bs

# Send a request to fanfiction.net/s/1 through fanfiction.net/s/15000000. If one of the pages contains the string "Artemis Fowl fanfic" in the title of the page continue.
for i in range(1, 15000000):
    url = "https://www.fanfiction.net/s/" +i
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, "html.parser")
title = soup.find("h1", {"class": "title"})
if title.text.find("Artemis Fowl fanfic") != -1:
    # Download the fic using fanficfare.
    print ("Downloading " +title " from " +url " ...")