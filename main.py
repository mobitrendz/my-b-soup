"""
This script scrapes the world capital cities table from a website using BeautifulSoup and requests.
It extracts data from an HTML table and prints the rows.
"""

import requests
from bs4 import BeautifulSoup

def main():
    """
    Main function to scrape and print the capital cities table.
    
    Fetches HTML from the specified URL, parses it, finds the sortable table,
    extracts data from table rows, filters out empty rows, and prints the data.
    """
    
    # URL of the webpage containing the capital cities table
    url = "https://geographyfieldwork.com/WorldCapitalCities.htm"
    
    # Fetch the HTML content from the URL
    html_text = requests.get(url).text
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # 1. Find the table by class name
    target_table = soup.find('table', class_='sortable')

    # Uncomment the next line to print the entire table HTML for debugging
    # print(target_table)
    
    # 2. Extract data from rows
    table_data = []
    if target_table:
        for row in target_table.find_all('tr'):
            # Find all columns (data cells or headers)
            columns = row.find_all('td')
            # Strip text from each cell and add to list
            row_data = [col.get_text(strip=True) for col in columns]
            table_data.append(row_data)

    # Remove empty rows
    table_data = list(filter(None, table_data))  

    # Print the extracted table data
    for row1 in table_data:
        print(row1)

# This ensures that main() runs only when this script is executed directly, not when imported as a module
if __name__ == "__main__":
    main()