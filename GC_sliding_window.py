# Calculate GC content of sequence in sliding window given input DNA sequence. Window can be adjusted in the code.

def gc_content(DNA_seq):
    # Define bold style
    class style:
       BOLD = '\033[1m'
       END = '\033[0m'

    # Set what characters are acceptable as an input.
    acceptableChars = ["A", "T", "G", "C"]
    set(acceptableChars)

    # Set AT and GC variables to 0
    GC = 0
    AT = 0

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

    if inputcheck(DNA_seq) == True:

        # To separate nucleotides into a list by iterating through the length of the list
        DNA_seq = [DNA_seq[i] for i in range(0, len(DNA_seq), 1)]

        for n in DNA_seq:
            if n == "C" or n == "G":
                GC += 1
            elif n == "A" or n == "T":
                AT += 1

        GC_Percent = (GC / len(DNA_seq))
        AT_Percent = (AT / len(DNA_seq))
        print("\n")

        # Format as percent
        print("This sequence is " + style.BOLD + '{:.2%}'.format(GC_Percent) + style.END + " G and C nucleotides. There are " + style.BOLD + str(GC) + " G and C nucleotides" + style.END + " in this sequence.")
        print("This sequence is " + style.BOLD + '{:.2%}'.format(AT_Percent) + style.END + " A and T nucleotides. There are " + style.BOLD + str(AT) + " A and T nucleotides" + style.END + " in this sequence.")
        print("\n")

# Get segments of sequence using sliding window
def overlap(DNA_seq, window_size):
    DNA_seq = DNA_seq.upper()
    b = [DNA_seq[i:i + window_size] for i in range(len(DNA_seq) - 2)]
    return b

# Get GC content if segments in sliding window
def gc_cont_seg(DNA_seq):
    for n in DNA_seq:
        GC = 0
        segment = list(n)
        for x in segment:
            if x == "C" or x == "G":
                GC += 1
            GC_Percent = (GC / len(segment))
        print(n, GC_Percent)

# test = overlap('ATGCGCCG', 3)
# gc_cont_seg(test)
