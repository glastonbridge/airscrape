import argparse
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import json
import lib.strategyredux as strategyredux
from lib.scrapeerror import *

parser = argparse.ArgumentParser(description='Scrape basic details for AirBnB properties.')
parser.add_argument('roomID',
                    help='the room ID you want details for')
parser.add_argument('--custom-host', dest="airbnbpath", default="https://airbnb.com/rooms/",
                    help='scrape somewhere other than https://airbnb.com/rooms/, for testing purposes')
parser.add_argument('--verbose',action="store_true",
                    help='print informative messages')

args = parser.parse_args()

def vprint(s):
    if args.verbose:
        print(s)

scrape_url = urljoin(args.airbnbpath,args.roomID)

vprint("Scraping "+scrape_url)

room_request = requests.get(scrape_url)

if room_request.status_code!=200:
    print ("Could not retrieve the URL: "+scrape_url)
    exit()

try:
    room_data = strategyredux.apply_strategy(room_request.content)
except NoListingError:
    print("Could not retrieve listing, it may have been removed")
    exit()
except ScrapeError:
    print("Fatal error, the page structure does not match any known scrape strategy")
    exit()

vprint("Successfully got the redux content on this page")

room_data.prettyprint()
