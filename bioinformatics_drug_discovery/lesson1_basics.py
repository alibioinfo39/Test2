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
    "V": "Hydrophobic",
    "I": "Hydrophobic",
    "L": "Hydrophobic",
    "M": "Hydrophobic",
    "F": "Hydrophobic",
    "W": "Hydrophobic",
    "Y": "Hydrophobic",
    
    "K": "Positive",
    "R": "Positive",
    "H": "Positive",
    
    "D": "Negative",
    "E": "Negative",
    
    "S": "Polar",
    "T": "Polar",
    "N": "Polar",
    "Q": "Polar",
    "C": "Polar",
    "G": "Neutral",
    "P": "Neutral"
}

# for aa in protein_sequence:
#     if aa in aa_property:
#         print(aa, aa_property[aa])

#Count Amino Acids
sequence = "MKTAYIAKQRQISFVKSHFSRQDILDLW"

aa_count = {}

# for aa in sequence:
#     aa_count[aa] = aa_count.get(aa, 0) + 1

#Assignment Hydrophobic %



print(len(sequence))

hydophobic_count = 0 

for aa in sequence:
    if aa in aa_property:
        if aa_property[aa] == "Hydrophobic":
            hydophobic_count += 1

hydrophonic_percent = (hydophobic_count/ len(sequence)) * 100
print(f"Hydrophobic residues: {hydophobic_count}")
print(f"Hydrophobic percentage: {hydrophonic_percent:.2f}%")
#Hydophobic is crucial in ligand binding because it is how they drive the interaction through hydophobic effect creating a favorable environment by releasing ordered water molecules



