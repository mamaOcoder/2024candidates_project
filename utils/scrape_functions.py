# Functions to scrape and clean Candidate data
import requests, re
import pandas as pd
import numpy as np
import networkx as nx
from bs4 import BeautifulSoup

import holoviews as hv
import hvplot.networkx as hvnx
from holoviews.operation.datashader import bundle_graph


def scrape_ballotpedia_tables(url):
    """
    Scrape a table from a Ballotpedia page and return it as a DataFrame.

    Args:
    - url (str): The URL of the Ballotpedia page containing the table.

    Returns:
    - list: The scraped html tables as a list.
    """
    # Send an HTTP request to the URL and get the page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table')

    return tables

def get_ballotpedia_table(tables, table_order):
    """
    Scrape a table from a Ballotpedia page and return it as a DataFrame.

    Args:
    - tables (list): List of Ballotpedia page html tables.
    - table_order (int): Index of the table that we want 

    Returns:
    - pd.DataFrame: The scraped table as a DataFrame.
    """
    # Check if the specified table order exists
    if table_order >= len(tables):
        raise IndexError("Specified table order does not exist on the page")

    # Extract the specified table
    table = tables[table_order]

    # Convert the table HTML to a DataFrame
    df = pd.read_html(str(table))[0]

    return df

def check_wikipedia_page(name):
    # Function to check if a Wikipedia page exists for a given name
    url = f"https://en.wikipedia.org/wiki/{name.replace(' ','_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return name
    else:
        return None #"wiki page not found"

def scrape_wikipedia_tables(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    return tables

# Function looks for wiki in href tag
def href_wiki(href):
    return href and re.compile("^/wiki/").search(href)
    
def scrape_wikipedia_table(url, table_order):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all tables on the page
        tables = soup.find_all('table')
        
        # Check if the specified table order is within the range of available tables
        if table_order < len(tables):
            # Convert the HTML table to a Pandas DataFrame
            df = pd.read_html(str(tables[table_order]))[0]
            return df
        else:
            print("Table order is out of range.")
            return None
    else:
        print("Failed to retrieve page:", url)
        return None
    
def find_state_name(s):
    # List of US state names
    us_states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
        'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
        'West Virginia', 'Wisconsin', 'Wyoming',
        'District of Columbia','Samoa','Guam','Mariana Islands','Virgin Islands'
    ]
    
    # Regular expression pattern to match state names
    pattern = r'\b(?:' + '|'.join(us_states) + r')\b'
    
    # Search for state name in the string
    match = re.search(pattern, s, flags=re.IGNORECASE)
    
    if match:
        return match.group(0)
    else:
        return None
