import genotype_network as gn
import os

GN = gn.GenotypeNetwork()
GN.read_sequences('Test/Demo_052715.fasta')
GN.generate_genotype_network()
GN.write_genotype_network('Test/Demo_052715.pkl')


def test_read_sequences_works_correctly():
    """
    Checks that GN.read_sequences reads in correct number of sequences.
    """
    assert len(GN.sequences) == 3


def test_generate_genotype_network():
    """
    Checks that the number of nodes equals the number of sequences
    Checks number of edges
    """
    assert len(GN.sequences) == len(GN.G.nodes())
    assert len(GN.G.edges()) == 2  # This will change based on dataset


def test_write_genotype_network():
    """
    Checks that the pickled network is written to disk.
    """

    assert 'Demo_052715.pkl' in os.listdir('Test')
