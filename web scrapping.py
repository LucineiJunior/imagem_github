import requests

#o beaultiful soup extrai os dados de arquivos html ou xml
from bs4 import BeautifulSoup as bs

github_user = input('Usuario do Github: ')
url = 'https://github.com/' + github_user
requisicao = requests.get(url)
soup = bs(requisicao.content, 'html.parser') #html parcer é o navegador
#aqui é selecionado exatamente a imagem de perfil pelo inspecionar
imagem_perfil = soup.find('img', {'alt': 'Avatar'})['src']

print(imagem_perfil)
