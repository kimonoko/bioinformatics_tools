# Calculate the approximate molecular weight of a DNA or RNA sequence, default DNA. Accounts for N.

def mol_weight(seq, nuc='DNA'):
    seq = list(seq)
    DNA_key = {'A':331, 'T':306, 'G':347, 'C':307}
    DNA_key['N'] = sum(DNA_key.values()) / len(DNA_key)
    RNA_key = {'A':347, 'U':324, 'G':363, 'C':323}
    RNA_key['N'] = sum(RNA_key.values()) / len(RNA_key)

    if nuc == 'DNA':
        weights = [DNA_key[nuc] for nuc in seq]
        print('The approximate molecular weight of this', nuc, 'sequence is ' + str(sum(weights)) + ' g/mol.')
    elif nuc == 'RNA':
        weights = [RNA_key[nuc] for nuc in seq]
        print('The approximate molecular weight of this', nuc, 'sequence is ' + str(sum(weights)) + ' g/mol.')

# Example sequence.
# mol_weight('AUGCN', nuc='RNA')