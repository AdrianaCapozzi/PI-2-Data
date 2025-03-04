from bs4 import BeautifulSoup

def test_html_title():
    html = "<html><head><title>Portal da Zeladoria</title></head><body></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    
    assert soup.title is not None, "O documento HTML não tem um título!"
    assert soup.title.string.strip() == "Portal da Zeladoria", "O título da página está incorreto!"

#testa se o título está escrito dentro do esperado