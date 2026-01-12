#Step 1 Printing
print("Python for Bioinformatics Drug Discovery")

#Variables
gene_name = "TP53"
protein_length = 393
mutation_rate = 0.02

# print(gene_name)
# print(protein_length)
# print(mutation_rate)

#Protein sequence
protein_sequence = "MKTAYIAKQRQISFVKSHFSRQDILDLW"

# print(protein_sequence[0])    # First
# print(protein_sequence[-1])   # Last

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
# print(f"Hydrophobic residues: {hydophobic_count}")
# print(f"Hydrophobic percentage: {hydrophonic_percent:.2f}%")

#f in print is called an f-string it makes u combine text and numbers without breaking the code
#.2f is 2 decimals 
#Hydophobic is crucial in ligand binding because it is how they drive the interaction through hydophobic effect creating a favorable environment by releasing ordered water molecules

#assignment 2

# for aa in sequence:
#     if aa in aa_property:
#         if aa_property[aa] == "Hydrophobic":
#             hydophobic_count += 1
# hydrophonic_percent = (hydophobic_count/ len(sequence)) * 100
# print(f"Hydrophobic residues: {hydophobic_count}")
# print(f"Hydrophobic percentage: {hydrophonic_percent:.2f}%")

# positive_count = 0
# for aa in sequence:
#     if aa in aa_property:
#         if aa_property[aa] == "Positive":
#             positive_count += 1
# positive_percent = (positive_count/ len(sequence)) * 100
# print(f"Positive residues: {positive_count}")
# print(f"Positive percentage: {positive_percent:.2f}%")

# negative_count = 0
# for aa in sequence:
#     if aa in aa_property:
#         if aa_property[aa] == "Negative":
#             negative_count += 1
# negative_percent = (negative_count/ len(sequence)) * 100
# print(f"Negative residues: {negative_count}")
# print(f"Negative percentage: {negative_percent:.2f}%")

# polar_count = 0
# for aa in sequence:
#     if aa in aa_property:
#         if aa_property[aa] == "Polar":
#             polar_count += 1
# polar_percent = (polar_count/ len(sequence)) * 100
# print(f"Polar residues: {polar_count}")
# print(f"Polar percentage: {polar_percent:.2f}%")

#Correction Assignment 2 

# Initialize counts
property_count = {
    "hydrophobic": 0,
    "positive": 0,
    "negative": 0,
    "polar": 0,
    "neutral": 0
}

# Loop through sequence once
for aa in sequence:
    if aa in aa_property:
        prop = aa_property[aa].lower()
        property_count[prop] += 1
    else:
        print(f"Unknown amino acid: {aa}")

# Calculate percentages
for prop, count in property_count.items():
    percent = (count / len(sequence)) * 100
    # print(f"{prop.capitalize()} residues: {count}")
    # print(f"{prop.capitalize()} percentage: {percent:.2f}%\n")


#Assignment 3
pe ={
    "Positive": 0,
    "Negative": 0,
    "Polar": 0,
    "Neutral": 0,
    "Hydrophobic" :0
}

for el in sequence:
    if el in aa_property:
        pa = aa_property[el]   # keep original case
        pe[pa] += 1
    else:
        print(f"Unknown amino acid detected: {el}")

for pa, tes in pe.items():
    perc = (tes / len(sequence))*100

print(f"{pa.capitalize()} Residues: {tes}")
print(f"{pa.capitalize()} Percentage: {perc:.2f}\n")
        


