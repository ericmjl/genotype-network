from Bio import SeqIO
import networkx as nx
from Levenshtein import distance
from itertools import combinations


class GenotypeNetwork(object):

    """docstring for GenotypeNetwork"""

    def __init__(self):
        super(GenotypeNetwork, self).__init__()
        self.G = nx.Graph()
        self.sequences = dict()

    def read_sequences(self, filename):
        """
        Reads in a sequence of type FASTA, assigns it to self.sequences as a
        dictionary
        - Dictionary Keys: Accession number
        - Dictionary Values: SeqRecords

        Parameters:
        ===========
        - filename: (str) FASTA file path

        Returns:
        ========
        None
        """
        self.sequences = SeqIO.to_dict(SeqIO.parse(filename, 'fasta'))

    def generate_genotype_network(self):
        """
        Generates a network of genotypes that are 1 AA apart based on
        information from the dictionary.
        - Graph nodes: Individual HA sequences
        - Graph edges: Indicate that two sequences are 1 AA apart

        Parameters:
        ===========
        None

        Returns:
        ========
        None
        """
        for seq in self.sequences.keys():  # Adds a node for each sequence
            self.G.add_node(seq)

        for seq1, seq2 in combinations(self.sequences.keys(), 2):
            if distance(str(self.sequences[seq1].seq),
                        str(self.sequences[seq2].seq)) == 1:
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
