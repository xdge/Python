# coding: utf-8

import urllib
import bs4
from urllib import request
import json

url = "https://www.condo.com/Manhattan-NY/Condos-Townhomes/1?sort=featured,priority,score,newest"
headers = {''}
Headers = {
  'accept': '',
  'accept-language': '',
  'cookie': '',
  'refer': '',
  'user-agent': ''
}

req = request.Request(url = url, headers = Headers)
response = urllib.request.urlopen(req)

soup = bs4.BeautifulSoup(response, 'lxml')

data_list = soup.select('body > div.canvas.row-offcanvas.row-offcanvas-left.row-offcanvas-filter > dmain > section > section > div > div:nth-of-type(1) > section > section > div:nth-child(1) > div > div > div > div > div:nth-of-type(1) > div.block-card-propertylisting.grid-box > div > div ')

data_list = soup.select('.xsCol12Landscape.smlCol12.lrgCol8')
house_list = []

print(data_list)

for data in data_list:
  house = []
  try:
    item_district = data.select('div > div > div:nth-child(3) > a.tileLink.phm > div > div.cardFooter.man.ptn.pbs > div')
    item_adress = data.select('div > div > div:nth-child(3) > a.tileLink.phm > div > div.h6.typeWeightNormal.typeTruncate.typeLowlight.mvn')
    item_price = data.select('div > div > div:nth-child(3) > a:nth-child(1) > div.backgroundBasic > div > div:nth-child(1) > span')
    item_beds = data.select('div > div > div:nth-child(3) > a:nth-child(1) > div.backgroundBasic > div > div:nth-child(2) > ul > li:nth-child(1)')
    item_baths = data.select('div > div > div:nth-child(3) > a:nth-child(1) > div.backgroundBasic > div > div:nth-child(2) > ul > li:nth-child(2)')
    item_area = data.select('div > div > div:nth-child(3) > a:nth-child(1) > div.backgroundBasic > div > div:nth-child(2) > ul > li:nth-child(3)')
    # print(item_name)
    if len(item_district) > 0:
      item = item_district[0].get_text()
      print(item)
    if len(item_adress) > 0:
      item = item_adress[0].get_text()
      print(item)
    if len(item_price) > 0:
      item = item_price[0].get_text()
      print(item)
    if len(item_beds) > 0:
      item = item_beds[0].get_text()
      print(item)
    if len(item_baths) > 0:
      item = item_baths[0].get_text()
      print(item)
    if len(item_area) > 0:
      item = item_area[0].get_text()
      print(item)
    print('') 
  except Exception as e:
    print(e)

    
