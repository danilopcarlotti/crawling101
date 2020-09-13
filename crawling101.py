from bs4 import BeautifulSoup
import time
import urllib.request

def baixa_arquivo(link,nome_arq):
    response = urllib.request.urlopen(link,timeout=20)
    arq_final = open(nome_arq, 'wb')
    arq_final.write(response.read())
    time.sleep(1)
    arq_final.close()

# Exemplo/
# baixa_arquivo('https://ww2.stj.jus.br/docs_internet/processo/dje/zip/stj_dje_20200908.zip','/home/danilo/Desktop/diario_stj.zip')

def encontrar_links_html(link):
    req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req,timeout=30).read()
    pag = BeautifulSoup(html,'html.parser')
    links = []
    for l in pag.find_all('a', href=True):
        links.append(l['href'])
    return links

# Exemplo
# print(encontrar_links_html('https://www.wikipedia.org/'))