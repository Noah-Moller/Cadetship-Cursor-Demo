# Web Scraper for Product Prices

## Overview
Build a Python web scraper that extracts product information from e-commerce websites and saves the data to a CSV file.

## Requirements

### Core Functionality
- Scrape product name, price, and availability from provided URLs
- Handle multiple product URLs in a single run
- Save results to CSV file with timestamp
- Include error handling for network issues and missing elements

### Technical Requirements
- Use requests library for HTTP requests
- Use BeautifulSoup for HTML parsing
- Implement proper delays between requests (1-2 seconds)
- Add User-Agent header to avoid blocking
- Log all activities and errors

### Input/Output
- Input: List of product URLs in a text file
- Output: CSV file with columns: url, product_name, price, availability, scraped_at

### Error Handling
- Skip URLs that return 404 or other HTTP errors
- Handle missing product information gracefully
- Log errors but continue processing remaining URLs
- Create empty CSV if no products are successfully scraped

### Code Structure
- Main scraper class with configurable delays and headers
- Separate method for parsing individual product pages
- CSV writing utility with proper escaping
- Command-line interface to specify input file and output location

## Usage Example
```
python scraper.py --input urls.txt --output products.csv --delay 2
```

## Expected Output Format
```csv
url,product_name,price,availability,scraped_at
https://example.com/product1,Widget A,29.99,In Stock,2024-01-15 10:30:00
https://example.com/product2,Widget B,,Out of Stock,2024-01-15 10:30:02
``` 