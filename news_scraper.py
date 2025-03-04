import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.bbc.com/news"  # Example news site
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find headlines (BBC example)
        headlines = soup.select("h3")  # Change selector based on the website
        
        print("\nLatest News Headlines:")
        for idx, headline in enumerate(headlines[:10], start=1):
            print(f"{idx}. {headline.get_text(strip=True)}")

    else:
        print("Failed to retrieve news")

if __name__ == "__main__":
    scrape_news()
