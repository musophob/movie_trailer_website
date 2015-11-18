# built after reading http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
import requests

class Imdb():
  def __init__(self, imdb_id):
    self.url = 'http://www.imdb.com/title/' + imdb_id
    self.page = requests.get(self.url)
    self.tree = html.fromstring(self.page.content)
    self.rating = self.tree.xpath('//span[@itemprop="ratingValue"]/text()')

