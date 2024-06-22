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
| 6-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 7-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 8-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 9-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 10-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 11-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 12-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 13-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 14-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 15-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 16-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 17-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 18-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 19-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 20-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 21-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 22-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 23-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 24-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 25-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 26-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 27-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 28-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 29-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 30-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 31-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 32-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 33-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 34-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 35-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 36-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 37-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 38-strongly connected component |                      1 |                      0 | 

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
| 21-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 22-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 23-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 24-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 25-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 26-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 27-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 28-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 29-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 30-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 31-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 32-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 33-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 34-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 35-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 36-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 37-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 38-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 39-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 40-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 41-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 42-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 43-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 44-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 45-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 46-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 47-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 48-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 49-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 50-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 51-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 52-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 53-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 54-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 55-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 56-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 57-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 58-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 59-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 60-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 61-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 62-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 63-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 64-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 65-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 66-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 67-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 68-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 69-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 70-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 71-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 72-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 73-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 74-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 75-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 76-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 77-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 78-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 79-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 80-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 81-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 82-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 83-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 84-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 85-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 86-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 87-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 88-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 89-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 90-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 91-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 92-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 93-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 94-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 95-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 96-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 97-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 98-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 99-strongly connected component  |                      1 |                      0 |                                                                                                                     |
| 100-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 101-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 102-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 103-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 104-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 105-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 106-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 107-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 108-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 109-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 110-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 111-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 112-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 113-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 114-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 115-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 116-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 117-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 118-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 119-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 120-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 121-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 122-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 123-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 124-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 125-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 126-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 127-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 128-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 129-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 130-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 131-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 132-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 133-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 134-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 135-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 136-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 137-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 138-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 139-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 140-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 141-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 142-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 143-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 144-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 145-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 146-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 147-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 148-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 149-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 150-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 151-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 152-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 153-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 154-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 155-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 156-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 157-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 158-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 159-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 160-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 161-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 162-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 163-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 164-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 165-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 166-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 167-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 168-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 169-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 170-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 171-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 172-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 173-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 174-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 175-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 176-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 177-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 178-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 179-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 180-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 181-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 182-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 183-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 184-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 185-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 186-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 187-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 188-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 189-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 190-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 191-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 192-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 193-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 194-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 195-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 196-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 197-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 198-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 199-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 200-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 201-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 202-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 203-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 204-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 205-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 206-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 207-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 208-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 209-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 210-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 211-strongly connected component |                      1 |                      0 |                                                                                                                     |
| 212-strongly connected component |                      1 |                      0 |    


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
<--
| 15-connected component |                      2 |                      0 |                                                                                                                     |
| 16-connected component |                      2 |                      0 |                                                                                                                     |
| 17-connected component |                      2 |                      0 |                                                                                                                     |
| 18-connected component |                      2 |                      0 |                                                                                                                     |
| 19-connected component |                      2 |                      0 |                                                                                                                     |
| 20-connected component |                      2 |                      0 |                                                                                                                     |
| 21-connected component |                      2 |                      0 |                                                                                                                     |
| 22-connected component |                      2 |                      0 |                                                                                                                     |
| 23-connected component |                      2 |                      0 |                                                                                                                     |
| 24-connected component |                      2 |                      0 |                                                                                                                     |
| 25-connected component |                      2 |                      0 |                                                                                                                     |
| 26-connected component |                      2 |                      0 |                                                                                                                     |
| 27-connected component |                      2 |                      0 |                                                                                                                     |
| 28-connected component |                      2 |                      0 |                                                                                                                     |
| 29-connected component |                      2 |                      0 |                                                                                                                     |
| 30-connected component |                      2 |                      0 |                                                                                                                     |
| 31-connected component |                      2 |                      0 |                                                                                                                     |
| 32-connected component |                      2 |                      0 |                                                                                                                     |
| 33-connected component |                      2 |                      0 |                                                                                                                     |
| 34-connected component |                      2 |                      0 |                                                                                                                     |
| 35-connected component |                      2 |                      0 |                                                                                                                     |
| 36-connected component |                      2 |                      0 |                                                                                                                     |
| 37-connected component |                      2 |                      0 |                                                                                                                     |
| 38-connected component |                      2 |                      0 |                                                                                                                     |
| 39-connected component |                      2 |                      0 | 
-->
