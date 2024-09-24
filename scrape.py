import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content = []
    for paragraph in soup.find_all('p'):
        content.append(paragraph.get_text())

    return " ".join(content)

if __name__ == "__main__":
    url = 'https://xaviers.ac/'  # Replace with your college website URL
    college_data = scrape_website(url)
    
    with open('college_data.txt', 'w', encoding='utf-8') as file:
        file.write(college_data)
