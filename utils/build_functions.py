# Functions to build the hyperlink graphs
import requests
import wikipediaapi
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin

user_agent = "MSDS452/Assignment1 (https://example.com)"
wiki_wiki = wikipediaapi.Wikipedia(user_agent, 'en')

def get_clean_wikipedia_hyperlinks(page_title): 
    page = wiki_wiki.page(page_title)

    if not page.exists():
        print(f"Page '{page_title}' does not exist on {language} Wikipedia.")
        return []

    # Fetch the page content
    response = requests.get(page.fullurl)
    if response.status_code != 200:
        print(f"Failed to fetch Wikipedia page: {page.fullurl}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # List to store valid titles
    valid_titles = []

    # Find all paragraphs and tables (main content)
    content_sections = soup.find_all(['p', 'table'])

    for section in content_sections:
        # Find all links within the current section
        links = section.find_all('a', href=True)

        for link in links:
            href = link['href']

            # Construct the full link URL
            full_link = urljoin(page.fullurl, href)

            # Exclude links that contain '#'
            if '#' in full_link:
                continue

            # Exclude links that lie inside tables
            # if section.name == 'table':
            #     continue

            # Exclude tables when scraping links except for the main table (<table class="infobox vcard">)
            if section.name=='table':
                table_class = section.get('class')
                # keep the main infobox table
                if not table_class: 
                    continue
                if 'infobox' not in table_class:
                    continue
                
            # Exclude Help: links 
            if 'Help:' in full_link:
                continue
                
            # Eclude top level links:
            if full_link=="https://en.wikipedia.org/wiki/United_States_House_of_Representatives":
                continue
                
            if full_link=="https://en.wikipedia.org/wiki/United_States_Senate":
                continue
    
            # Extract the title from the href
            if href.startswith('/wiki/'):
                title = href[len('/wiki/'):]
                title = unquote(title).replace('_', ' ')
                valid_titles.append(title)

    return valid_titles

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