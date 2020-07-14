import random
from paste_bin_app.models import PasteBinDB


def randURLGen(length):
    
    letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                  'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
                  'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
                  'T','U','V','W','X','Y','Z']
    flag = True
    
    while flag:
        
        set_of_url = set(get_all_url())
        
        flag = False
        URL = ''
    
        for i in range(length):
            URL = URL + random.choice(letterList)
        
        if URL in set_of_url:
            flag = True
    
    return URL
        

def get_all_url():
    
    all_entries = PasteBinDB.DBManager.all()
    
    list_of_urls = []
    
    for entry in all_entries.values():
        list_of_urls.append(entry['url'])
    
    return list_of_urls
