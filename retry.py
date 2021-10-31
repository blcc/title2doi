# pip install habanero
from habanero import Crossref
import re

def titletodoi(keyword):
    cr = Crossref()
    result = cr.works(query=keyword)
    items = result['message']['items']
    item_title = items[0]['title']
    tmp = ''
    for it in item_title:
        tmp += it
    title = keyword.replace(' ', '').lower()
    title = re.sub(r'\W', '', title)
    # print('title: ' + title)
    tmp = tmp.replace(' ', '').lower()
    tmp = re.sub(r'\W', '', tmp)
    # print('tmp: ' + tmp)
    if (title == tmp):
        doi=items[0]['DOI']
        return doi
    else:
        return None
        
print(f'doi={titletodoi("Increased Mars rover autonomy using AI planning, scheduling and execution")}')
