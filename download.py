import csv
import sys
import requests
from zipfile import ZipFile
import glob
import os
from os.path import join
import json

def download_file():
    print "Downloading Turn14 data loadsheet"
    data = json.load(open('turn14_creds.json'))
    username = data["username"]
    password = data["password"]
    s = requests.session()
    login_data = {'password':password, 'username':username}
    s.post('https://www.turn14.com/user/login', data=login_data)
    zipurl = 'https://www.turn14.com/export.php?action=inventory_feed'
    resp = s.get(zipurl)
    zname = 'inventory.zip'
    zfile = open(zname, 'wb')
    zfile.write(resp.content)
    zfile.close()
    unzip_file()

def unzip_file():
    print "Unzipping Turn14 data loadsheet"
    zip = ZipFile('inventory.zip')
    zip.extractall()

def remove_used():
    dir = "./"
    test = os.listdir(dir)
    for item in test:
        if item.endswith('.zip'):
            os.remove(join(dir,item))
        if item.endswith('.csv'):
            os.remove(join(dir,item))


download_file()
