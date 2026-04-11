🌍 World Countries Web Scraper
A lightweight Python utility designed to scrape global country data from a live educational landing page. This script identifies a specific data table, extracts its contents, and exports it into a structured CSV file.
🚀 Features
Live Data Extraction: Fetches real-time HTML from mobitrendz.github.io.
Error Handling: Includes status checks to ensure the webpage is accessible before parsing.
Clean Formatting: Automatically strips whitespace and cleans HTML tags for a "ready-to-use" dataset.
CSV Export: Saves results to sample_world_countries.csv with UTF-8 encoding.
🛠️ Prerequisites
Ensure you have Python 3.x installed. You will also need to install the following dependencies:
bash
pip install requests beautifulsoup4
Use code with caution.

📂 Project Structure
scraper.py: The main Python script containing the scraping logic.
sample_world_countries.csv: The output file generated after running the script.
📖 How It Works
Request: The script sends an HTTP request to the target URL using the requests library.
Parsing: BeautifulSoup parses the HTML tree to find the table with the specific ID countryTable.
Iteration: It loops through the <thead> for column headers and <tbody> for country details.
Storage: The csv module writes the accumulated list of lists into a local spreadsheet file.
🖥️ Usage
Simply run the script via your terminal:
bash
python scraper.py
Use code with caution.

🛡️ Disclaimer
This script is intended for educational purposes. Always check a website's robots.txt file and Terms of Service before scraping data in a production environment.
Would you like me to add a troubleshooting section to this README for common connection errors?


