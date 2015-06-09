from Bio import SeqIO
from itertools import combinations 

class ListCompiler(object):
	"""
	This class reads sequences from a file, compiles a master list of comparisons, and divides the list into sublists
	"""
	def __init__(self):
		super(ListCompiler, self).__init__()
		self.masterList = dict()
		self.sequences = dict()

	def read_sequences(self, filename):
		"""
		Reads in a sequence of type FASTA, assigns it to self.masterList as a dictionary
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
		self.sequences = set([s.seq for s in SeqIO.parse(filename, 'fasta')])

	def compile_list(self):
		"""
		Generates a master list of all the comparisons you need to make
		Dict Keys: One sequence
		Dict Values: Another sequence

		Parameters
		-----
		None
		-----

		Returns
		-----
		None
		-----
		"""
		for seq1, seq2 in combinations(self.sequences, 2):
			self.masterList[seq1] = seq2

	def divide_list(self, processor):
		"""
		Divides the master list based on the number of processors (cores)
		Parameters
		-----
		processor: Number of CPUs
		-----

		Returns
		-----
		None
		-----
		"""
		