from Bio import SeqIO
import networkx as nx

class GenotypeNetwork(object):
	"""docstring for GenotypeNetwork"""
	def __init__(self):
		super(GenotypeNetwork, self).__init__()
		self.G = nx.Graph()
		self.seq = dict()
		
	def read_sequences(self, filename):
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

	def generate_genotype_network(self):
		"""
		