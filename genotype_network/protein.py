from Bio import SeqIO
from Bio.Alphabet import generic_protein
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
        return self.G.nodes(data=True)

    @property
    def edges(self):
        return self.G.edges(data=True)

    def generate_genotype_network(self, handle, verbose=False):
        """
        Generates a network of genotypes that are 1 AA apart based on
        information from the dictionary.
        - Nodes: (str) amino acid sequence.
        - Edges: indicate that two sequences are 1 AA apart

        Parameters:
        ===========
        - handle:    (str) name of the FASTA file that contains the sequences.

        Returns:
        ========
        None
        """
        # Note: Alphabet is specified, so that the protein genotype network is
        # correctly constructed on a set of protein sequences, not nucleotides.
        sequences = SeqIO.to_dict(SeqIO.parse(handle, 'fasta',
                                              alphabet=generic_protein))

        for accession, sequence in sequences.items():
            if str(sequence.seq) in self.nodes:
                self.G.node[str(sequence.seq)]['accessions'].add(accession)
            else:
                self.G.add_node(str(sequence.seq), accessions=set([accession]))
        # Compute the total number of comparisons to make.
        total = comb(len(self.nodes), 2)

        for i, (seq1, seq2) in enumerate(combinations(self.nodes, 2)):
            # This reassignment is done because Seq1 and Seq2 are themselves
            # tuples of (node, metadata_dict).
            seq1 = seq1[0]
            seq2 = seq2[0]

            # Print to screen the current combination being run.
            if verbose:
                print("{0} of {1} combinations".format(i, total))
            lev_distance = distance(str(seq1), str(seq2))
            if lev_distance == 1:
                self.G.add_edge(str(seq1), str(seq2))

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
