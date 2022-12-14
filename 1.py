import json

with open('bigpencil1.json', "r", encoding='utf-8') as f:
    data = json.load(f)
    mean_sum = 0
    percent_sum = 0
    c = 0
    for i, j in data.items():
        mean_sum += j['mean']
        percent_sum += j['percent']
        c += 1
        
    print(mean_sum, percent_sum, c)
    
#16,148 11.754 99