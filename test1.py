import requests
from bs4 import BeautifulSoup

def crawl_page(url):
    # Send a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Process the parsed HTML and extract the desired information
        # (This will depend on the structure of the webpage you're crawling)
        
        # Example: print all the text inside paragraph tags
        with open('output.txt', 'wb') as f:
            f.write(soup.find(class_ = 'content2').encode('utf-8'))
    else:
        print(f"Failed to fetch the page: {url}")

# Example usage: crawl a specific URL
crawl_page('https://edfjzxt.xmu.edu.cn/website/page/Information/xxgk.html')