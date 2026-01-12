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
