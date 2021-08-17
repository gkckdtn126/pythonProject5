from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser") #html을 분석하겠다
#객체를 리턴 한다.
for location in soup.select("location"):
    print("도시 :",location.select_one("city").string)
    print("날씨 :",location.select_one("wf").string)