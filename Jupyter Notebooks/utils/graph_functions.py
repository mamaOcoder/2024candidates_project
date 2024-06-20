# Functions used in Final Project Notebook
import math
import pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.colors as mcolors, networkx as nx, scipy as sp
from collections import defaultdict, Counter
from networkx.drawing.nx_agraph import graphviz_layout
from cdlib import algorithms

import holoviews as hv
import hvplot.networkx as hvnx
from holoviews.operation.datashader import bundle_graph

def node_sizes_scaling(G,a=0,b=1,mode='lin'): # c=10,
    if mode=='lin':
        ns = [a + b*G.degree(node) for node in G.nodes()] 
    if mode=='log':
        ns = [a + b*np.log(G.degree(node)) if G.degree(node) > 0 else a for node in G.nodes()]

    return ns

def edge_width_sizes_scaling(edgeweight_d,A=0,B=1,mode='lin'):
    if mode=='lin':
        modified_edgeweight_d={k:A+B*v for k,v in edgeweight_d.items()}
    if mode=='log':
        modified_edgeweight_d={k:A+B*np.log(v) for k,v in edgeweight_d.items()}
    return modified_edgeweight_d

# def hv_plot_graph(G, node_sizes, arrowhead_length, plot_size, pos=None, nodelabels=1, node_color="green",bundled=None,
#                   partition=None, partition_colors=None, edge_color='gray',edge_line_width=1,
#                   title=None, fontsize=None,
#                   xoffset=0, yoffset=0, text_font_size=None, text_color=None, bgcolor="white"):
#     if pos is None:
#         pos = nx.spring_layout(G)
    
#     pos_df = pd.DataFrame.from_dict(pos, orient='index', columns=['x', 'y'])
#     pos_df['index'] = pos_df.index
    
#     if partition is not None:
#         node_colors = [partition_colors[partition[node]] for node in G.nodes()]
#     else:
#         node_colors = node_color
    
#     plot = hvnx.draw(G, pos=pos, node_size=node_sizes, node_color=node_colors,
#                      edge_color=edge_color, edge_line_width=edge_line_width)

#     plot.opts(width=plot_size[0], height=plot_size[1], arrowhead_length=arrowhead_length, bgcolor=bgcolor)
    
#     if title is not None:
#         plot = plot.opts(title=title, fontsize=fontsize.get('title', '9pt'))
            
#     if bundled == 0:
#         if nodelabels == 1:
#             labels = hv.Labels(pos_df, ['x', 'y'], 'index')
#             plot = plot * labels.opts(xoffset=xoffset, yoffset=yoffset,
#                                       text_font_size=text_font_size, text_color=text_color,
#                                       fontsize=fontsize, bgcolor=bgcolor)
#             return plot
#         else:
#             return plot
        
#     if bundled == 1:
#         plot = bundle_graph(plot)
#         if nodelabels==1:
#             labels = hv.Labels(pos_df, ['x', 'y'], 'index')
#             plot = plot * labels.opts(xoffset=xoffset, yoffset=yoffset,
#                                       text_font_size=text_font_size, text_color=text_color,
#                                       fontsize=fontsize, bgcolor=bgcolor)
#             return plot
#         else:
#             return plot

