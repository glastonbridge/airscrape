import argparse
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import json

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

vprint("Response from server : {0}".format(room_request.status_code))

soup = BeautifulSoup(room_request.content, "html.parser")
redux_data = soup.find("script",attrs={"data-hypernova-key" : "spaspabundlejs"})
room_json_string = redux_data.string[redux_data.string.index("{"):redux_data.string.rindex("}")+1]

if len(room_json_string) > 200:
    vprint("Successfully got the redux content on this page")

room_json = json.loads(room_json_string)

redux_data = room_json['bootstrapData']['reduxData']
if not 'homePDP' in redux_data:
    print("This listing is no longer available")
else:
    listing_info = redux_data['homePDP']['listingInfo']['listing']
    print("= Property name")
    print("   - "+listing_info['name'])
    print()
    print("= Property type")
    print("   - "+listing_info['room_and_property_type'])
    print()
    print("= Number of bedrooms")
    print("   - {0} ({1} bedrooms)".format(listing_info['bedroom_label'],len(listing_info['listing_rooms'])))
    print()
    print("= Number of bathrooms")
    bathroom_label = listing_info['bathroom_label']
    print("   - {0} ({1} bathrooms)".format(bathroom_label,bathroom_label[:bathroom_label.find(" ")]))
    print()
    print("= Amenities")

    for amenity in listing_info['listing_amenities']:
        print("   - "+amenity['name'])
