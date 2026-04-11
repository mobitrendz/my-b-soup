## 🌍 World Countries Web Scraper

A lightweight Python utility designed to scrape global country data from a live educational landing page. This script identifies a specific data table, extracts its contents, and exports it into a structured CSV file.

### 🚀 Features

- **Live Data Extraction**: Fetches real-time HTML from mobitrendz.github.io.
- **Error Handling**: Includes status checks to ensure the webpage is accessible before parsing.
- **Clean Formatting**: Automatically strips whitespace and cleans HTML tags for a "ready-to-use" dataset.
- **CSV Export**: Saves results to sample_world_countries.csv with UTF-8 encoding.

### 🛠️ Prerequisites

Ensure you have Python 3.x installed. You will also need to install the following dependencies:

```bash
pip install requests beautifulsoup4
```

### 📂 Project Structure

- **scraper.py**: The main Python script containing the scraping logic.
- **sample_world_countries.csv**: The output file generated after running the script.

### 📖 How It Works

- **Request**: The script sends an HTTP request to the target URL using the requests library.
- **Parsing**: BeautifulSoup parses the HTML tree to find the table with the specific ID countryTable.
- **Iteration**: It loops through the <thead> for column headers and <tbody> for country details.
- **Storage**: The csv module writes the accumulated list of lists into a local spreadsheet file.

### 🖥️ Usage

Simply run the script via your terminal:

```bash
python scraper.py
```

### 🛠️ Troubleshooting

If you encounter issues while running the scraper, check the following common solutions:

| Issue | Potential Cause | Solution |
| :--- | :--- | :--- |
| **ModuleNotFoundError** | Libraries are not installed. | Run `pip install requests beautifulsoup4` in your terminal. |
| **403 Client Error** | The server is blocking the request. | The site may require a `User-Agent` header to prove you aren't a bot. |
| **ConnectionError** | No internet or URL typo. | Verify your connection and ensure the URL in the script is correct. |
| **Empty CSV File** | Table ID has changed. | Inspect the website to ensure the table still uses `id="countryTable"`. |
| **Permission Denied** | The CSV file is open in Excel. | Close `sample_world_countries.csv` before running the script again. |

### Adding a User-Agent (If Blocked)

If the website starts blocking your requests, update the requests.get() line in your scraper.py code to look like this:

```bash
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
```

### 🛡️ Disclaimer
This script is intended for **educational purposes**. Always check a website's robots.txt file and Terms of Service before scraping data in a production environment.