def hv_plot_graph(G, node_sizes, arrowhead_length, plot_size, pos=None, nodelabels=1, 
                  node_color="green", node_cmap=None, bundled=None,
                  partition=None, partition_colors=None, edge_color=None,edge_line_width=1,
                  title=None, fontsize=None,
                  xoffset=0, yoffset=0, text_font_size=None, text_color=None, bgcolor="white",edge_cmap=None):
    if pos is None:
        pos = nx.spring_layout(G)
    
    pos_df = pd.DataFrame.from_dict(pos, orient='index', columns=['x', 'y'])
    pos_df['index'] = pos_df.index
    
    if partition is not None:
        node_colors = [partition_colors[partition[node]] for node in G.nodes()]
    else:
        node_colors = node_color

    nodes = hvnx.draw_networkx_nodes(G, pos=pos, node_size=node_sizes, node_color=node_colors, node_cmap=node_cmap)
    edges = hvnx.draw_networkx_edges(G, pos=pos, node_size=node_sizes, arrowstyle='->',
                                   edge_color=edge_color,
                                   edge_cmap=edge_cmap, edge_line_width=edge_line_width, colorbar=True)
    
    nodes.opts(width=plot_size[0], height=plot_size[1], bgcolor=bgcolor)
    edges.opts(width=plot_size[0], height=plot_size[1], arrowhead_length=arrowhead_length, bgcolor=bgcolor)
    
    if title is not None:
        nodes = nodes.opts(title=title, fontsize=fontsize.get('title', '9pt'))
        edgdes = edges.opts(title=title, fontsize=fontsize.get('title', '9pt'))
        
    plot = edges * nodes 
                    
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

def attribute_image_graph(G, node_attributes_d):
    # Create a defaultdict to store link counts between attribute values
    link_counts = defaultdict(int)
    
    # Iterate through the edges of G and count the links between attribute values
    for u, v in G.edges():
        attr_u = node_attributes_d[u]
        attr_v = node_attributes_d[v]
        link_counts[(attr_u, attr_v)] += 1
    
    # Create a new graph for the attribute image graph
    if nx.is_directed(G):
        attribute_image_G = nx.DiGraph()
    else:
        attribute_image_G = nx.Graph()
    
    # Add nodes for each unique attribute value
    for attr_value in set(node_attributes_d.values()):
        attribute_image_G.add_node(attr_value)
    
    # Add weighted edges based on link counts
    for (attr_u, attr_v), weight in link_counts.items():
        attribute_image_G.add_edge(attr_u, attr_v, weight=weight)
        
#     # Remove isolated nodes
#     isolates = list(nx.isolates(attribute_image_G))
#     attribute_image_G.remove_nodes_from(isolates)
    
    return attribute_image_G

def community_circle_layout(G, communities_d, community_centers, community_radii):
    # Initialize dictionary to store node positions
    pos = {}
    
    # Calculate the number of communities
    num_communities = len(community_centers)
    
    # Calculate the angle increment between community centers
    angle_increment = 2 * math.pi / num_communities
    
    # Iterate over all nodes in the graph
    for node in G.nodes():
        # Get the community ID of the current node
        community_id = communities_d[node]
        
        # Get the center and radius of the community
        center = community_centers[community_id]
        radius = community_radii[community_id]
        
        # Calculate the angle for the current node within its community circle
        community_nodes = [n for n, cid in communities_d.items() if cid == community_id]
        node_index = community_nodes.index(node)
        node_angle = node_index * (2 * math.pi / len(community_nodes))
        
        # Calculate the coordinates of the current node
        node_x = center[0] + radius * math.cos(node_angle)
        node_y = center[1] + radius * math.sin(node_angle)
        
        # Store the position of the current node
        pos[node] = (node_x, node_y)
    
    return pos

def community_separated_layout(G, communities_d, community_centers, community_radii):
    # Initialize dictionary to store node positions
    pos = {}

    # Iterate over all communities
    for community_id, center in enumerate(community_centers):
        # Get the radius of the community
        radius = community_radii[community_id]
        
        # Extract the subgraph for the current community
        community_nodes = [node for node, cid in communities_d.items() if cid == community_id]
        subgraph = G.subgraph(community_nodes)
        
        if len(community_nodes) == 1:
            # If there is only one node in the community, place it at the center
            pos[community_nodes[0]] = center
            continue
        
        # Get the positions using graphviz_layout
        subgraph_pos = nx.nx_agraph.graphviz_layout(subgraph, prog='neato')
        
        # Normalize the positions to fit inside the circle
        max_x = max(pos[0] for pos in subgraph_pos.values())
        min_x = min(pos[0] for pos in subgraph_pos.values())
        max_y = max(pos[1] for pos in subgraph_pos.values())
        min_y = min(pos[1] for pos in subgraph_pos.values())
        
        x_range = max_x - min_x
        y_range = max_y - min_y
        
        if x_range == 0 and y_range == 0:
            # If all positions are the same, place nodes in a small circle around the center
            for i, node in enumerate(community_nodes):
                angle = 2 * math.pi * i / len(community_nodes)
                pos[node] = (center[0] + radius * 0.1 * math.cos(angle), center[1] + radius * 0.1 * math.sin(angle))
        else:
            scale = 2 * radius / max(x_range, y_range)  # Scaling factor to fit inside the circle
            
            for node, (x, y) in subgraph_pos.items():
                # Scale and translate positions to fit in the circle
                new_x = center[0] + scale * (x - (min_x + x_range / 2))
                new_y = center[1] + scale * (y - (min_y + y_range / 2))
                pos[node] = (new_x, new_y)
    
    return pos

