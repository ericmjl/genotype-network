from Bio import SeqIO
import networkx as nx
from Levenshtein import distance
from itertools import combinations
from scipy.misc import comb


class ProteinGN(object):

    """docstring for ProteinGN"""

    def __init__(self):
        super(ProteinGN, self).__init__()
        self.G = nx.Graph()

    @property
    def nodes(self):
        return self.G.nodes()

    def generate_genotype_network(self, handle):
        """
        Generates a network of genotypes that are 1 AA apart based on
        information from the dictionary.
        - Nodes: amino acid sequence.
        - Edges: indicate that two sequences are 1 AA apart

        Parameters:
        ===========
        - handle:    (str) name of the FASTA file that contains the sequences.

        Returns:
        ========
        None
        """
        sequences = SeqIO.to_dict(SeqIO.parse(handle, 'fasta'))

        for accession, sequence in sequences.items():
            if sequence in self.G.nodes():
                self.G.node[sequence]['accessions'].add(accession)
            else:
                self.G.add_node(sequence, accessions=set([accession]))

        # Compute the total number of comparisons to make.
        total = comb(len(self.G.nodes()), 2)

        for i, (seq1, seq2) in enumerate(combinations(self.G.nodes(), 2)):
            # Print to screen the current combination being run.
            print("{0} of {1} combinations".format(i, total))

            if distance(str(seq1.seq), str(seq2.seq)) == 1:
                self.G.add_edge(seq1, seq2)

    def write_genotype_network(self, handle):
        """
        Writes the genotype network to disk.

        Parameters:
        ===========
        - handle    (str) the file name, including path, to save the genotype
                    network to
        """

        nx.write_gpickle(self.G, handle)

    def find_network_cycle(self, root):
        """
        Finds network cycle with an optional root.

        Parameters:
        ===========
        - root    (str) the amino acid sequence to find a cycle with this root
        """
        return nx.cycle_basis(self.G, root)

    def read_genotype_network(self, handle):
        """
        Reads a previously constructed genotype network.

        Parameters:
        ===========
        - handle    (str) the file name, including path, to read the genotype
                    network from.
        """

        g = nx.read_gpickle(handle)
        # check that this is a NetworkX undirected graph.
        assert isinstance(g, nx.Graph), "The file is not a NetworkX graph"
        self.G = g
