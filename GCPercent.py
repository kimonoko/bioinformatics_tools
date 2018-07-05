# Calculate GC percent

DNA_seq = ["G", "A", "T", "C", "G", "C", "C", "G", "T", "G", "C", "T", "A", "G", "T"]
GC = 0

#for index, s in enumerate(DNA_seq):
#    print (index, s)

for n in DNA_seq:
    if n == "C" or n == "G":
        GC += 1
        
GC_Percent = (GC / len(DNA_seq))
print("\n")

# format as percent
print("The GC percent of this sequence is:" + '{:.2%}'.format(GC_Percent))