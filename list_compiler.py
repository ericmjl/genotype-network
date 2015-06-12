from Bio import SeqIO
from itertools import combinations 
import multiprocessing
from collections import defaultdict

class ListCompiler(object):
	"""
	This class reads sequences from a file, compiles a master list of comparisons, and divides the list into sublists
	"""
	def __init__(self):
		super(ListCompiler, self).__init__()
		self.masterSeq = defaultdict(list)
		self.sequences = dict()

	def read_sequences(self, filename):
		"""
		Reads in a sequence of type FASTA, assigns it to self.sequences as a dictionary
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
		Dict keys: One sequence object
		Dict value: Other sequence object

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
			self.masterSeq[seq1].append[seq2]

	def divide_list(self):
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
		m = multiprocessing.cpu_count()
		
