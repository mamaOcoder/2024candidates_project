## 3. Connectivity

In graph theory, connectivity is a fundamental concept that describes how nodes are connected to one another within a graph (see [Wikipedia page on graph connectivity](https://en.wikipedia.org/wiki/Connectivity_(graph_theory))). There are different types of connectivity depending on whether the graph is directed or undirected, each providing insights into the graph's properties and behavior. Before describing the connectedness of the Senate and House hyperlink graphs, we define these concepts.

### 3.1. Connectivity in Undirected Graphs

In an undirected graph, edges have no direction, meaning the connection between any two nodes is bidirectional.

* **Connected Component**: A connected component in an undirected graph is a subgraph in which any two nodes are connected to each other by paths, and which is connected to no additional nodes in the supergraph.
* **Giant Connected Component**: The giant connected component is the largest connected subgraph that typically contains a substantial proportion of the entire undirected graph’s vertices and edges.

### 3.2. Connectivity in Directed Graphs

In directed graphs, edges have directions, indicating the relationship flows from one node to another. This gives rise to more nuanced concepts of connectivity: weak connectivity and strong connectivity.

* **Weakly Connected Component**: A weakly connected component is a subgraph where if the direction of edges is ignored, the subgraph is connected. This means that replacing all directed edges with undirected edges results in a connected component.
* **Giant Weakly Connected Component**: This is the largest weakly connected subgraph in the directed graph.
* **Strongly Connected Component**: A strongly connected component is a subgraph where for every pair of nodes ($u, v$) in the graph, there is a directed path from $u$ to $v$ and also another directed path from $v$ to $u$.
* **Giant Strongly Connected Component**: This is the largest strongly connected subgraph in the directed graph.

### 3.3. Connectivity of Candidate Hyperlink Graphs

In the tables below, the enumeration column corresponds to the decreasing order of sizes of the corresponding connected components. 
<!-- 
We observe that the weakly connected component subgraphs contain more candidates compared to the strongly connected component subgraphs in both the Senate and the House, which is consistent with their definitions.

### 3.4. Plots of Connected Components of Candidate Hyperlink Graphs 
-->

### 3.4.1 Senate 
                                                                                                         |
| Connected Component             |   Number of Candidates |   Number of Presidents | Presidents                                                                                                          |
|:--------------------------------|-----------------------:|-----------------------:|:--------------------------------------------------------------------------------------------------------------------|
| 0-weakly connected component    |                     68 |                      8 | Joe Biden, George H. W. Bush, George W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 0-strongly connected component  |                     23 |                      8 | Joe Biden, George H. W. Bush, George W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 1-strongly connected component  |                      3 |                      0 |                                                                                                                     |
| 2-strongly connected component  |                      3 |                      0 |                                                                                                                     |
| 3-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 4-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 5-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 33 remaining strongly connected component  |                      1 |                      0 |                                                                                                                     |


### 3.4.2 Reciprocated Senate

| Connected Component   |   Number of Candidates |   Number of Presidents | Presidents                                                                                                          |
|:----------------------|-----------------------:|-----------------------:|:--------------------------------------------------------------------------------------------------------------------|
| 0-connected component |                     12 |                      8 | Joe Biden, George H. W. Bush, George W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 1-connected component |                      9 |                      0 |                                                                                                                     |
| 2-connected component |                      3 |                      0 |                                                                                                                     |
| 3-connected component |                      3 |                      0 |                                                                                                                     |
| 4-connected component |                      2 |                      0 |                                                                                                                     |
| 5-connected component |                      2 |                      0 |                                                                                                                     |
| 6-connected component |                      2 |                      0 |                                                                                                                     |
| 7-connected component |                      2 |                      0 |  

### 3.4.3 House

| Connected Component              |   Number of Candidates |   Number of Presidents | Presidents                                                                                                          |
|:---------------------------------|-----------------------:|-----------------------:|:--------------------------------------------------------------------------------------------------------------------|
| 0-weakly connected component     |                    420 |                      8 | Joe Biden, George H. W. Bush, George W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 1-weakly connected component     |                      2 |                      0 |                                                                                                                     |
| 2-weakly connected component     |                      2 |                      0 |                                                                                                                     |
| 3-weakly connected component     |                      2 |                      0 |                                                                                                                     |
| 4-weakly connected component     |                      2 |                      0 |                                                                                                                     |
| 5-weakly connected component     |                      2 |                      0 |                                                                                                                     |
| 0-strongly connected component   |                    192 |                      8 | Joe Biden, George W. Bush, George H. W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 1-strongly connected component   |                      4 |                      0 |                                                                                                                     |
| 2-strongly connected component   |                      4 |                      0 |                                                                                                                     |
| 3-strongly connected component   |                      3 |                      0 |                                                                                                                     |
| 4-strongly connected component   |                      3 |                      0 |                                                                                                                     |
| 5-strongly connected component   |                      2 |                      0 |                                                                                                                     |
| 6-strongly connected component   |                      2 |                      0 |                                                                                                                     |
| 7-strongly connected component   |                      2 |                      0 |                                                                                                                     |
| 8-strongly connected component   |                      2 |                      0 |                                                                                                                     |
| 9-strongly connected component   |                      2 |                      0 |                                                                                                                     |
| 10-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 11-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 12-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 13-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 14-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 15-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 16-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 17-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 18-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 19-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 20-strongly connected component  |                      2 |                      0 |                                                                                                                     |
| 192 remaining strongly connected component  |                      1 |                      0 |                                                                                                                     |

### 3.4.4 Reciprocated House

| Connected Component    |   Number of Candidates |   Number of Presidents | Presidents                                                                                                          |
|:-----------------------|-----------------------:|-----------------------:|:--------------------------------------------------------------------------------------------------------------------|
| 0-connected component  |                     79 |                      8 | Joe Biden, George W. Bush, George H. W. Bush, Jimmy Carter, Bill Clinton, Barack Obama, Ronald Reagan, Donald Trump |
| 1-connected component  |                      7 |                      0 |                                                                                                                     |
| 2-connected component  |                      5 |                      0 |                                                                                                                     |
| 3-connected component  |                      4 |                      0 |                                                                                                                     |
| 4-connected component  |                      4 |                      0 |                                                                                                                     |
| 5-connected component  |                      4 |                      0 |                                                                                                                     |
| 6-connected component  |                      4 |                      0 |                                                                                                                     |
| 7-connected component  |                      4 |                      0 |                                                                                                                     |
| 8-connected component  |                      4 |                      0 |                                                                                                                     |
| 9-connected component  |                      3 |                      0 |                                                                                                                     |
| 10-connected component |                      3 |                      0 |                                                                                                                     |
| 11-connected component |                      3 |                      0 |                                                                                                                     |
| 12-connected component |                      3 |                      0 |                                                                                                                     |
| 13-connected component |                      3 |                      0 |                                                                                                                     |
| 26 remaining connected components |                      2 |                      0 |                                                                                                                     |


