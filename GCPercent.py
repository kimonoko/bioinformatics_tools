# Define bold style
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

# Calculate GC percent

DNA_seq = input("Please type your DNA sequence. ")
set(DNA_seq)

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
    
    # Tm calculator
    
    Primer_Check = input(style.BOLD + "Is this sequence a primer? (y/n) " + style.END)
    
    def Primer_Check_Function(Primer_Check):
        print("\n")
        if Primer_Check == "y" or Primer_Check == "Y":
            Tm = ((GC * 4) + (AT * 2))
            print("The annealing temperature (Tm) of this primer is " + style.BOLD + str(Tm) + " degrees Celsius" + style.END + ".") 
            print("\n")
            print(style.BOLD + "Thank you for using the GC content calculator!" + style.END)
        elif Primer_Check == "n" or Primer_Check == "N":
            print(style.BOLD + "Thank you for using the GC content calculator!" + style.END)
        # Loop back to input if not y or n. 
        else:
            print(style.BOLD + "Please only enter y for yes or n for no." + style.END)
            Primer_Check = input(style.BOLD + "Is this sequence a primer? (y/n) " + style.END)
            Primer_Check_Function(Primer_Check)

    Primer_Check_Function(Primer_Check)
