from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector
import quopri

from decoder import decode_str

with open('source_file1.eml', 'r', encoding='UTF-8') as in_file:
    #print(in_file.read())
    file_text = in_file.read()
#print(file_text)
soup = BeautifulSoup(file_text, 'lxml')
# print(soup)
data = soup.find('table', class_='3D"w95"')
#print(data)
#data.f
rows = data.find_all('tr')
counter = 0
for i in rows:
    print(f'string # {counter}')
    counter += 1
    print(decode_str(i.text))
#name = data.find_all('td', class_='3D"font12"')
#counter = 0
#for i in name:
#    print(counter)
#    counter += 1
#    print(decode_str(i.text))
#
#digits = data.find_all('td', class_='3D"font15"')
#counter = 0
#for i in digits:
#    print(counter)
#    counter += 1
#    print(decode_str(i.text))
