#  Jumia Body Wash Scraper

A simple automation & web scraping project that extracts body wash products from [Jumia Kenya](https://www.jumia.co.ke/).

##  What it Does
- Uses Selenium to scrape product names, prices, brands, and URLs.
- Exports the results to a CSV file.
- Attempts to handle dynamic loading (pagination still under improvement).

## Challenges
- Jumia loads data dynamically using JavaScript, making scraping tricky.
- Only able to scrape ~30 items out of 2500+ — pagination & loading issues.
- Looking for better ways to handle this (Selenium waits, scrolls, or possibly using APIs).

##  Open to Collaboration!
If you’ve worked with complex dynamic sites or have ideas to solve pagination, feel free to contribute or message me. Would love to learn more together.

## Built With
- Python 
- Selenium
- ChromeDriver
