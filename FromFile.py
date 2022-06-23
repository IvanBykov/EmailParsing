from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector
import quopri

from decoder import decode_str

with open('source_file.eml', 'r', encoding='UTF-8') as in_file:
    #print(in_file.read())
    file_text = in_file.read()
#print(file_text)
soup = BeautifulSoup(file_text, 'lxml')
# print(soup)
data = soup.find('table', class_='3D"w95"')
#print(data)
data.f
name = data.find_all('td', class_='3D"font12"')
for i in name:
    print(decode_str(i.text))
#print(decode_str(name))
#name = data.find_all('td', class_='3D"font15"')
#print(decode_str(name[0].text))
#print(decode_str(name[1].text))
#print(decode_str(name[2].text))
