import requests
import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(module)s:%(message)s')

def download(url):
    ext = url[-3:]
    r = requests.get(url)
    if r.ok and ext == ('pdf' or 'doc' or 'xls'):
        with open(f'file.{ext}','wb') as f:
            f.write(r.content)
        return 'Success'

    else:
        raise TypeError('Unwanted File')

url = input("Enter url")
logging.debug(download(url))
