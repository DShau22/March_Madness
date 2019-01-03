from bs4 import BeautifulSoup
import requests

def get_season_data(url):
    req = requests.get(url)
    assert req.status_code == 200, "http request has status code: {0}".format(req.status_code)

    soup = BeautifulSoup(req, 'lxml')
