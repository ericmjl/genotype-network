from genotype_network.protein import ProteinGN
import os
import networkx as nx

# Change cwd for tests to the current path.
here = os.path.dirname(os.path.realpath(__file__))
os.chdir(here)

GN = ProteinGN()
GN.generate_genotype_network('test_data/Demo_052715.fasta')
GN.write_genotype_network('test_data/Demo_052715.pkl')
GN.read_genotype_network('test_data/Demo_052715.pkl')


def test_read_sequences_works_correctly():
    """
    Checks that GN.read_sequences reads in correct number of sequences.
    """
    assert len(GN.nodes) == 3

    for n, d in GN.nodes:
        assert isinstance(n, str)
        if len(d['accessions']) == 2:
            assert 'human_h1n1_mut3_same_as_mut1' in d['accessions']

def test_generate_genotype_network():
    """
    Checks that the number of nodes equals the number of sequences
    Checks number of edges
    """
    assert len(GN.edges) == 2


def test_write_genotype_network():
    """
    Checks that the pickled network is written to disk.
    """

    assert 'Demo_052715.pkl' in os.listdir('test_data')

def test_read_genotype_network():
    """
    Checks that the genotype network is being loaded correctly by counting
    nodes in a test pkl file.
    """

    G = nx.read_gpickle('test_data/Demo_052715.pkl')
    # The length of the test file
    assert len(G.nodes()) == 3
