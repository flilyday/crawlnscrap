# 웹페이지 헤더에서 인코딩 값을 가져오고, 없을 시에 기본값을 utf-8로 지정
import sys
from urllib.request import urlopen
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

#이 세줄이 핵심
print(f.info())
encoding = f.info().get_content_charset(failobj='utf-8')
text = f.read().decode(encoding)

print(text)