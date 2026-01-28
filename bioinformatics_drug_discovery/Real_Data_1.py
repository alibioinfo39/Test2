import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bacteria_list_200.csv")

# harmful = {"Yes":0}
# not_harmful = {"No":0}
# for value in df["Harmful to Humans"]:
#     if value == "Yes":
#         harmful["Yes"] += 1
# for op in df["Harmful to Humans"]:
#     if op == "No":
#         not_harmful["No"] += 1

# print(f"Numbers of Not Harmful:  {not_harmful}")
# print(harmful)

counts = df["Harmful to humans"].value_counts()
print(counts)