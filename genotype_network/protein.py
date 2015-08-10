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

        # Compute the total number of comparisons to make.
        total = comb(len(self.sequences.keys()), 2)
        for i, (seq1, seq2) in enumerate(
                combinations(self.sequences.keys(), 2)):

            print("{0} of {1} combinations".format(i, total))
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
        # Checks that this is a NetworkX undirected graph.
        assert isinstance(g, nx.Graph), "The file is not a NetworkX graph"
        self.G = g

    def find_polymorphism(self, pos, letter):
        """
        Reads the genotype network and returns a list of nodes at position 
        pos and letter letter.

        Parameters:
        ===========
        - pos   (str) the amino acid position, user input

        - letter   (str) the amino acid name, user input
        """
       
        # Checks that this is a NetworkX undirected graph.
        assert isinstance(G, nx.Graph), "The file is not a NetworkX graph"
        poly_nodes = []
        # Iterates through all nodes and returns a list of sequences that
        # match with user inputs
        for n in G.nodes():
        	node = n
        	if node[pos] == letter:
        		poly_nodes.append(node)
        return poly_nodes
