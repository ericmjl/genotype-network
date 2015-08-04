import GenotypeNetwork as gn
import os
import networkx as nx

# Change cwd for tests to the current path.
here = os.path.dirname(os.path.realpath(__file__))
os.chdir(here)

GN = gn.GenotypeNetwork()
GN.read_sequences('test/Demo_052715.fasta')
GN.generate_genotype_network()
GN.write_genotype_network('test/Demo_052715.pkl')
GN.read_genotype_network('test/Demo_052715.pkl')


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

    assert 'Demo_052715.pkl' in os.listdir('test')


def test_read_genotype_network():
    """
    Checks that the genotype network is being loaded correctly by counting
    nodes in a test pkl file.
    """

    G = nx.read_gpickle('test/Demo_052715.pkl')
    # The length of the test file
    assert len(G.nodes()) == 3
