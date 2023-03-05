import discord
import sneakit
import config
from discord.ext import commands
from config import TOKEN

sneakit_product = sneakit.sneakit_url
sneakit_sizes = sneakit.sneakit_sizes
sneakit_product_img = sneakit.sneakit_image
sneakit_product_title = sneakit.sneakit_title
sneakit_product_url = sneakit.sneakit_product_url
stockx_url = sneakit.stockx_url
restocks_url = sneakit.restocks_url
hypeboost_url = sneakit.product_url

if not TOKEN:
    raise ValueError("The BOt-Token was not included in the config.py file")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (Sneakit)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.content.startswith(f'$sneakit'):
    await message.channel.send("Scraping!")

    if f'$sneakit' in message_content:
        SKU = message_content.replace('$sneakit ', '')
        sneakit_product_output = sneakit_product(SKU)
        sneakit_product_img_output = sneakit_product_img(SKU)
        sneakit_sizes_output = sneakit_sizes(SKU)
        sneakit_product_title_output = sneakit_product_title(SKU)
        stockx_url_output = stockx_url(SKU)
        restocks_url_output = restocks_url(SKU)
        hypeboost_url_output = hypeboost_url(SKU)
        sneakit_product_url_output = sneakit_product_url(SKU)

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
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]     ]({stockx_url_output})" f"[[Hypeboost]     ]({hypeboost_url_output})" f"[[Restocks]     ]({restocks_url_output})",
          inline=False
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )

        await message.channel.send(embed=embed)
        print('Scraping Successful!')


bot.run(TOKEN)
