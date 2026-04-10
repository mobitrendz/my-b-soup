## My B Soup - A Beautiful Soup Learning Project
A step by step guide by Sreeraj Sreenivasan - 9 April 2026

### Create and run a new FastAPI project

- Create a python project using UV (Assuming UV is already installed)

```bash
uv init my-b-soup
cd my-b-soup
```

- Create python virtual environment

```bash
uv venv
```

- Activate virtual environment

```bash
source .venv/bin/activate
```

- To check the active virtual environment

```bash
which python
```

- Expected result

```bash
<your-dir-path>/my-b-soup/.venv/bin/python
```

- Add request dependency for web scraping

```bash
uv add requests
```

- Add Beautiful Soup dependency

```bash
uv add beautifulsoup4
```

- Modify main.py

```bash
import requests
from bs4 import BeautifulSoup

def main():
    print("Hello from my-b-soup!")

    postcode = input("Enter Postcode: ")

    url = f"https://auspost.com.au/postcode/{postcode}"
    html_text = requests.get(url).text
    
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # 1. Find the table by class name
    target_table = soup.find('table', class_='resultsList fn_tableResultsList fn_tablePostcodeList')
    
    # 2. Extract data from rows
    table_data = []
    if target_table:
        for row in target_table.find_all('tr'):
            # Find all columns (data cells or headers)
            columns = row.find_all('td', class_='second')
            # Strip text from each cell and add to list
            row_data = [col.get_text(strip=True) for col in columns]
            table_data.append(row_data)

    # Remove empty rows
    table_data = list(filter(None, table_data))  

    # Print the extracted table data
    for row1 in table_data:
        print(row1)

if __name__ == "__main__":
    main()
```

- Run the code and input Australian Postcode 

```bash
python main.py
```