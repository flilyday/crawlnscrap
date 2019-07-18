# csv로 저장하기

import csv

with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.writer(f) #1. csv모듈의 writer(파일)함수로 wrtier객체를 만들고
    writer.writerow(['rank', 'city', 'population']) #2. 객체.writerow혹은 객체.writerows매서드로 데이터를 쓴다.
    writer.writerows([
       [1, '상하이', 2415000],
       [2, '카리치', 3415000],
       [3, '베이징', 4415000],
       [4, '텐진', 5415000],
       [5, '이스탄불', 6415000],
    ])

