from urllib.request import urlopen

f = urlopen('http://hanbit.co.kr')
print(type(f))  #urlopen은 httpResponse객체를 반환한다.
print(f.status)
print(f.read()) #read()는 바이트코드를 반환한다
print(f.getheader('Content-Type'))

