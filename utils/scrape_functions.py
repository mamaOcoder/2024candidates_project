# All functions used in collect_candidates.py
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


def node_sizes_scaling(G,a=0,b=1,mode='lin'): # c=10,
    if mode=='lin':
        ns = [a + b*G.in_degree(node) for node in G.nodes()] 
    if mode=='log':
        ns = [a + b*np.log(G.in_degree(node)) if G.in_degree(node) > 0 else a for node in G.nodes()]

    return ns

def hv_plot_graph(G, node_sizes, arrowhead_length, plot_size, pos=None, nodelabels=1, node_color="green",bundled=None,
                  partition=None, partition_colors=None, edge_color='gray',edge_line_width=1,
                  title=None, fontsize=None,
                  xoffset=0, yoffset=0, text_font_size=None, text_color=None, bgcolor="white"):
    if pos is None:
        pos = nx.spring_layout(G)
    
    pos_df = pd.DataFrame.from_dict(pos, orient='index', columns=['x', 'y'])
    pos_df['index'] = pos_df.index
    
    if partition is not None:
        node_colors = [partition_colors[partition[node]] for node in G.nodes()]
    else:
        node_colors = node_color
    
    plot = hvnx.draw(G, pos=pos, node_size=node_sizes, node_color=node_colors,
                     edge_color=edge_color, edge_line_width=edge_line_width)

    plot.opts(width=plot_size[0], height=plot_size[1], arrowhead_length=arrowhead_length, bgcolor=bgcolor)
    
    if title is not None:
        plot = plot.opts(title=title, fontsize=fontsize.get('title', '9pt'))
            
    if bundled == 0:
        if nodelabels == 1:
            labels = hv.Labels(pos_df, ['x', 'y'], 'index')
            plot = plot * labels.opts(xoffset=xoffset, yoffset=yoffset,
                                      text_font_size=text_font_size, text_color=text_color,
                                      fontsize=fontsize, bgcolor=bgcolor)
            return plot
        else:
            return plot
        
    if bundled == 1:
        plot = bundle_graph(plot)
        if nodelabels==1:
            labels = hv.Labels(pos_df, ['x', 'y'], 'index')
            plot = plot * labels.opts(xoffset=xoffset, yoffset=yoffset,
                                      text_font_size=text_font_size, text_color=text_color,
                                      fontsize=fontsize, bgcolor=bgcolor)
            return plot
        else:
            return plot

def graph_attributes(G,nodedatalist,edgedatalist):
    # nodedatalist/edgedatalist is a list of tuples with first element a dictionary and second element the attribute name
    if nodedatalist!=None:
        for (d,s) in nodedatalist:
            for n in G.nodes():
                G.nodes[n][s] = d[n]
    if edgedatalist!=None:
        for (d,s) in edgedatalist:
            for e in G.edges():
                G.edges[e][s] = d[e]

def html_to_text_with_hyperlinks(html_file_path):
    # Read the HTML file with a different encoding
    with open(html_file_path, 'r', encoding='ISO-8859-1') as file:
        html_content = file.read()

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text content
    text_content = soup.get_text(separator='\n', strip=True)

    # Extract hyperlinks and their corresponding text
    hyperlinks = [(link.text.strip(), link.get('href')) for link in soup.find_all('a')]

    # Concatenate text content with hyperlinks
    for link_text, link_url in hyperlinks:
        text_content += f'\n{link_text}: {link_url}'

    return text_content


def extract_urls(text):
    # Define the regex pattern to match URLs
    url_pattern = r'https?://\S+'

    # Find all matches of the pattern in the text
    urls = re.findall(url_pattern, text)

    return urls