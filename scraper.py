import requests
from bs4 import BeautifulSoup
import csv

def scrape_countries_to_csv():
    # URL of the practice page
    url = "https://mobitrendz.github.io/beautiful-soup/"
    filename = "sample_world_countries.csv"
    
    try:
        # 1. Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # 2. Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. Locate the table by its ID 
        table = soup.find('table', id='countryTable')
        
        if not table:
            print("Error: Could not find the table with ID 'countryTable'.")
            return

        # 4. Extract data from the table
        scraped_data = []
        
        # Get Header row
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        scraped_data.append(headers)
        
        # Get Body rows
        tbody = table.find('tbody')
        if not tbody:
            print("Error: Could not find <tbody> in the table.")
            return
        
        rows = tbody.find_all('tr')
        for row in rows:
            # Extract text from each cell (td)
            cells = [td.get_text(strip=True) for td in row.find_all('td')]
            scraped_data.append(cells)
            
        # 5. Save the data to a CSV file
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(scraped_data)
            
        print(f"✅ Successfully scraped {len(scraped_data) - 1} country details and saved to {filename}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    scrape_countries_to_csv()
