from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup


ID_APP = 'TimothyK-Liquidat-PRD-ceaa20421-4daa1eeb'


def getKeyWords():
    return input('Enter your keywords (ex: white piano):\n')

def findEbay( keywords ):
    api = finding(appid=ID_APP, config_file=None)
    api_request = {'keywords': keywords}

    response = api.execute('findCompletedItems', api_request)
    soup = BeautifulSoup(response.content, 'lxml')

    totalentries = int(soup.find('totalentries').text)
    items = soup.find_all('item')

    if len(items)==0:
        return 'unknown'

    #print(items[0].prettify() + '\n')

    return items[0].sellingstatus.currentprice.string

#print(findEbay('ec obee EB-STATE3LT-02 3 Lite Smart Thermostat Black'))
    
    # for item in items:
    #     cat = item.categoryname.string.lower()
    #     title = item.title.string.lower()
    #     price = int(round(float(item.currentprice.string)))
    #     url = item.viewitemurl.string.lower()
    #
    #     print('________')
    #     print('cat:\n' + cat + '\n')
    #     print('title:\n' + title + '\n')
    #     print('price:\n' + str(price) + '\n')
    #     print('url:\n' + url + '\n')
    #     input()
