from urllib.request import urlopen
from link_finder import LinkFinder
from general import *




class Apollo:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''         #the txt file     stored in  HARDDRIVE
    crawled_file = ''
    queue = set()                            # stored in RAM
    crawled = set()


    def __init__(self, project_name, base_url, domain_name):

        Apollo.project_name = project_name
        Apollo.base_url = base_url
        Apollo.domain_name = domain_name
        Apollo.queue_file = Apollo.project_name + '/queue.txt'
        Apollo.crawled_file = Apollo.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('TheFirstCrawler', Apollo.base_url)


    @staticmethod
    def boot():
        create_directory(Apollo.project_name )
        create_files(Apollo.project_name, Apollo.base_url)
        Apollo.queue = file_to_set(Apollo.queue_file)
        Apollo.crawled = file_to_set(Apollo.crawled_file)


    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Apollo.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Apollo.queue)) + ' | Crawled  ' + str(len(Apollo.crawled)))
            Apollo.add_links_to_queue(Apollo.gather_links(page_url))
            Apollo.queue.remove(page_url)
            Apollo.crawled.add(page_url)
            Apollo.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Apollo.base_url, page_url)
            finder.feed(html_string)

        except Exception as e:


            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Apollo.queue) or (url in Apollo.crawled):
                continue
            if Apollo.domain_name not in url:
                continue
            Apollo.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Apollo.queue, Apollo.queue_file)
        set_to_file(Apollo.crawled, Apollo.crawled_file)



























