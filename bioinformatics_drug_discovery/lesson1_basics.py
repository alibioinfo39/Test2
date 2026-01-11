#Step 1 Printing
print("Python for Bioinformatics Drug Discovery")

#Variables
gene_name = "TP53"
protein_length = 393
mutation_rate = 0.02

print(gene_name)
print(protein_length)
print(mutation_rate)

#Protein sequence
protein_sequence = "MKTAYIAKQRQISFVKSHFSRQDILDLW"

print(protein_sequence[0])    # First
print(protein_sequence[-1])   # Last

#looping through a protein

# for aa in protein_sequence:
#     print(aa)

#Dictionary = Amino Acid Properties
aa_property = {
    "A": "Hydrophobic",
    "E": "Negative",
    "K": "Positive",
    "S": "Polar"
}

for aa in protein_sequence:
    if aa in aa_property:
        print(aa, aa_property[aa])

#Count Amino Acids
aa_count = {}

for aa in protein_sequence:
    aa_count[aa] = aa_count.get(aa, 0) + 1
print(aa_count)