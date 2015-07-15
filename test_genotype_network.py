import genotype_network as gn

GN = gn.GenotypeNetwork()
GN.read_sequences('Test/Demo_052715.fasta')
GN.generate_genotype_network()

def test_read_sequences_works_correctly():
	"""
	Checks that GN.read_sequences reads in correct number of sequences.
	"""
	assert len(GN.seq) == 3

# def test_generate_genotype_network():
# 	"""
# 	Checks that the number of nodes equals the number of sequences
# 	Checks number of edges
# 	"""
# 	assert len(GN.seq) == len(GN.G.nodes())
# 	assert len(GN.G.edges()) == 1 #This will change based on dataset