def circular_centers_radii(G,communities,R,a):  
    cc=[]
    num_communities = len(communities)
    angle_increment = 2 * np.pi / num_communities
    cc=[(R * np.cos(i * angle_increment), R * np.sin(i * angle_increment)) for i in range(num_communities)]
    cr=[]
    communities_d = {node: i for i, community in enumerate(communities) for node in community}
    for i in range(len(communities)):
        t=[]
        for k,v in communities_d.items():
            if v==i:
                t.append(k)
        cr.append(len(t)/a)
    return cc,cr

def check_graph(G):
    # Check for self-loops
    if any(G.has_edge(node, node) for node in G.nodes()):
        return False
    
    if nx.is_directed(G):
        # Check if the directed graph has no weights
        for u, v, data in G.edges(data=True):
            if 'weight' in data:
                return False
    else:
        # Check if the undirected graph has weights all equal to 1 or no weights
        for u, v, data in G.edges(data=True):
            if 'weight' in data and data['weight'] != 1:
                return False
    
    return True

def create_centralities_list(G,maxiter=2000,pphi=5,centList=[]):
    if len(centList)==0:
        centList=['degree','closeness','betweenness','eigenvector','Katz','PageRank','HITS','load','communicability','current flow']
    cenLen=len(centList)
    valus={}
    for uu,centr in enumerate(centList):
        if centr=='degree':
            if isinstance(G,nx.DiGraph):
                cent=nx.in_degree_centrality(G)
                sstt='In Degree Centralities '
                valus['in_degree']=cent
                cent=nx.out_degree_centrality(G)
                sstt+= 'and Out Degree Centralities'
                valus['out_degree']=cent
            else:
                cent=nx.degree_centrality(G)
                sstt='Degree Centralities'
                ssttt='degree centrality'
                valus[centr]=cent
        elif centr=='closeness':
            cent=nx.closeness_centrality(G)
            sstt='Closeness Centralities'
            ssttt='closeness centrality'
            valus[centr]=cent
        elif centr =='load':
            cent=nx.load_centrality(G)
            sstt='Load Centraities'
            valus[centr]=cent
        elif centr == 'communicability':
            if not isinstance(G, nx.DiGraph):
                cent=nx.communicability_betweenness_centrality(G)
                sstt='Communicability Centralities'
                valus[centr]=cent
        elif centr=='betweenness':
            cent=nx.betweenness_centrality(G)
            sstt='Betweenness Centralities'
            ssttt='betweenness centrality'
            valus[centr]=cent
#         elif centr=='current flow':
#             if not isinstance(G, nx.DiGraph):
            
#                 cent=nx.current_flow_closeness_centrality(G, solver='lu')
#                 sstt='Current Flow Closeness Centrality'
#                 valus[centr]=cent
        elif centr=='eigenvector':
            try:
                cent=nx.eigenvector_centrality(G,max_iter=maxiter)
                sstt='Eigenvector Centralities'
                ssttt='eigenvector centrality'
                valus[centr]=cent

            except:
                valus[centr]=None

                continue
        elif centr=='Katz':
            phi = (1+math.sqrt(pphi))/2.0 # largest eigenvalue of adj matrix
            cent=nx.katz_centrality_numpy(G,1/phi-0.01)
            cent=nx.katz_centrality_numpy(G,.05)#,1/phi-0.01)
            
            sstt='Katz Centralities'
            ssttt='Katz centrality'
            valus[centr]=cent
