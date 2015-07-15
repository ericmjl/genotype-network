# import list_compiler as lc 
# import os 
# import pickle as pkl

# from scipy.misc import comb

# assert 'Test' in os.listdir(os.getcwd()), 'Test directory required for test data.'
# assert 'pickled_lists' in os.listdir(os.getcwd()), 'pickled_lists required for pickled lists.'

# filename = 'Test/test_sequences.fasta'
# m_cpu = 2
# LC = lc.ListCompiler(m_cpu)
# LC.read_sequences(filename)
# LC.compile_list()
# LC.divide_list()

# def test_read_sequences():
# 	assert len(LC.sequences) == 5

# def test_compile_list():
# 	"""
# 	Checks to make sure that the length of master_seq is N choose 2.
# 	"""
# 	assert len(LC.master_seq) == comb(len(LC.sequences), 2)

# def test_divide_list():
# 	"""
# 	Checks to make sure that the length of the lists put together 
# 	is the length of the original master list.
# 	"""
# 	total_length = 0
# 	for filename in os.listdir('pickled_lists'):
# 		if '.pkllist' in filename:
# 			with open('pickled_lists/{0}'.format(filename)) as f:
# 				total_length += len(pkl.load(f))

# 	assert total_length == len(LC.master_seq)

