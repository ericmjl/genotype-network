import networkx as nx
import distance
import pickle as pkl

class SubgraphProcessor(object):
	"""
	This class reads each sublist from ListCompiler, generates a graph, and saves them into directory
	"""
	def __init__(self):
		super(SubgraphProcessor, self).__init__()
		self.P = nx.Graph()
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
		self.sequences = set([s.seq for s in SeqIO.parse(filename, 'fasta')])

		with open("pickled_lists/CPU{0}_comparisons.pkllist".format(current_CPU),'r') as f:
			for seq in self.seq: #Adds a node for each sequence
				self.P.add_node(seq)

		for seq1, seq2 in combinations(self.seq, 2):
			if distance.levenshtein(self.seq[seq1], self.seq[seq2]) == 1:
				self.P.add_edge(seq1, seq2)

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

		with open("subgraphs/subgraph_CPU{0}.pkllist".format(current_CPU),'w') as f:
			pkl.dumps(self.P, f)