#             valus[centr+'_%i' %pphi]=cent

        elif centr=='PageRank':
            try:
                cent=nx.pagerank(G)
                sstt='PageRank'
                ssttt='pagerank'
                valus[centr]=cent

            except:
                valus[centr]=None

                continue
        elif centr=='HITS':
            if isinstance(G,nx.DiGraph):
                dd=nx.hits(G,max_iter=maxiter)
                sstt='HITS hubs '
                valus['HITS_hubs']=dd[0]
                sstt+= 'and HITS authorities'
                valus['HITS_auths']=dd[1]
            else:
                dd=nx.hits(G,max_iter=maxiter)
                cent=nx.degree_centrality(G)
                sstt='HITS'
                ssttt='HITS Centralities'
                valus[centr]=dd[0]
        else:
            continue
#         print('%s done!!!' %sstt)
    return valus

dindices=['out_degree','in_degree','closeness','betweenness','eigenvector','HITS_hubs','HITS_auths','Katz','PageRank','load']
indices=['degree','closeness','betweenness','eigenvector','HITS','Katz','PageRank','load','communicability'] #,'current flow'
# indices=['degree','closeness','betweenness','eigenvector']

# Without 'communicability' and 'current flow' (undirected case)
dindicesd=['out_degree','in_degree','closeness','betweenness','eigenvector','HITS_hubs','HITS_auths','Katz','PageRank','load']
indicesd=['degree','closeness','betweenness','eigenvector','HITS','Katz','PageRank','load']
# indicesd=['degree','closeness','betweenness','eigenvector']

dindicesdr=dindices
indicesdr=indices

# Plus 'node'
dindicesdrn=["node"]+dindices
indicesdrn=['node']+indices

def central_df(G,node,central_pd):
    central_pd[node]=central_pd.index.values
    if isinstance(G,nx.DiGraph):
        central_pd=central_pd[[node]+dindices]
    else:
        central_pd=central_pd[[node]+indices]
    central_pd[node]=central_pd.index.values
    central_pd.reset_index(drop = True, inplace = True)
    # central_pd=central_pd[['node']]
    central_pd.sort_values(node) #.head()
    # central_pd['node']=G.nodes()
    return central_pd
    
def communities_dictionaries(G,k=None):
    
    # The parameter k is needed to be set only for fluid communities
    
    container_d={}
    
    # Girvan-Newman
    gncp = nx.community.girvan_newman(G)
    top_level_communities = next(gncp)
    next_level_communities = next(gncp)
    gnc = sorted(sorted(map(sorted, next_level_communities)), key=len,reverse=True)
    ngnc = len(gnc)
    gncp_d = {n:i for i,c in enumerate(gnc) for n in c}
    container_d["Girvan-Newman communities"]=(gncp_d,ngnc)
    
    # Louvain
    lc = nx.community.louvain_communities(G, seed=123)
    lc = sorted(sorted(map(sorted, lc)), key=len,reverse=True)
    nlc = len(lc)
    lcp_d = {n:i for i,c in enumerate(lc) for n in c}
    container_d["Louvain communities"]=(lcp_d,nlc)
    
    # Leiden
    if nx.is_directed(G)==False:
        lec = algorithms.leiden(G)
        lec = lec.communities
        lec = sorted(sorted(map(sorted, lec)), key=len,reverse=True)
        nlec = len(lec)
        lecp_d={n:i for i,c in enumerate(lec) for n in c}
        container_d["Leiden communities"]=(lecp_d,nlec)
    else:
        pass
    
    # Label propagation
    if nx.is_directed(G)==False:
        lpc = nx.algorithms.community.label_propagation.label_propagation_communities(G)
        lpc = sorted(lpc, key=len, reverse=True)
        nlpc = len(lpc)
        lpc_d = {n:i for i,c in enumerate(lpc) for n in c}
        container_d["Label propagation communities"]=(lpc_d,nlpc)
    else:
        pass
    
    # Asynchronous label propagation
    alpc = nx.algorithms.community.label_propagation.asyn_lpa_communities(G)
    alpc = sorted(alpc, key=len, reverse=True)
    nalpc = len(alpc)
    alpc_d={n:i for i,c in enumerate(alpc) for n in c}
    container_d["Asynchronous label propagation communities"]=(alpc_d,nalpc)
    
    # Fluid communities
    if nx.is_directed(G)==False and check_graph(G) and nx.is_connected(G): 
        fcp=nx.algorithms.community.asyn_fluid.asyn_fluidc(G, k, max_iter=100, seed=None)
        fcp=sorted(fcp, key=len, reverse=True)
        nfcp=len(fcp)
        fcp_d={n:i for i,c in enumerate(fcp) for n in c}
        container_d["Fluid communities"]=(fcp_d,nfcp)
    else:
        pass
    
    return container_d

