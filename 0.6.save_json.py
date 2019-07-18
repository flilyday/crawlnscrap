import json

cities = [
    {'rank': 1, 'city': '상하이', 'population': 241500000},
    {'rank': 2, 'city': '카리치', 'population': 341500000},
    {'rank': 3, 'city': '베이징', 'population': 441500000},
    {'rank': 4, 'city': '텐진', 'population': 541500000},
    {'rank': 5, 'city': '이스탄불', 'population': 641500000}
]

print(json.dumps(cities, ensure_ascii=False, indent=2)) #indent를 주면 줄바꿈 될 때마다 2개의 공백으로 들여쓰기 해준다.

with open('top_cities.json', 'w') as f:
    json.dump(cities, f) #파일에 저장할 때는 json.dump()함수를 사용한다.


# dumps는 dict > json
# loads는 json > dict

