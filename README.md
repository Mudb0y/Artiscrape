# Artiscrape

This tool aims to scrape all fics from the Artemis Fowl fandom from fanfiction.net, and possibly AO3.

$ pip install fanficfare requests bs4

After the dependencies are installed, simply run the script.

$ mkdir artiscrape-content&&cd artiscrape-content&&python ./artiscrape.py

## Important note!

This scrapes story IDs from around 1 to 15000000 on fanfiction.net, which is close to the total volume of fics.

This might take months (if not years) to complete, so don't judge me if your mum wants you to reboot your PC but you can't because you're currently downloading fanfiction. From personal experience, I can assure you, your mum won't listen.

Best advice I can give you is use a VPS (Digital Ocean / Linode / OCI if you want something good for free), make sure it runs Linux (because who would run a Windows server), and run the script there using screen or another session manager.

## Give me fancy GUI because I'm not a cmdline nerd!

The answer is no. If you're a data horder / archivist, you probably already know what you're doing anyways, and this tool is simple enough to the point where literally only the most basic commandline knowledge is required.

If you know Python and wish to make a GUI, feel free to, I won't stop you.