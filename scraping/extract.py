import requests
from lxml import etree 
from bs4 import BeautifulSoup

class car:
    def __init__(self,name,version,energie,boite_de_vitesse,prix):
        self.name =name
        self.version=version
        self.energie=energie
        self.boite_de_vitesse=boite_de_vitesse
        self.prix=prix
        
#url is a mapping function which redirects to a website with needed informations
def url(article):
    if article == 'renault clio':
       url_list = ['https://www.autoplus.fr/renault/clio/-/prix-neuf/?year-min=2019'] 
    elif article == 'jeep':
       url_list = ['https://www.autoplus.fr/jeep/wrangler/prix-neuf/']
    elif article == 'ferrari':
       url_list =['https://www.autoplus.fr/ferrari/458/Pista-Spider/prix-neuf/']
    elif article == 'huawei':
       url_list = ['https://www.idealo.fr/prix/6467183/huawei-p30-pro.html']
    elif article == 'iphone 6':
       url_list=['https://www.idealo.fr/prix/2567982/apple-iphone-6.html']
    elif article == 'iphone 11 pro':
       url_list = ['https://www.idealo.fr/prix/6719907/apple-iphone-11-pro.html']
    else :
       url_list =['https://www.ikea.com/fr/fr/cat/canapes-cuir-et-tissu-enduit-10662/']
    return url_list
    
#The main scraping function. It scrapes all the features of the car.
def extract_car(url_list):
    hearder = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }

    detail_list = []
    for url in url_list:
        res = requests.get(url,headers=hearder)
        html = etree.HTML(res.text)
        items = html.xpath('//tr[@class="row--even"][1]')
        #|//tr[@class="row--dfp"]')
        #print(items)
       
        for  item in items:
            
            version = item.xpath('.//td[2]/a/text()')
            detail_list.append(version[0])
            energie = item.xpath('.//td[3]/text()')
            detail_list.append(energie[0])
            prix = item.xpath('.//td[8]/text()')
            prix[0]="".join(prix[0].split())
            detail_list.append(prix[0])
            
    return detail_list      

def extract_telephone(url_list):
    telephone_totale =[]
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    detail_list = []
    for url in url_list:
        res = requests.get(url,headers = header)
        html = BeautifulSoup(res.text,'html.parser')
        items = html.find('li',class_='productOffers-listItem row row-24 row-24-mobile')
        
        #items = html.xpath('//li[@class="productOffers-listItem row row-24 row-24-mobile"]')
        
        #for item in items:
            
        name = items.find('span').text.strip()
        name = name.replace('\u00AD','')
        name = name[:-6]
        detail_list.append(name)
        prix = items.find('a',class_='productOffers-listItemOfferPrice').text.strip()
        prix="".join(prix.split())
        detail_list.append(prix)
        
    return detail_list
            


def extract_canape(url_list):
    canape_totale =[]
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    detail_list = []
    for url in url_list:
        res = requests.get(url,headers = header)
        html = BeautifulSoup(res.text,'html.parser')
        item = html.find('div',class_='product-compact__spacer')
        
        
        #items = html.xpath('//li[@class="productOffers-listItem row row-24 row-24-mobile"]')
        
        
        name = item.find('span',class_='product-compact__name').text.strip()
        detail_list.append(name)
        type_ = item.find('span',class_='product-compact__type').text.strip()
        detail_list.append(type_)
        prix = item.find('span',class_='product-compact__price').text.strip()
        detail_list.append(prix)
        
    return detail_list
        
def main(article):
    if article == 'renault clio' or 'jeep' or 'ferrari':
       print(extract_car(url(article)))
    elif article == 'huawei' or 'iphone 6' or 'ihpne 11 pro':
       print(extract_telephone(url(article)))
    else :
       print(extract_canape(url(article)))

main('jeep')
