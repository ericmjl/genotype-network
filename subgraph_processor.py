import networkx as nx
import distance

class SubgraphProcessor(object):
	"""
	This class reads each sublist from ListCompiler, generates a graph, and saves them into directory
	"""
	def __init__(self):
		super(SubgraphProcessor, self).__init__()
		self.G = nx.Graph()
		self.seq = dict()

	def generate_graph(self):
		"""
		Reads in a sequence of type FASTA, assigns it to self.seq as a dictionary
		Dictionary Keys: Accession number
		Dictionary Values: SeqRecords

		Parameters
		-----
		filename: (str) FASTA file path
		-----

		Returns
		-----
		None
		-----
		"""
		self.seq = SeqIO.to_dict(SeqIO.parse(filename, 'fasta'))

		for seq in self.seq: #Adds a node for each sequence
			self.G.add_node(seq)

		for seq1, seq2 in combinations(self.seq, 2):
			if distance.levenshtein(self.seq[seq1], self.seq[seq2]) == 1:
				self.G.add_edge(seq1, seq2)

		nx.write_gpickle(G, "graph.gpickle")