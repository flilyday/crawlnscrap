import sqlite3

conn = sqlite3.connect('top_cities.db') #파일을 열고 연결을 변수에 지정
c = conn.cursor() #커서를 추출
c.execute('DROP TABLE IF EXISTS cities') #테이블이 존재하는 경우에 제거
c.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
    ''') #테이블 생성
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 2415000))
# SQL내부에서 파라미터로 변경할 부분은 ?로 지정한다.

c.execute('INSERT INTO cities VALUES (:rank, :city, :population)', {'rank':2, 'city':'카라치', 'population':3415000})
# 파라미터가 딕셔너리일 때는 플레이스 홀더를 :<이름> 형태로 지정한다.

c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': '베이징', 'population': 441500000},
    {'rank': 4, 'city': '텐진', 'population': 541500000},
    {'rank': 5, 'city': '이스탄불', 'population': 641500000}
])
# executemany() 매서드를 사용하면 여러개의 파라미터를 지정해서 SQL구문을 실행할 수 있다.

conn.commit() #바뀐 부분을 커밋

c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

conn.close() #객체를 닫는다.