def calculate_gini(arr):
    # Flatten the array
    arr = np.array(arr).flatten()
    n = len(arr)
    if n == 0:
        return None
    sorted_arr = np.sort(arr)
    coefficients = np.arange(1, n + 1)
    gini_index = (np.sum((2 * coefficients - n - 1) * sorted_arr)) / (n * np.sum(sorted_arr))
    return gini_index # round(gini_index, 3)  # Round to 3 decimal points

def count_attributes(members, attr_dict):
    counts = Counter(attr_dict[n] for n in members if n in attr_dict)
    return dict(counts)
    
### In order to apply to 4 attributes, 
### Create a plot function
def plot_attribute_graph(G, attribute, color_palette):
    value_list = list(set(nx.get_node_attributes(G, attribute).values()))
    if attribute=="party":
        color_map = {'Republican': 'red', 'Democratic': 'blue', 'Independent': 'yellow', 'Green': 'green'}
    else:
        color_map = {val: color_palette[i % len(color_palette)] for i, val in enumerate(value_list)}
    node_colors = [color_map[G.nodes[node][attribute]] for node in G.nodes()]
    
    node_sizes = node_sizes_scaling(G, a=50, b=0, mode='lin')
    pos = graphviz_layout(G)
        
    title = f"Colored by {attribute}"
    
    plot = hv_plot_graph(
        G, node_sizes=node_sizes, arrowhead_length=0, plot_size=(400, 300), pos=pos, 
        nodelabels=0, node_color=node_colors, bundled=0, partition=None, 
        partition_colors=None, edge_color='lightsalmon', edge_line_width=1, 
        title=title, fontsize={'title': '12pt'}, xoffset=0, yoffset=-8, 
        text_font_size='9pt', text_color='midnightblue', bgcolor="white"
    )
    
    return plot

def count_attr_num(G, attribute):
   
    attribute_values = nx.get_node_attributes(G, attribute).values()
    attribute_counts = Counter(attribute_values)
    
    for attr_val, count in attribute_counts.items():
        print(attr_val, count)

def save_dataframe_as_png(df, filename, table_type):
    fig, ax = plt.subplots(figsize=(len(df.columns)*2.2, len(df)*0.5)) # Adjust figsize as needed
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    if table_type=='centrality':
        table.set_fontsize(18)
    table.scale(1.5, 1.5) # Adjust scale as needed
    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        if table_type=='centrality':
            cell.set_height(0.02)
            if key[1] == 0:
                cell.set_width(0.16)
            else:
                cell.set_width(0.1)
        if table_type=='attribute_counts':
            cell.set_height(0.01)
            if key[1] == 1:
                cell.set_width(0.8)
            else:
                cell.set_width(0.3)
    
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)