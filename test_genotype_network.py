import genotype_network as gn

GN = gn.GenotypeNetwork()
GN.read_sequences('Test\Demo_052715.fasta')

def test_read_sequences_works_correctly():
	'''
	Checks that GN.read_sequences reads in correct number of sequences.
	'''
	assert len(GN.seq) == 3