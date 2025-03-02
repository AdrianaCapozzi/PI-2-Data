import requests

def test_get_requests():
    token = "https://orlok.pythonanywhere.com/api/v1/janitorial/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get("https://orlok.pythonanywhere.com/api/v1/janitorial/", headers=headers)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    assert response.status_code == 200

