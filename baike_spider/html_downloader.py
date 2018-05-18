import string
import urllib.request
from urllib.parse import quote


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        s = quote(url,safe=string.printable)
        response = urllib.request.urlopen(s)
        if response.getcode() != 200:
            return None

        return response.read()
