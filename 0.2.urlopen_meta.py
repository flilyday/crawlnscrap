import re
import sys
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read()
#일단 바이트 코드로 읽어서 저장해 놓는다.
scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
# 캐릭터셋은 html본문 앞에 저장해 놓는 경우가 많으므로 응답 본문 1024자를 일단 ascii문자로 디코딩 해둔다. ascii는 최소한의 charset

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1) #인코딩 값이 명시되 있으면 추출한 값을 적용
else:
    encoding = 'utf-8'

print('encoding: ', encoding, file=sys.stderr)

text = bytes_content.decode(encoding)
print(text)