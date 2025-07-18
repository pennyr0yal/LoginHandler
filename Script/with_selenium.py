# ===================== BIBLIOTECAS
import subprocess
import re
import os
import requests
import zipfile
import io
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import SessionNotCreatedException

# ===================== FUNÇÕES SELENIUM
def esperar_e_clicar(driver: webdriver,xpath_elemento: str,timeout: int = 30):
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath_elemento))).click()

def preencher_campo(driver: webdriver, xpath_elemento: str, preencher_com: str):
    driver.find_element(By.XPATH,xpath_elemento).send_keys(preencher_com)

def clicar_elemento(driver: webdriver, xpath_elemento: str):
    driver.find_element(By.XPATH, xpath_elemento).click()

# ===================== SCRIPT

url = 'https://the-internet.herokuapp.com/login'

def get_driver(silencio=True):
    options = webdriver.ChromeOptions()
    if silencio:   # Por padrão, a janela não será exibida enquanto o programa roda.
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chromedriver_path = 'C:/WebDrivers/chromedriver.exe'
    service = Service(executable_path=chromedriver_path)

    return webdriver.Chrome(service=service,options=options)

def update_chromedriver():
    def get_installed_chrome_version():
        try:
            output = subprocess.check_output(
                r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',shell=True).decode()
            version = re.search(r'(\d+\.\d+\.\d+\.\d+)', output)
            if version:
                return version.group(1)
        except Exception:
            raise Exception('Não foi possível detectar a versão do Chrome instalada.')

        # Checa se a pasta C:/WebDrivers precisa ser criada
        pasta_webdriver = 'C:/WebDrivers'
        if not os.path.exists(pasta_webdriver):
            os.mkdir(pasta_webdriver)

        chrome_version = get_installed_chrome_version()
        major_version = chrome_version.split('.')[0]

        # Acessa a página de downloads do Chrome
        url = 'https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json'
        resp = requests.get(url, verify=False)
        resp.raise_for_status()
        data = resp.json()

        # Localiza a versão mais reccente
        driver_url = None
        for version_info in data['versions']:
            if version_info['version'].startswith(major_version + '.'):
                for item in version_info.get('downloads', {}).get('chromedriver', []):
                    if item['platform'] == 'win32':
                        driver_url = item['url']
                        break
            if driver_url:
                break
        if not driver_url:
            raise Exception('Download do chromedriver para Windows x32 não encontrado.')

        # Efetua o download
        response = requests.get(driver_url, verify=False)
        response.raise_for_status()
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            for file in z.namelist():
                if 'chromedriver' in file.lower() and file.endswith('.exe'):
                    z.extract(file, pasta_webdriver)
                    src_path = os.path.join(pasta_webdriver, file)
                    final_path = os.path.join(pasta_webdriver, 'chromedriver.exe')
                    if src_path != final_path:
                        os.replace(src_path, final_path)
                    print('\r' + ' ' * 66, end='')
                    print('\rChromedriver atualizado!\n', end='', flush=True)
                    break
            else:
                raise Exception('chromedriver.exe not found in the ZIP archive')

def login_with_selenium(usuario,senha):
    try:
        driver = get_driver(False)
    except SessionNotCreatedException as e:
        try:
            print('\nChromedriver desatualizado ou inexistente, baixando atualização...', end='', flush=True)
            update_chromedriver()
            driver = get_driver()
        except SessionNotCreatedException as e:
            print('Atualize sua versão do navegador Google Chrome e tente novamente.')
            sys.exit(1)

    driver.get(url)
    esperar_e_clicar(driver,'//*[@id="username"]',60)
    preencher_campo(driver,'//*[@id="username"]',usuario)   # Preenche campo de usuário
    preencher_campo(driver,'//*[@id="password"]',senha)   # Preenche campo de senha
    clicar_elemento(driver,'//*[@id="login"]/button')   # Submete os dados de login

    # Identifica o alerta exibido na página após tentativa de login
    alert = driver.find_element(By.ID, 'flash')
    alert_class = alert.get_attribute('class')

    return alert_class