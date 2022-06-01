import itertools
import pandas as pd

df = pd.read_csv(r"C:\Users\xu_zi\Desktop\lsl\Moffitt_and_Bambah-Mukku_et_al_merfish_all_cells.csv")
ans_df = pd.read_csv(r'C:\Users\xu_zi\Desktop\lsl\SUB-DATASET.csv')

for i, j in itertools.product(ans_df['Animal_ID'].unique(), ans_df['Bregma'].unique()):
    count+=1
    ans = df[ (df['Animal_ID'] == i ) & (df['Bregma'] == j ) ]
    if ans.shape[0]>0:
        name = str (ans_df[(ans_df['Animal_ID'] ==i) & (ans_df['Bregma'] == j)]['Subname'].unique()[0])
        #print(name)
        print(name,i, j,ans.shape,'is done')

        ans.to_csv('.\data\\' + name + ".csv", index=False)
        

print('done','*'*30)