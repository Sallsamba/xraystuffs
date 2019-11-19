import requests
from lxml import etree 

#a car is an object, with features, and those features once scraped, will be shown to the user
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
    elif article ==
       url_list =['https://www.autoplus.fr/ferrari/458/Pista-Spider/prix-neuf/']
    return url_list
    
#The main scraping function. It scrapes all the features of the car.
def extract_car(url_list):
    hearder = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }

    data_totale =[]
    for url in url_list:
        res = requests.get(url,headers=hearder)
        html = etree.HTML(res.text)
        items = html.xpath('//tr[@class="row--even"]|//tr[@class="row--odd"]')
        #|//tr[@class="row--dfp"]')
        #print(items)
        for  item in items:
            detail_list = []
            version = item.xpath('.//td[2]/a/text()')
            detail_list.append(version[0])
            energie = item.xpath('.//td[3]/text()')
            detail_list.append(energie[0])
            prix = item.xpath('.//td[8]/text()')
            prix[0]="".join(prix[0].split())
            detail_list.append(prix[0])
            print(detail_list)
            data_totale.append(detail_list)
            
def extract_telephone(url_list):

            

if __name__ == "__main__":
   extract_car(url('jeep'))