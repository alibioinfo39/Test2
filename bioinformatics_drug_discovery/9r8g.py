import requests

pdb_id = "9R8G"  # example PDB ID
url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

response = requests.get(url)

if response.status_code == 200:
    with open(f"{pdb_id}.pdb", "w") as f:
        f.write(response.text)
    print("PDB file downloaded")
else:
    print("Failed to download")

from Bio.PDB import PDBParser
conflict = 0

parser = PDBParser(QUIET=True)
structure = parser.get_structure("protein", "9R8G.pdb")

Protein = {
    "ALA": 0,
    "ARG": 0,
    "ASN": 0,
}


for model in structure:
    for chain in model:
        print("Chain:", chain.id)
        for residue in chain:
            print(residue.get_resname(), residue.id)
            print(pe)

import requests

pdb_id = "9QFO"
url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"

response = requests.get(url)
response.raise_for_status()
data = response.json()

title = data["struct"]["title"]

organism = "N/A"

if "rcsb_entity_source_organism" in data and len(data["rcsb_entity_source_organism"]) > 0:
    if "scientific_name" in data["rcsb_entity_source_organism"][0]:
        organism = data["rcsb_entity_source_organism"][0]["scientific_name"]

print("Title:", title)
print("Organism:", organism)