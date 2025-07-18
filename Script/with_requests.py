# ===================== BIBLIOTECAS
import requests
from bs4 import BeautifulSoup

# ===================== INFORMAÇÕES DE ACESSO

url = 'https://the-internet.herokuapp.com/authenticate'

def login_with_requests(usuario,senha):
    session = requests.Session()

    headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Dados de login
    payload = {
    'username': usuario,
    'password': senha
    }

    response = session.post(url, data=payload, headers=headers, verify=False)    # Envia POST request
    soup = BeautifulSoup(response.text, 'html.parser')

    alert = soup.find(id='flash')

    classes = alert.get('class', [])
    if 'success' in classes:
        return 'success'
    elif 'error' in classes:
        return 'error'
    else:
        return 'classnotidentified'