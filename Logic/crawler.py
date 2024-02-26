from requests import get
from bs4 import BeautifulSoup
from collections import deque
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock
import json


class IMDB_crawler:
    '''
    put your own user agent in the headers
    '''
    headers = {
        'User-Agent': None
    }
    top_250_URL = 'https://www.imdb.com/chart/top/'

    def __init__(self,crawling_threshold=1000):
        '''
        Initialize the crawler 

        Parameters
        ----------
        crawling_threshold: int 
            The number of pages to crawl
        '''
         # TODO
        pass

    def get_id_from_URL(self, URL):
        '''
        Get the id from the URL of the site. The id is what comes exactly after title.
        for example the id for the movie https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1 is tt0111161.

        Parameters
        ----------
        URL: str
            The URL of the site
        Returns
        ----------
        str
            The id of the site
        '''
         # TODO
        return URL.split('/')[4]

    def write_to_file_as_json(self):
        '''
        Save the crawled files into json
        '''
         # TODO
        pass

    def read_from_file_as_json(self):
        '''
        Read the crawled files from json
        '''
         # TODO
        pass

    
    def crawl(self,URL):
        '''
        Make a get request to the URL and return the response

        Parameters
        ----------
        URL: str
            The URL of the site
        Returns
        ----------
        requests.models.Response
            The response of the get request
        '''
         # TODO
        pass

    def extract_top_250(self):
        '''
        Extract the top 250 movies from the top 250 page and use them as seed for the crawler to start crawling.
        '''
         # TODO
        pass

    def get_imdb_instance(self):
         # TODO
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
    

    def start_crawling(self):
        '''
        Start crawling the movies until the crawling threshold is reached.
        '''
         # TODO
        pass

    def crawl_page_info(self, URL):
        '''
        Main Logic of the crawler. It crawls the page and extracts the information of the movie and then saves it.

        Parameters
        ----------
        URL: str
            The URL of the site
        '''
         # TODO
        pass

    def extract_movie_info(self,res,movie,URL):
        '''
        Extract the information of the movie from the response and save it in the movie instance.

        Parameters
        ----------
        res: requests.models.Response
            The response of the get request
        movie: dict
            The instance of the movie
        URL: str
            The URL of the site
        '''
         # TODO
        pass

    def get_summary_link(url):
        '''
        Get the link to the summary page of the movie
        Example:
        https://www.imdb.com/title/tt0111161/ is the page
        https://www.imdb.com/title/tt0111161/plotsummary is the summary page

        Parameters
        ----------
        url: str
            The URL of the site
        Returns
        ----------
        str
            The URL of the summary page
        '''
         # TODO
        pass

    def get_review_link(url):
        '''
        Get the link to the review page of the movie
        Example:
        https://www.imdb.com/title/tt0111161/ is the page
        https://www.imdb.com/title/tt0111161/reviews is the review page
        '''
         # TODO
        pass

    def get_title(soup):
        '''
        Get the title of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The title of the movie
        
        '''
         # TODO
        pass

    def get_first_page_summary(soup):
        '''
        Get the first page summary of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The first page summary of the movie
        ''' 
        # TODO
        pass

    def get_director(soup):
        '''
        Get the directors of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The directors of the movie
        '''
         # TODO
        pass

    def get_stars(soup):
        '''
        Get the stars of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The stars of the movie
        '''
         # TODO
        pass

    def get_writers(soup):
        '''
        Get the writers of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The writers of the movie
        '''
         # TODO
        pass

    def get_related_links(soup):
        '''
        Get the related links of the movie from the More like this section of the page from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The related links of the movie
        '''
         # TODO
        pass

    def get_summary(soup):
        '''
        Get the summary of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The summary of the movie
        '''
         # TODO
        pass

    def get_synposis(soup):
        '''
        Get the synposis of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The synposis of the movie
        '''
         # TODO
        pass

    def get_reviews_with_scores(soup):
        '''
        Get the reviews of the movie from the soup
        reviews structure: [[review,score]]

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[List[str]]
            The reviews of the movie
        '''
         # TODO
        pass
    
    def get_genres(soup):
        '''
        Get the genres of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The genres of the movie
        '''
         # TODO
        pass
    
    def get_rating(soup):
        '''
        Get the rating of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The rating of the movie
        '''
         # TODO
        pass
    
    def get_mpaa(soup):
        '''
        Get the MPAA of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The MPAA of the movie
        '''
         # TODO
        pass
    
    def get_release_year(soup):
        '''
        Get the release year of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The release year of the movie
        '''
         # TODO
        pass

    def get_languages(soup):
        '''
        Get the languages of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The languages of the movie
        '''
         # TODO
        pass

    def get_countries_of_origin(soup):
        '''
        Get the countries of origin of the movie from the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        List[str]
            The countries of origin of the movie
        '''
         # TODO
        pass

    def get_budget(soup):
        '''
        Get the budget of the movie from box office section of the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The budget of the movie
        '''
         # TODO
        pass
    
    def get_gross_worldwide(soup):
        '''
        Get the gross worldwide of the movie from box office section of the soup

        Parameters
        ----------
        soup: BeautifulSoup
            The soup of the page
        Returns
        ----------
        str
            The gross worldwide of the movie
        '''
         # TODO
        pass

def main():
    imdb_crawler = IMDB_crawler(crawling_threshold=600)
    # imdb_crawler.read_from_file_as_json()
    imdb_crawler.start_crawling()
    imdb_crawler.write_to_file_as_json()

if __name__ == '__main__':
    main()
