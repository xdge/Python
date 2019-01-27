# coding: utf-8

import urllib
from urllib import request
import json

base_url = "https://www.trulia.com/json/search/url/?url=https%3A%2F%2Fwww.trulia.com%2Fsold%2FNew_York%2CNY%2F"
headers = {
  'accept': '*/*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': 'tlftmusr=190125plva077tg1gi4ucppxdypsw376; fvstts=20190124; _ga=GA1.2.2041839923.1548385641; _gid=GA1.2.380426961.1548385641; s_fid=2C0DF1E63D3C9BA9-3E7F5D4F02C50720; G_ENABLED_IDPS=google; s_vi=[CS]v1|2E253EB8052A36AA-4000010500000784[CE]; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; __gads=ID=8f81f1349170d848:T=1548385759:S=ALNI_MbQifR3xeOogqQ49h5RqXY67hRWmg; PHPSESSID=2hsb04p1dfpujcg924krj4gdl7; csrft=l1m4mCCbQtnsXe1US05JhcMjDwVAlOb3uh4VgvxuIbs%3D; s_cc=true; G_AUTHUSER_H=0; fontsLoaded=1; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dsld; previousSearches=locQuery0%3DNew%2BYork%2C%2BNY%3BlocQuery1%3DNew%2BYork%2C%2BNY; tabc=%7B%221071%22%3A%22control%22%2C%221094%22%3A%22b%22%2C%221081%22%3A%22control%22%2C%221022%22%3A%22b%22%2C%221052%22%3A%22a%22%2C%221053%22%3A%22a%22%7D; _gat=1; search_parameter_set=%7B%22searchType%22%3A%22sold%22%2C%22location%22%3A%7B%22cities%22%3A%5B%7B%22city%22%3A%22New+York%22%2C%22state%22%3A%22NY%22%7D%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22lastSaleDate%22%2C%22ascending%22%3Afalse%7D%2C%22soldWithin%22%3A9%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A55%2C%22pg-pdp%22%3A11%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; SERVERID=webfe24|XE12c; trul_visitTimer=1548578745299_1548580461650; _px3=6922dcd6cf46e837669006e316774e515a9b76e5a23cf658c28aee171923037c:979HcQdIvDx4nexOhq75ITFbh9BilWkskxcobZzGJFlomAyECYecpi0mTw+vUf8Ygbmy0SPjHNq5YsDChOqHSg==:1000:jlds5XowUs44RM8i7p9SNd7/PVm4+kEa5lUQWjmbxUUTFZWrcQ7va699e8Plsn6IVk6kGVbb9GRw2bYptH801p3ta5XRVK+WbaSAM0wW5yTX0PgZPgyvpHIj1S7txUysQxPaV8tfqVfZ31ZYLXAsCy1ulgh/uQw1ko0wlsyN/Pc=; s_sq=truliacom%3D%2526c.%2526a.%2526activitymap.%2526page%253Dsold%25253Asrp%25253Ahybrid%2526link%253D2%2526region%253DresultsColumn%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dsold%25253Asrp%25253Ahybrid%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.trulia.com%25252Fsold%25252FNew_York%25252CNY%25252F2_p%25252F%2526ot%253DA',
  'refer': 'https://www.trulia.com/sold/New_York,NY/',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

url_tail = "_p%2f"
data_arr = []
for i in range(1,101):
  url = base_url + str(i) + url_tail
  req = request.Request(url = url, headers = headers)
  while True:
    try:
      response = urllib.request.urlopen(req)
    except Exception as e:
      pass
    else:
      break
  data_str = response.read().decode('utf-8')
  data_dict = json.loads(data_str)
  del data_dict['page']['version']
  del data_dict['page']['canonicalUrl']
  for index, item in enumerate(data_dict['page']['cards']):
    if('maloneId' in item.keys()) == True:
      del item['maloneId']
    if('shortPrice' in item.keys()) == True:
      del item['shortPrice']
    if('cardUrl' in item.keys()) == True:
      del item['cardUrl']
    if('savable' in item.keys()) == True:
      del item['savable']
    if('stateCode' in item.keys()) == True:
      del item['stateCode']
    if('highlightedTags' in item.keys()) == True:
      del item['highlightedTags']
    if('footer' in item.keys()) == True:
      del item['footer']
    if('photoUrl' in item.keys()) == True:
      del item['photoUrl']
    if('photoUrlForHdDpiDisplay' in item.keys()) == True:
      del item['photoUrlForHdDpiDisplay']
    if('photoCount' in item.keys()) == True:
      del item['photoCount']
    if('photos' in item.keys()) == True:
      del item['photos']
    if('photosForHdDpiDisplay' in item.keys()) == True:
      del item['photosForHdDpiDisplay']
    if('description' in item.keys()) == True:
      del item['description']
    if('streetViewPhotoUrl' in item.keys()) == True:
      del item['streetViewPhotoUrl']
    if('satellitePhotoUrl' in item.keys()) == True:
      del item['satellitePhotoUrl']
    data_arr.append(item)
  # filename = 'data' + str(i) + '.json'
  print(i)
fw = open('houseData_sold.json', 'w')
fw.write(json.dumps(data_arr, indent = 2, ensure_ascii=False))
fw.close()