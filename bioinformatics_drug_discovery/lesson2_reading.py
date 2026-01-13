#Reading fasta file and Analyzign protein properties

fasta_file = "proteins.fasta"
sequences = {}  # dictionary to store sequences: {header: sequence}

with open(fasta_file, "r") as f:
    header = ""
    seq = ""
    for line in f:
        line = line.strip()  # remove whitespace & newline
        if line.startswith(">"):
            if header:
                sequences[header] = seq  # save previous sequence
            header = line[1:]  # remove ">"
            seq = ""
        else:
            seq += line  # append sequence lines
    sequences[header] = seq  # save last sequence

# Check results
for h, s in sequences.items():
    print(f"{h}: {s}")



#011326
aa_property = {
    "K": "Positive",
    "R": "Positive",
    "H": "Positive",
    "D": "Negative",
    "E": "Negative",
    "S": "Polar",
    "T": "Polar",
    "N": "Polar",
    "Q": "Polar",
    "A": "Hydrophobic",
    "V": "Hydrophobic",
    "I": "Hydrophobic",
    "L": "Hydrophobic",
    "M": "Hydrophobic",
    "F": "Hydrophobic",
    "W": "Hydrophobic",
    "Y": "Hydrophobic",
    "C": "Neutral",
    "G": "Neutral",
    "P": "Neutral"
}

for header, seq in sequences.items():
    pe = {"Hydrophobic": 0, "Positive": 0, "Negative": 0, "Polar": 0, "Neutral": 0}
    for aa in seq:
        if aa in aa_property:
            category = aa_property[aa]
            pe[category] += 1
        else:
            print(f"Unknown amino acid in {header}: {aa}")

    print(f"\nProtein: {header}")
    print("----------------------------")
    total_length = len(seq)
    for category, count in pe.items():
        perc = (count / total_length) * 100
        print(f"{category}: {count} ({perc:.2f}%)")

