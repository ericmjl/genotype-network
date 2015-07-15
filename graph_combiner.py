import networkx as nx 
import os 

class GraphCombiner(object):
	"""
	This object is responsible for the "reduce" step of combining the 
	computed subgraphs. It is step #3 in the process.

	Parameters:
	===========
	- directory: 		(str) the directory in which the subgraphs are stored.
	"""
	def __init__(self, directory):
		super(GraphCombiner, self).__init__()
		self.directory = directory
		self.subgraphs = []		
		self.G = nx.Graph()

	def read_graphs(self):
		"""
		Reads the present in the directory into the list of graphs.
		"""
		for f in os.listdir(self.directory):
			if f.split('.')[-1] == 'pkl':
				subgraph = nx.read_gpickle(f)
				self.subgraphs.append(subgraph)

	def combine_graphs(self):
		"""
		Combines the subgraphs into a single graph. 
		"""
		for g in self.subgraphs:
			self.G.add_edges_from(g.edges())

	def write_combined_graph(self):
		"""
		Writes the graph to disk.
		"""
		nx.write_gpickle(self.G, 'combined_graph.pkl')

