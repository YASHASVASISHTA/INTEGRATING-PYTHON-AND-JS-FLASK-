# scraper.py
import requests
from bs4 import BeautifulSoup
import random 
def scrape_hackathon_ideas():
    url = "https://www.boardinfinity.com/blog/top-10-prize-winning-hackathon-project-ideas-3/"  # Replace with the website URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        hackathon_ideas = []

        # Assuming hackathon ideas are present in specific HTML elements (e.g., <div> with class="idea")
        for idea_elem in soup.find_all('h3'):
            hackathon_ideas.append(idea_elem.text.strip())

        return random.choice(hackathon_ideas)
    else:
        return None

if __name__ == "__main__":
    ideas = scrape_hackathon_ideas()
    print(ideas)
    
