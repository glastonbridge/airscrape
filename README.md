# AirBnB Scraper

An exercise in scraping using BeautifulSoup

## Installation

Clone this repository. If you are using pipenv, you can run
```
pipenv install
pipenv run python scrape_exe.py
```

If you want to run bare python, ensure that you have the `bs4` (BeautifulSoup) and
`requests` libraries installed. This code was written in python 3.6.

## Usage

```
$ pipenv run python scrape_exe.py --help
usage: scrape_exe.py [-h] [--custom-host AIRBNBPATH] [--verbose] roomID

Scrape basic details for AirBnB properties.

positional arguments:
  roomID                the room ID you want details for

optional arguments:
  -h, --help            show this help message and exit
  --custom-host AIRBNBPATH
                        scrape somewhere other than https://airbnb.com/rooms/,
                        for testing purposes
  --verbose             print informative messages
  ```

For example, the file "scrape_requests.sh" contains the following code.
```
#!/bin/sh

echo "Room 14531512?s=51"
pipenv run python scrape_exe.py 14531512?s=51

echo "Room 19278160?s=51"
pipenv run python scrape_exe.py 19278160?s=51

echo "Room 19292873?s=51"
pipenv run python scrape_exe.py 19292873?s=51
```

## Code notes

For ease of reading, this script is split into three files.

 * `scrape_exe.py` - entry point for parsing url arguments and fetching the
                     raw html for the page. It then calls the other two files
 * `lib/strategy-redux.py` - the scraping strategy
 * `lib/roominfo.py` - the data object containing the results of the scrape,
                       as well as a pretty-print method for outputting the
                       data in a friendly way.
