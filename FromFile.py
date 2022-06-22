from bs4 import BeautifulSoup

with open('source_file.eml', 'r', encoding='utf-8') as in_file:
    #print(in_file.read())
    file_text = in_file.read()
#print(file_text)
soup = BeautifulSoup(file_text, 'lxml')
# print(soup)
data = soup.find('td')
#data = soup.find("td")
print(data)


