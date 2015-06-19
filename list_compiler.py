from Bio import SeqIO
from itertools import combinations 
import pickle as pkl
import math

class ListCompiler(object):
	"""
	This class reads sequences from a file, compiles a master list of comparisons, and divides the list into sublists
	"""
	def __init__(self, m_cpu):
		super(ListCompiler, self).__init__()
		self.master_seq = list()
		self.sequences = set()
		self.m_cpu = m_cpu

	def read_sequences(self, filename):
		"""
		Reads in a sequence of type FASTA, assigns it to self.sequences as a set of biopython Seq objects.

		Parameters:
		===========
		- filename: 	(str) FASTA file path

		Returns:
		========
		None
		"""
		self.sequences = set([s.seq for s in SeqIO.parse(filename, 'fasta')])

	def compile_list(self):
		"""
		Generates a master list of tuples for all comparisons e.g. [(1,2),(1,3)]
		- List Index: Normal index
	    - List Value: Tuple of the 2 sequences

		Parameters:
		===========
		None

		Returns:
		========
		None
		"""
		for seq1, seq2 in combinations(self.sequences, 2):
			self.master_seq.append((seq1, seq2))

	def divide_list(self):
		"""
		Writes to disk the split lists as a series of pickled lists.
		
		Parameters:
		===========
		None

		Returns:
		========
		None

		"""
		i = 0

		block_size = int(math.ceil(len(self.master_seq)/self.m_cpu))
		current_cpu = 0
		while(i + block_size) <= len(self.master_seq):
			with open("pickled_lists/CPU{0}_comparisons.pkllist".format(current_cpu),'w') as f:
				pkl.dump(self.master_seq[i : i + block_size], f)
				i += block_size
				current_cpu += 1

