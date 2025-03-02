from bs4 import BeautifulSoup

def test_html_structure():
    html = "<html><head><title>Portal da Zeladoria</title></head><body><h1>Bem-vindo</h1></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    assert soup.title.string == "Portal da Zeladoria"
    assert soup.h1.string == "Bem-vindo"


#Isso verifica se o título da página e o <h1> estão corretos