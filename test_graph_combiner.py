# import graph_combiner as gc
# import os 
# import pickle as pkl

# directory = ('Test')
# GC = gc.GraphCombiner(directory)
# GC.read_graphs()
# GC.combine_graphs()
# GC.write_combined_graph()

# assert 'Test' in os.listdir(os.getcwd()), 'Test directory that stores test data'
# assert 'pickled_lists' in os.listdir(os.getcwd()), 'pickled_lists that will be combined'

# def test_read_graphs():
# 	"""
# 	Checks that GC.read_graphs reads correct number of graphs
# 	"""
# 	assert len(GC.subgraphs) == 3

# def test_combine_graphs():
# 	"""
# 	Checks that GC.combine_graphs combines the right number of nodes and edges
# 	"""
# 	assert len(GC.subgraphs) == len(GC.G.nodes())
# 	assert len(GC.G.edges()) == 3 #This will change based on number of edges

# def test_write_combined_graph():
# 	"""
# 	Checks that GC.write_combined_graph can write correct length graph to disk
# 	"""
# 	assert len('Test/combined_graph.pkl') == 3