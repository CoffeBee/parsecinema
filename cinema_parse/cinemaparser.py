"""Parse subscity website"""
import requests as re
from bs4 import BeautifulSoup

class CinemaParser:
    """Class to parse subscity. It takes one parament - city"""
    def __init__(self, city='msk'):
        self.city = city
        self.raw_content = None

    def extract_raw_content(self) -> str:
        """Extract raw contest of main page and save it to self.raw_content"""
        self.raw_content = re.get('https://{}.subscity.ru'.format(self.city))
        if self.raw_content.status_code != 200:
            raise re.exceptions.RequestException('Something went wrong')

    def print_raw_content(self):
        """Print raw html of main page"""
        print(self.raw_content.text)

    def film_list(self):
        """Return list of films"""
        soup = BeautifulSoup(self.raw_content.text, "lxml")
        divs = soup.find_all("div", {"class": "movie-title"})
        return [i.text.replace('\xa0', '').replace('\xad', '') for i in divs]

    def nearest_session(self, name):
        soup = BeautifulSoup(self.raw_content.text, "lxml")
        href = soup.find_all("a", {"text": name})
        return href
