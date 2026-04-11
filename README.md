# World Capital Cities Scraper

A Beautiful Soup learning project by Sreeraj Sreenivasan - Updated 11 April 2026

This project demonstrates web scraping using Python, requests, and BeautifulSoup4 to extract world capital cities data from an HTML table.

## Reference

- [World Capital Cities Table](https://geographyfieldwork.com/WorldCapitalCities.htm)

## Setup Instructions

### Prerequisites
- Python 3.x
- UV package manager (recommended)

### Create and Setup the Project

1. Create a new Python project using UV:

```bash
uv init beautiful-soup
cd beautiful-soup
```

2. Create a Python virtual environment:

```bash
uv venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Verify the active virtual environment:

```bash
which python
```

Expected result:
```bash
<your-dir-path>/beautiful-soup/.venv/bin/python
```

5. Add required dependencies:

```bash
uv add requests beautifulsoup4
```

## Usage

Run the scraper:

```bash
python main.py
```

The script will:
- Fetch HTML content from the World Capital Cities webpage
- Parse the HTML using BeautifulSoup
- Extract data from the sortable table containing capital cities information
- Print the extracted table rows to the console

## Code Overview

The main script (`main.py`) performs the following steps:

1. Imports necessary libraries (requests, BeautifulSoup)
2. Defines a `main()` function that:
   - Specifies the target URL
   - Fetches the HTML content
   - Parses the HTML
   - Finds the table with class 'sortable'
   - Extracts data from table rows
   - Filters out empty rows
   - Prints the results

## Dependencies

- `requests`: For making HTTP requests to fetch web content
- `beautifulsoup4`: For parsing and navigating HTML content