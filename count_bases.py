# Count the number of bases in a given sequence.

def count_bases(seq):
    seq = seq.upper()
    seq = list(seq)
    adenine = 0
    cytosine = 0
    thymine = 0
    guanine = 0
    unknown = 0
    
    for n in seq:
        if n == 'A':
            adenine += 1
        elif n == 'C':
            cytosine += 1
        elif n == 'T':
            thymine += 1
        elif n == 'G':
            guanine += 1
        else:
            unknown += 1
    
    print('There are ' + str(adenine) + ' adenines, ' + str(guanine) + ' guanines, ' + str(cytosine) + ' cytosines, ' + str(thymine) + ' thymines, and ' + str(unknown) + ' unknown nucelotides in this sequence.')

# Example input sequence
count_bases('ATGCCGCGCTGTGCRCGAGACGAC')