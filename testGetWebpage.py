import urllib.request
from bs4 import BeautifulSoup


with urllib.request.urlopen(
    "https://dho.inven.co.kr/dataninfo2/areacity/list.php?sname=%EB%A6%AC%EC%8A%A4%EB%B3%B8"
) as response:
    soup = BeautifulSoup(response.content, "html.parser")
    the_page = response.read()
    # print(the_page)
    table = soup.find("javascript", {})
# javascript:DHO.Db.viewAreaCity(2, '');
# urllib.parse.urlencode