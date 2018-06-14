from bs4 import BeautifulSoup
import json
from .roominfo import RoomInfo
from .scrapeerror import *

def apply_strategy(scrapedfile):
    """We know that there is a readable copy of the redux store backing the
    page. It's in json and it's nice to parse."""
    try:
        soup = BeautifulSoup(scrapedfile, "html.parser")
        redux_data = soup.find("script",attrs={"data-hypernova-key" : "spaspabundlejs"})
        room_json_string = redux_data.string[redux_data.string.index("{"):redux_data.string.rindex("}")+1]

        room_json = json.loads(room_json_string)

        redux_data = room_json['bootstrapData']['reduxData']
    except Exception:
        raise FormatError

    if not 'homePDP' in redux_data:
        raise NoListingError

    listing_info = redux_data['homePDP']['listingInfo']['listing']

    result = RoomInfo()
    result.property_name = listing_info['name']
    result.property_type = listing_info['room_and_property_type']
    result.bedroom_label = listing_info['bedroom_label']
    result.bedroom_count = len(listing_info['listing_rooms'])
    result.bathroom_label = listing_info['bathroom_label']
    result.bathroom_count = result.bathroom_label[:result.bathroom_label.find(" ")]
    for amenity in listing_info['listing_amenities']:
        result.amenities.append(amenity['name'])
    return result
