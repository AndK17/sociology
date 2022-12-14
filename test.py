from detoxify import Detoxify
import json


with open('nemorgenshtern/nemorgenshtern_3633604.json', "r", encoding='utf-8') as f:
    data = json.load(f)['comments']

print(data)
results = Detoxify('multilingual').predict(data)
    # print(i, results)

import pandas as pd
    
print(pd.DataFrame(results, index=data).round(5))

# import os
# import json


# directorys = ['bigpencil']#, 'postupashki', 'nemorgenshtern']

# for directory in directorys:
#     files = os.listdir(directory)

#     c = 0
#     with open(directory+'1.txt', 'w', encoding='utf-8') as wf:
#         for file in files:
#             with open(directory+'/'+file, "r", encoding='utf-8') as f:
#                 data = json.load(f)['comments']
#                 for i in data:
#                     if i not in ['', ' ', '\n']:
#                         wf.write(i.replace('\n', ' ')+'\n')
#                     c += 1
        
#     print(c)