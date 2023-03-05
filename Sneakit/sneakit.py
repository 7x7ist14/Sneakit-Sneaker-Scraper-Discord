import requests
import json
from bs4 import BeautifulSoup

def sneakit_url(SKU):
  produkt_code = SKU
  global url
  url = f"https://sneakit.com/search/products/{produkt_code}?query={produkt_code}&page=1"
  print("Scraped Sneakit URL!", url)
  return url

def sneakit_product_url(SKU):
  raw = sneakit_info(SKU)
  slug = raw['data'][0]['slug']
  p_url = "https://sneakit.com/product/" + slug
  print("Scraped Sneakit Product URL:" + p_url)
  return p_url


def sneakit_info(SKU):
  sneakit_url_r = sneakit_url(SKU)
  r = requests.get(sneakit_url_r)
  global output
  output = json.loads(r.text)
  print("Scraped Sneakit info!")
  return output

def sneakit_sizes(SKU):
  raw = sneakit_info(SKU)
  sizes = raw['data'][0]['product_variants_with_shop_price']
  result = []
  for entry in sizes:
    result.append({'size': entry['size'], 'shop_price_in_eur': entry['shop_price_in_eur']})
  result = sorted(result, key=lambda x: x['size'])
  output_str = ''
  for entry in sorted(result, key=lambda x: x['size']):
    output_str += f"{entry['size']}: {entry['shop_price_in_eur']}€\n"
  print("Scraped Sneakit Prices & Sizes!")
  return output_str

def sneakit_image(SKU):
  raw = sneakit_info(SKU)
  image = raw['data'][0]['productable']['preview_img_public_url']
  #print(image)
  print("Scraped Image!")
  return image

def sneakit_title(SKU):
  raw = sneakit_info(SKU)
  title = raw['data'][0]['name']
  print("Scraped Sneakit Title!")
  return title

def stockx_url(SKU):
  url = "https://stockx.com/api/browse?_search=" + SKU

  headers = {
          'accept': 'application/json',
          'accept-encoding': 'utf-8',
          'accept-language': 'en-DE',
          'app-platform': 'Iron',
          'referer': 'https://stockx.com/en-DE',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'
      }

  request1 = requests.get(url=url, headers=headers)

  product_id = json.loads(request1.text)
  product_id_final = product_id['Products'][0]['id']

  ID = product_id_final
  url_stockX = "https://stockx.com/" + ID
  print("Scraped StockX URL: " + url_stockX)
  return url_stockX

def restocks_url(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)
  return product_url

def product_url(SKU):
  url = "https://hypeboost.com/en/search/shop?keyword=" + SKU

  headers = {
      "cookie": "country=eyJpdiI6ImlCRDJaRExPQkZYNTNlMmM0OWFEQVE9PSIsInZhbHVlIjoiTFRaRW01UW5wNUY2RjZnQzViWGlPYWRtYVRmbmxxMXpoRjNzODlZZUdIZmNLWjZSTFp0Q3htbTFuYUF4ZGkwVSIsIm1hYyI6IjQ0MzBlZTdkZmNhYjVhYmJhMDAzNDhlNjQ3MGU5NzQ1YThkOTk0ZDRkNzYxZGQzYzg0ODI0ZWYzZWZhODBlZGYiLCJ0YWciOiIifQ%253D%253D; currency=eyJpdiI6ImFlbkxaNHJyOHdUZlJFRlJ2dGlna0E9PSIsInZhbHVlIjoieEx2OE01VHhzOGZ1eFdsM09IVDFIZmR6R1hieHpDRDZScWoweVhqTDZjUzY2a3FFUmhQZGdPV2piaFN3OTViTCIsIm1hYyI6IjgzMTY0NDExNzljYjM1MzFmZmM5ZTBhOGY0MjU3ZWViMjA2NjBjYmUwMjg0MDFkMmUyYmJiNTVjYTUxZTk5MjMiLCJ0YWciOiIifQ%253D%253D",
      "Content-Type": "application/json"
  }

  response = requests.request("GET", url, headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  for a in soup.find_all('a', href=True):
    print('Scraped product url!')
    return a['href']