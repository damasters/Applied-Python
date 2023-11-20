# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Homework 09

import ssl
from urllib.parse import urljoin
import urllib.request
import os

from bs4 import BeautifulSoup as bs

#imported functions from files in directions
def retrieve_and_store_webpage(url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read().decode('utf-8'), 'html.parser')
    f = open(fn, 'w', encoding='utf-8')
    print(soup, file=f)
    f.close()


def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')


def relative_file_path_to_URL(relative_file_path):
    # expand relative to absolute
    absolute_file_path = os.path.abspath(relative_file_path)
    # prepend file:// on UNIX-style OSes like Mac and Linux and file:/// on Windows
    file_name_url = urljoin('file:', urllib.request.pathname2url(absolute_file_path))
    return file_name_url


def main():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # url = 'https://www.blackcatdc.com/schedule.html'                  #urls of websites, commented out after run once
    # url = 'https://hoytsherman.org/'

    # retrieve_and_store_webpage(url, ctx, 'blackcat_main.html')        #retrieve commented out after run once
    # retrieve_and_store_webpage(url, ctx, 'hoytsherman_main.html')

    relative_file_path = 'sites/blackcat_main.html'                     #establish file path for black cat
    file_name_url = relative_file_path_to_URL(relative_file_path)       #get the name of the url from the path

    relative_file_path2 = 'sites/hoytsherman_main.html'                 #establish file path for hoyt sherman
    file_name_url2 = relative_file_path_to_URL(relative_file_path2)     #get the name of the url from the path

    soup = load_webpage(file_name_url, ctx)                             #load webpage from local file
    show_wraps = soup.find_all('div', class_='show-details')            #found class "show details" via inspect tool
    print("Concerts coming up at Black Cat")
    for show in show_wraps:                     #for each show in "show-details" print the text associated w/ the tag
        print('\t' + show.h2.text)              #shows' date
        print('\t\t'+show.h1.text)              #shows' name
    soup2 = load_webpage(file_name_url2, ctx)                          #load second webpage from local file
    show_wraps2 = soup2.find_all('div', class_='event')                #find class 'event' in second webpage
    print()                                                            #space
    print("Upcoming concerts coming up at Hoyt Sherman Place")
    for show in show_wraps2:                    #for each show in 'event' print the date and the name of the show
        print('\t'+show.em.text)                #shows' date
        print('\t\t' + show.a.text)             #shows' name

if __name__ == '__main__':
    main()
