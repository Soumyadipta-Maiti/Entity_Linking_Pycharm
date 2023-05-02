from EL_Wiki import Entity_Linking_via_Wiki
import pandas as pd

input_str = str(input('Write Your Sentence :\n'))
input_lst = list(input_str.split('. '))
input_df = pd.DataFrame(input_lst)
op_el = pd.DataFrame()
op_el = Entity_Linking_via_Wiki(input_df)

print(op_el)

