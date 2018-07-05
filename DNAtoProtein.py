# Define bold style
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

# Set what characters are acceptable as an input.
acceptableChars = ["A", "T", "G", "C"]
set(acceptableChars)

# Prompt the user.
DNA_seq = input("Please type your DNA sequence. ")
set(DNA_seq)

# Eliminate spaces, if any.
DNA_seq = DNA_seq.replace(" ", "")

# Convert DNA sequence to uppercase
DNA_seq = DNA_seq.upper()

def inputcheck(DNA_seq):
    # If any character in the input is a number
    if any(char.isdigit() for char in DNA_seq):
        print("\n")
        print (style.BOLD + "Unacceptable input. Number detected." + style.END)
        return False
    # If any character in the input isn't an "acceptable character."
    elif set(DNA_seq).issubset(set(acceptableChars)) == False:
        print("\n")
        print (style.BOLD + "Unacceptable input. Only enter A, T, G or C." + style.END)
        return False
    else:
        return True

# If input is only ATGC, execute rest of script
if inputcheck(DNA_seq) == True:
    
    # To separate codons into a list by iterating through the length of the list
    DNA_seq = [DNA_seq[i:i+3] for i in range(0, len(DNA_seq), 3)]

    # Verify that list creation worked
    #print(DNA_seq)
    
    # * means STOP codon.

    # Codon/amino acid dictionary
    codon_to_protein = {"TTT": "F", "TTC": "F", 
                        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", 
                        "ATT": "I", "ATC": "I", "ATA": "I", 
                        "ATG": "M", 
                        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", 
                        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", 
                        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", 
                        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", 
                        "GCT": "A", "GCC":"A", "GCA": "A", "GCG": "A", 
                        "TAT": "Y", "TAC": "Y", 
                        "TAA": "*", "TAG": "*", "TGA": "*", 
                        "CAT": "H", "CAC": "H",  
                        "CAA": "Q", "CAG": "Q", 
                        "AAT": "N", "AAC": "N", 
                        "AAA": "K", "AAG": "K", 
                        "GAT": "D", "GAC": "D",
                        "GAA": "E", "GAG": "E", 
                        "TGT": "C", "TGC": "C", 
                        "TGG": "W",
                        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
                        "AGT": "S", "AGC": "S", 
                        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    protein_seq = [codon_to_protein[codon] for codon in DNA_seq]
    protein_seq = "".join(protein_seq)

    print("\n")
    print(style.BOLD + "Amino Acid Sequence:" + style.END)
    print("\n")
    print("Please note that asterisks (*) indicate a stop codon." + style.END)
    print("\n")
    print(protein_seq)

    from collections import Counter

    AA_freq = Counter(protein_seq)
    # Convert Counter output to a dictionary.

    import operator

    print("\n")
    print(style.BOLD + "Amino Acid Frequency: " + style.END)
    print("\n")

    AA_freq = dict(AA_freq)
    # Sort dictionary by value in descending order (reverse)
    sorted_AA_freq = sorted(AA_freq.items(), key=operator.itemgetter(1), reverse=True)

    def printfreq(sorted_AA_freq):
        for x in sorted_AA_freq:
            print(x[0], x[1])

    printfreq(sorted_AA_freq)
