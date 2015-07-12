#VERSION: 1.03
#AUTHORS: MrNeon

from novaprinter import prettyPrinter
from helpers import retrieve_url, download_file
import json


class strikesearch(object):
    url = 'https://getstrike.net/'
    name = 'Strike Search'
    supported_categories = {'all': '', 'movies': 'Movies', 'tv': 'TV', 'anime': 'Anime', 'books': 'Books',
                            'music': 'Music', 'games': 'Games', 'software': 'Applications'}

    def __init__(self):
        pass

    def download_torrent(self, info):
        print(download_file(info))

    def search(self, what, cat='all'):
        json_data = retrieve_url("".join((self.url, 'api/v2/torrents/search/?phrase=', what,
                                          '&category=', self.supported_categories.get(cat, ''))))
        json_dict = json.loads(json_data)

        if json_dict['results'] < 1:
            return

        for r in json_dict['torrents']:
            r_dict = {'link': r['magnet_uri'],
                      'name': r['torrent_title'],
                      'size': str(r['size']) + 'B',
                      'seeds': r['seeds'],
                      'leech': r['leeches'],
                      'desc_link': r['page'],
                      'engine_url': self.url}
            prettyPrinter(r_dict)
