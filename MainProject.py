import pandas as pd
import numpy as pe 

from chembl_webresource_client.new_client import new_client


target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)

selected_target = targets.target_chembl_id[11]
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
df = pd.DataFrame.from_dict(res)

print(targets)