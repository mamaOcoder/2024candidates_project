# <p align="center">2024 Senate and House of Representatives Candidates' Wikipedia Hyperlink Graphs Analysis</p>

## <p align="center">By Leslie Stovall, Mingming Gu, and Moses Boudourides</p>

**Notice**: This project is an elaboration of the final project by the first two authors in the Spring 2024 *Northwestern University MSDS 452 class* under the supervision of the third author. **It is an ongoing research effort, and the contents will be continuously updated throughout the summer of 2024 until the draft of the manuscript for the paper is completed. Please check back regularly for the latest updates and additional network statistical computations.**

## Summary
This study investigates the network characteristics and community structures of the 2024 U.S. Senate and House candidates based on their Wikipedia pages, utilizing graph theory and network analysis techniques. By constructing and analyzing directed hyperlink graphs, we examined the connectivity, assortativity, centrality indices and community partitions among candidates, focusing on attributes such as incumbency, party affiliation, state, and candidacy status. Our findings reveal distinct patterns of connectivity and reciprocity within the Senate and House candidate networks. In particular, we identify the presence of tightly-knit communities and significant variations in candidate connectivity across different states and political affiliations. Through visualizations including Sankey diagrams and adjacency matrix heatmaps, we provide a comprehensive overview of the underlying structures and attribute distributions within these political candidate networks. This analysis contributes to a deeper understanding of the digital presence and interconnectivity of political figures, offering insights into the dynamics of online political representation.

## Table of Contents
1. [Data Collection](docs/1_Hyperlinks.md)
2. [Graphs](docs/2_Graphs.md)
3. [Connectivity](docs/3_Connectivity.md)
4. [Attributes and Assortativity](docs/4_Attributes_and_Assortativity.md)
   - Gender and Race of Candidates
6. [Centralities](docs/5_Centralities.md)
7. [Communities](docs/6_communities.md)
8. Regression Analysis of Homophily and Heterophily
9. Node Classification by:
    - Support Vector Machines (SVMs)
    - Graph Convolutional Networks (GCNs)

## Files
- Jupyter notebooks (will be uploaded once they are formatted for public sharing)
<!--
- collect_candidates.ipynb contains the code for scraping and cleaning the data from Ballotpedia and Wikipedia. The 4 pickle files are the most updated results from running this code.
- Final Project Notebook.ipynb contains the code for generating the graphs and performing network analyses.
- utils/scrape_functions.py contains the functions created for collect_candidates.ipynb.
- utils/graphs_functions.py contains the functions created for Final Project Notebook.ipynb.
-->
- [Class project report PDF](https://github.com/mamaOcoder/2024candidates_project/blob/main/MSDS452_Final_Project.pdf)

<!-- 
## Interactive Visualizations
You can view our interactive visualizations here:
- [Interactive Visualizations](https://mamaocoder.github.io/2024candidates_project/)
-->

## Contact
For any questions or further information, please contact Moses Boudourides at Moses.Boudourides@gmail.com.
