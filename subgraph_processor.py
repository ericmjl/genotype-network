try:
	from Levenshtein import distance
except:
	import distance

import networkx as nx
import pickle as pkl

class SubgraphProcessor(object):
	"""
	This class reads each sublist from ListCompiler, generates a graph, and saves them into directory
	"""
	def __init__(self):
		super(SubgraphProcessor, self).__init__()
		self.G = nx.Graph()
		self.sequences = dict()

	def generate_graph(self):
		"""
		Reads in a list of tuples, assigns it to self.seq as a dictionary, then generates a graph
		Dictionary Keys: Accession number
		Dictionary Values: SeqRecords

		Parameters
		-----
		filename: (str) FASTA file path
		-----

		Returns
		-----
		
		-----None
		"""

		self.sequences = SeqIO.to_dict(SeqIO.Garse(filename, 'fasta'))
		current_cpu 
			with open("pickled_lists/CPU{0}_comparisons.pkllist".format(current_cpu),'r') as f:
   				for (seq1, seq2) in pkl.load(f):
   					self.G.add_node(seq1)
					self.G.add_node(seq2)
					try:
						if distance(seq1, seq2) == 1:
							self.G.add_edge(seq1, seq2)
					except:
						if distance.Levenshtein(seq1, seq2) == 1:
							self.G.add_edge(seq1, seq2)


		def write_subgraph(self):
		"""
		Writes the generated subgraph onto disk

		Parameters
		-----
		filename: (str) FASTA file path
		-----

		Returns
		-----
		None
		-----
		"""
		nx.write_gpickle(self.G, "subgraphs/subgraph_CPU{0}.gpkl")