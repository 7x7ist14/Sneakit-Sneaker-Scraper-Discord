import discord
import sneakit
import datetime
from discord.ext import commands
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX

sneakit_product = sneakit.sneakit_url
sneakit_sizes = sneakit.sneakit_sizes
sneakit_product_img = sneakit.sneakit_image
sneakit_product_title = sneakit.sneakit_title
sneakit_product_url = sneakit.sneakit_product_url
stockx_url = sneakit.stockx_url
restocks_url = sneakit.restocks_url
hypeboost_url = sneakit.product_url
goat_url = sneakit.product_goat

if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX:
    raise ValueError("The Command-Prefix was not included in the config.py file")

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (Sneakit)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX):
      await message.channel.send("Scraping...")

      if COMMAND_PREFIX in message_content:
          SKU_raw = message_content.replace(COMMAND_PREFIX, '')
          SKU = SKU_raw.replace(" ", "")
          sneakit_product_img_output = sneakit_product_img(SKU)
          sneakit_sizes_output = sneakit_sizes(SKU)
          sneakit_product_title_output = sneakit_product_title(SKU)
          stockx_url_output = stockx_url(SKU)
          restocks_url_output = restocks_url(SKU)
          hypeboost_url_output = hypeboost_url(SKU)
          sneakit_product_url_output = sneakit_product_url(SKU)
          goat_url_product_output = goat_url(SKU)

          embed = discord.Embed(
            title=sneakit_product_title_output,
            url=sneakit_product_url_output,
            color=0x607d8b
          )
          embed.set_author(
            name="Sneakit Scraper",
            url="https://twitter.com/jakobaio",
            icon_url= "https://consumersiteimages.trustpilot.net/business-units/630e4bd7744ce9c5e2e2fc4e-198x149-1x.jpg"
            )
          embed.set_thumbnail(
            url=sneakit_product_img_output
          )
          embed.add_field(
            name="Prices:",
            value=sneakit_sizes_output
          )
          embed.set_footer(
            text="Developed by Jakob.AIO"
          )
          embed.add_field(
            name="Open Product on:",
            value=f"[[StockX]]({stockx_url_output})      " f"[[Sneakit]]({sneakit_product_url_output})      " f"[[Restocks]]({restocks_url_output})      " f"[[Hypeboost]]({hypeboost_url_output})      " f"[[GOAT]]({goat_url_product_output})      ",
            inline=False
          )
          embed.set_footer(
            text=f"Developed by JakobAIO      |      Sneakit-Scraper      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
          )

          await message.channel.send(embed=embed)
          print('Scraping Successful!')

    else:
      await message.channel.send("***wrong command used!***")

bot.run(TOKEN)
