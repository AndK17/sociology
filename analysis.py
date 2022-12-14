from detoxify import Detoxify
import pandas as pd
import json
import os

model = Detoxify('multilingual')


def analys_for_screen(input_data, toxicity_precentage = 0.7):
    if input_data != []:
        results = []
        c = 1
        for i in input_data:
            r = model.predict(i.replace('\n', ''))
            results.append(r)
            print(f'{c}/{len(input_data)} OK')
            c += 1
        pdres = pd.DataFrame(results, index=input_data).round(5)
        print(pdres)
        percent = round(sum([1 for i in pdres if i > toxicity_precentage])/len(pdres), 3)
        return percent, len(pdres)
    else:
        return 0, 0
  
    
def analys(input_data, toxicity_precentage = 0.7):
    if input_data != []:
        results = []
        c = 1
        for i in input_data:
            results.append(model.predict(i.replace('\n', '')))
            print(f'{c}/{len(input_data)} OK')
            c += 1
        pdres = pd.DataFrame(results, index=input_data).round(5)['toxicity']
        percent = round(sum([1 for i in pdres if i > toxicity_precentage])/len(pdres), 3)
        return percent, len(pdres)
    else:
        return 0, 0
    
    
# directory = '55x55_2022-12-14'
# directory = 'Соточкапорусскому_2022-12-14'
# directory = 'Поступашки_2022-12-14'
# directory = 'Диджитализируй_2022-12-14'
# directory = 'вДудь_2022-12-14'
# directory = 'ВПИСКА_2022-12-14'
# directory = 'Апоговорить_2022-12-14'
# directory = 'XENO_2022-12-14'
# directory = 'HFA_2022-12-14'
# directory = 'БустерИграет_2022-12-14'
directory = 'BadComedian_2022-12-14'
# directory = 'СоседКомкиных_2022-12-14'
    
with open(f'youtube/{directory}.txt', "r", encoding='utf-8') as f:
    data = f.readlines()
    print(directory, analys(data))
    
#tg
#postupashki - (0.026, 3372), nemorgenshtern - (0.139, 15613), bigpencil c постом - (0.125, 25021), bigpencil без поста - (0.104, 19918)
#youtube
# Соточкапорусскому_2022-12-14 (0.013, 3467) Поступашки_2022-12-14 (0.036, 9116) Диджитализируй_2022-12-14 (0.018, 9599) - 546 токс./22 182 всего = 0.025
# вДудь_2022-12-14 (0.114, 9781) ВПИСКА_2022-12-14 (0.073, 8511) Апоговорить_2022-12-14 (0.127, 9873) - 2990 токс./28165 всего = 0.106
# HFA_2022-12-14 (0.045, 9241) XENO_2022-12-14 (0.057, 9670) БустерИграет_2022-12-14 (0.054, 9541) - 1482 токс./28452 всего = 0.052
# СоседКомкиных_2022-12-14 (0.103, 8894) BadComedian_2022-12-14 (0.116, 5706) 55x55_2022-12-14 (0.056, 9709) - 2122 токс./24309 всего = 0.087



# for directory in ['bigpencil']:
# directory = 'nemorgenshtern'
# files = os.listdir(directory)
# res = {}

# i = 1
# for file in files:
    # with open(directory+'/'+file, "r", encoding='utf-8') as f:
    #     data = json.load(f)
    #     percent, count = analys(data['comments'])
#         res[data['link']] = {'text':data['text'],
#                             'percent':percent,
#                             'count':count}
#     print(f'{directory} {i}/{len(files)} OK')
#     i += 1
        
# print(res)
# with open(directory+".json", "w", encoding="utf-8") as write_file:
#     json.dump(res, write_file, ensure_ascii=False)
    