import csv

with open('top_cities.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader() #첫번째 줄에는 헤더를 입력

    writer.writerows([
        {'rank': 1, 'city':'상하이', 'population':241500000},
        {'rank': 2, 'city': '카리치', 'population': 341500000},
        {'rank': 3, 'city': '베이징', 'population': 441500000},
        {'rank': 4, 'city': '텐진', 'population': 541500000},
        {'rank': 5, 'city': '이스탄불', 'population': 641500000},
    ])