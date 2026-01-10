with open("010826.fasta", "r") as file:
    for el in file:
        option = el.startline(">")

print(option)