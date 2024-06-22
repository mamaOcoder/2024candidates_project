## 2. Graphs

The creation of hyperlink graphs is a crucial step in analyzing the relationships and connections among the Wikipedia pages of candidates for the 2024 U.S. Senate and House of Representatives elections. By mapping out the hyperlinks between the Wikipedia pages of the candidates, we can analyze the interconnectedness and network structure of the political landscape.

### 2.1. Obtaining Edge Values

To begin, the validated Wikipedia pages for each candidate were used as the basis for constructing the corresponding hyperlink graph (Senate or House). Each Wikipedia page in both dataframes was inspected to extract hyperlinks pointing to other Wikipedia pages. These hyperlinks represent adjacencies between different candidates in the wikisphere. To fetch these hyperlinks, we utilized the Python wrapper [wikipediaapi](https://github.com/martin-majlis/Wikipedia-API) to secure the existence of each candidate’s Wikipedia page and compile a list of hyperlinks. In the main fetching process, we parsed the HTML content with the Python library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) through a function (called get_clean_wikipedia_hyperlinks) searching for anchor tags (<a>) with valid href attributes inside the content of the parsed Wikipedia page. However, we have excluded certain hyperlinks outside the main contents of the candidates' wikipedia pages (such as those within non-infobox tables, help links, and specific top-level links). These excluded hyperlinks are added by Wikipedia (not by authors of candidates' Wikipedia pages) in order to provide comprehensive lists of all candidates competing for the same office and at the same State with that candidate. The reasoning for excluding such extended lists of candidates' hyperlinks was clear. Not only were these links separate from the primary content candidates presented about themselves, but including them would also lead to a highly interconnected hyperlink graph (almost complete).

With this method, we created two dictionaries: one to store all the clean hyperlinks found on each candidate's page and another to store hyperlinks from a candidate's page that point to other candidates' pages. Iterating on the items of the latter dictionary, we constructed the edges of the corresponding hyperlink graphs (for Senate and House candidates).

### 2.2. Building the Graphs

For this purpose, we were using the Python library [NetworkX](https://networkx.org/), which is designed for the creation, manipulation, and study of complex networks. Both the Senate candidate’s graph (Gs) and the House candidate’s graph (Gh) were initiated as a NetworkX digraph (directed graph). Each candidate was represented by his/her Wikipedia page as a node in their respective graph, and the hyperlinks between their Wikipedia pages (nodes) were represented as edges connecting these nodes.

* **Nodes**: Each candidate with a validated Wikipedia page was added as a node in the graph. Additional attributes such as party affiliation, office, incumbency status, and state were assigned to each node to provide context and facilitate further analysis (as we are going to discribe in one of the next sections).
* **Edges**: Hyperlinks extracted from the Wikipedia pages were used to create directed edges between nodes. These edges indicate a hyperlink from one candidate's Wikipedia page to another, capturing the nature of their interconnectedness.
  
### 2.3 Elementary Graph Statistics and Graph Plots

The created graphs were visualized using the interactive (javascript-based) Python library [Holoviews](https://www.holoviews.org/). Different visual attributes were used to enhance the clarity and interpretability of the graphs. Nodes were sized by their degree. For each graph, we were compiling the following basic graph statistics:

* **Order**: number of nodes.
* **Seize**: number of edges.
* **Density**: ratio of the number of edges to the number of possible edges if every node were connected to every other node.
* **Average degree**: ratio of the sum of degrees of all nodes to the total number of nodes.
* **Transitivity**: fraction of all possible triangles present in the graph.
* **Reciprocity**: ratio of the number of edges pointing in both directions to the total number of edges.
* **Number of connected components**: defined in the next section.

### 2.3.1 The graph of Senate candidates (including Presidents)

<p align="center">
  <img src="plots/SenateGraph1.png" alt="Senate candidates hyperlink graph">
  <br>
  <b>Figure 1</b>: Senate candidates hyperlink graph (<a href="https://mamaocoder.github.io/2024candidates_project/plots/SenateGraph1.html">interactive graph</a>).
</p>

Compare the graph statistics of the Senate graph, which includes the eight Presidents, with those of the Senate graph excluding the Presidents:

| Senate graph statistic                  |   With Presidents |   Without presidents |
|:----------------------------------------|------------------:|---------------------:|
| Order                                   |            68     |               46     |
| Size                                    |           246     |               77     |
| Density                                 |             0.054 |                0.037 |
| Average degree                          |             3.618 |                1.674 |
| Transitivity                            |             0.555 |                0.22  |
| Reciprocity                             |             0.358 |                0.494 |
| Number of weakly connected components   |             1     |                5     |
| Number of strongly connected components |            39     |               26     |

### 2.3.2 The graph of reciprocated Senate candidates (including Presidents)

<p align="center">
  <img src="plots/RecSenateGraph1.png" alt="Reciprocated Senate candidates hyperlink graph">
  <br>
  <b>Figure 2</b>: Reciprocated Senate candidates hyperlink graph (<a href="https://mamaocoder.github.io/2024candidates_project/plots/RecSenateGraph1.html">interactive graph</a>).
</p>

Compare the graph statistics of the reciprocated Senate graph, which includes the eight Presidents, with those of the reciprocated Senate graph excluding the Presidents:

| Reciprocated Senate graph statistic   |   With Presidents |   Without presidents |
|:--------------------------------------|------------------:|---------------------:|
| Order                                 |            35     |               26     |
| Size                                  |            44     |               19     |
| Density                               |             0.074 |                0.058 |
| Average degree                        |             1.257 |                0.731 |
| Transitivity                          |             0.565 |                0     |
| Number of connected components        |             8     |                8     |
| Average clustering coefficient        |             0.159 |                0     |

### 2.3.3 The graph of House candidates (including Presidents)

<p align="center">
  <img src="plots/HouseGraph1.png" alt="House candidates hyperlink graph">
  <br>
  <b>Figure 3</b>: House candidates hyperlink graph (<a href="https://mamaocoder.github.io/2024candidates_project/plots/HouseGraph1.html">interactive graph</a>).
</p>

In Figure 3, nodes are not labeled with candidates' names due to the graph's size, which would make name annotations difficult to read. To view node labels, one must refer to the corresponding <a href="https://mamaocoder.github.io/2024candidates_project/plots/HouseGraph1.html">interactive graph</a>.

Compare the graph statistics of the House graph, which includes the eight Presidents, with those of the House graph excluding the Presidents:

| House graph statistic                   |   With Presidents |   Without presidents |
|:----------------------------------------|------------------:|---------------------:|
| Order                                   |           430     |              361     |
| Size                                    |          1619     |              930     |
| Density                                 |             0.009 |                0.007 |
| Average degree                          |             3.765 |                2.576 |
| Transitivity                            |             0.343 |                0.221 |
| Reciprocity                             |             0.248 |                0.376 |
| Number of weakly connected components   |             6     |               20     |
| Number of strongly connected components |           213     |              173     |

### 2.3.4 The graph of reciprocated House candidates (including Presidents)

<p align="center">
  <img src="plots/RecHouseGraph1.png" alt="Reciprocated House candidates hyperlink graph">
  <br>
  <b>Figure 4</b>: Reciprocated House candidates hyperlink graph (<a href="https://mamaocoder.github.io/2024candidates_project/plots/RecHouseGraph1.html">interactive graph</a>).
</p>

Compare the graph statistics of the reciprocated House graph, which includes the eight Presidents, with those of the reciprocated House graph excluding the Presidents:

| Reciprocated House graph statistic   |   With Presidents |   Without presidents |
|:-------------------------------------|------------------:|---------------------:|
| Order                                |           182     |              173     |
| Size                                 |           201     |              175     |
| Density                              |             0.012 |                0.012 |
| Average degree                       |             1.104 |                1.012 |
| Transitivity                         |             0.386 |                0.32  |
| Number of connected components       |            40     |               40     |
| Average clustering coefficient       |             0.179 |                0.157 |

