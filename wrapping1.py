import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store data
quotes_data = []

# Extract quotes and authors
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quotes_data.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(quotes_data)

# Save to CSV
df.to_csv("quotes.csv", index=False)

print("Data scraped successfully!")
print(df.head())

output:
    Data scraped successfully!

Quote                                    Author
"The world as we have created it..."     Albert Einstein
"It is our choices..."                   J.K. Rowling
"There are only two ways..."             Albert Einstein
