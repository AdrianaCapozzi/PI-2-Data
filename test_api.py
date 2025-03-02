import requests

BASE_URL = "https://orlok.pythonanywhere.com/api/v1/janitorial/"

def test_get_requests():
    response = requests.get(BASE_URL)
    assert response.status_code == 200  
    assert isinstance(response.json(), list)  

if __name__ == "__main__":
    test_get_requests()
    print("Todos os testes passaram!")
