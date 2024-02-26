from requests import get
from bs4 import BeautifulSoup
from collections import deque
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock
import json


class IMDB_crawler:
    # put your own User agent
    headers = {
        'User-Agent': None
    }
    top_250_URL = 'https://www.imdb.com/chart/top/'

    # Initialize the crawler with crawling_threshold being the number of pages to crawl
    def __init__(self,crawling_threshold=1000):
        pass

    # get id from URL of site. The id is what comes exactly after title
    # for example the id for the movie https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1 is tt0111161
    def get_id_from_URL(self, URL):
        return URL.split('/')[4]

    # save your crawled files into json
    def write_to_file_as_json(self):
        pass

    # load your crawled files from json
    def read_from_file_as_json(self):
        pass

    # make a get request to a url
    def crawl(self,URL):
        pass

    # extract the id's of top 250 pages 
    def extract_top_250(self):
        pass

    def get_imdb_instance(self):
        return {
            'id': None, # str
            'title': None, # str
            'first_page_summary': None, # str
            'release_year': None, # str
            'mpaa': None, # str
            'budget': None, # str
            'gross_worldwide': None, # str
            'rating': None, # str
            'directors': None, # List[str]
            'writers': None, # List[str]
            'stars': None, # List[str]
            'related_links': None, # List[str]
            'genres': None, # List[str]
            'languages': None, # List[str]
            'countries_of_origin': None, # List[str]
            'summaries': None, # List[str]
            'synposis': None, # List[str]
            'reviews': None, # List[List[str]]
        }
    

    # crawl all the pages until crawling threshold is reached
    def start_crawling(self):
        pass

    # Crawl and extract the movie info
    def crawl_page_info(self, URL):
        pass

    # Extract movie info and save it
    def extract_movie_info(self,res,movie,URL):
        pass

    # Get the link to summary page of movie for example the summary page of movie
    # https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1 is the page
    # https://www.imdb.com/title/tt0111161/plotsummary/?ref_=tt_stry_pl
    def get_summary_link(url):
        pass

    # Get the link to summary page of movie for example the summary page of movie
    # https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1 is the page
    # https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv
    def get_review_link(url):
        return '/'.join(url.split('/')[:-1]) + '/reviews/'

    def get_title(soup):
        pass

    def get_first_page_summary(soup):
        pass

    def get_director(soup):
        pass

    def get_stars(soup):
        pass

    def get_writers(soup):
        pass

    def get_related_links(soup):
        pass

    def get_summary(soup):
        pass

    def get_synposis(soup):
        pass

    def get_reviews_with_scores(soup):
        pass
    
    def get_genres(soup):
        pass
    
    def get_rating(soup):
        pass
    
    def get_mpaa(soup):
        pass
    
    def get_release_year(soup):
        pass

    def get_languages(soup):
        pass

    def get_countries_of_origin(soup):
        pass

    def get_budget(soup):
        pass
    
    def get_gross_worldwide(soup):
        pass

def main():
    imdb_crawler = IMDB_crawler(crawling_threshold=600)
    # imdb_crawler.read_from_file_as_json()
    imdb_crawler.start_crawling()
    imdb_crawler.write_to_file_as_json()

if __name__ == '__main__':
    main()
