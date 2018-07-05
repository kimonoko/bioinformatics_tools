# Generate the reverse, complement and reverse complement of an input DNA sequence. Only ATGC accepted, upper or lower case.

seq = input('Please enter a DNA sequence. ')
seq = seq.upper()
seq = list(seq)

rev_seq = seq[::-1]
print('The reverse of thise sequence is ' + str(''.join(rev_seq)) + '.')

DNA_comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
comp = [DNA_comp[nuc] for nuc in seq]
print('The complement of this sequence is ' + str(''.join(comp)) + '.')

rev_comp = comp[::-1]
rev_comp = ''.join(rev_comp)
print('The reverse complement of this sequence is ' + str(rev_comp) + '.')
