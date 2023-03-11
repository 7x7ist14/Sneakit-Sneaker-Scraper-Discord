# Sneakit-Sneaker-Scraper-Discord
A Scraper for all prices and sizes of Sneakers on Sneakit
The scraper will return a message in your Discord chanel with a list of all sizes and prices + the product url for Sneakit, Restocks, StockX and Hypeboost.


# Requirements:
1. Check if you have all the needed Python libraries.

+ requests (pip install requests)
+ json (pip install json)
+ BeautifulSoup (pip install beautifulsoup4)
+ Discord (pip install discord.py)

--> to install them just write the pip install... command in your Terminal.


# How to use

1. Open the "Config" file and input your Discord Bot Token and the name of the channel where you want to use the scraper in.

2. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)

3. Write the keyword ($sneakit) + SKU in your discord server.
   format: $sneakit SKU --> (example: $sneakit CW1590-100)
   --> you can also change the command and the prefix in the config file if you want to.


The Scraper will now send you all listed sizes and their prices in the discord channel.
Also the Sneakit product URL is in the blue title.
At the bottom of the discord message you can also find the StockX, Sneakit, GOAT, Hypeboost and Restocks Product URL to the Scraped Product.

# Return Message Example:
The return message looks like this:

![image](https://user-images.githubusercontent.com/103487648/224495962-bd130f4c-3427-4e55-9022-8a0c317d4cd6.png)


![image](https://user-images.githubusercontent.com/103487648/224495997-3544498c-9e55-4b8c-9dfb-321f879c1b6c.png)

