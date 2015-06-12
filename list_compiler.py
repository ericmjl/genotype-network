from Bio import SeqIO
from itertools import combinations 
import pickle as pkl

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
		Generates a master list of tuples for all comparisons e.g. [(1,2),(1,3)]
		List Index: Normal index
	    List Value: Tuple of the 2 sequences

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
			self.masterSeq.append(seq1, seq2)

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
		m_CPUs = 32
		i = 0

		block_size = math.ceil(len(self.masterSeq)/m_CPUs)
		current_CPU = 0
		while(i + block_size) < len(self.masterSeq):
			with open("pickled_lists/CPU{0}_comparisons.pkllist".format(current_CPU),'w') as f:
				pkl.dumps(self.masterSeq[i : i + block_size], f)