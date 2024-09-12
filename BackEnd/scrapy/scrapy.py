#    biblioteca de controle da pagina chrome
from selenium import webdriver
#    biblioteca para simular teclas 
from selenium.webdriver.common.keys import Keys
#    biblioteca para iniciar a o chrome 
from selenium.webdriver.chrome.service import Service
#    biblioteca para localizar elementos na pagina 
from selenium.webdriver.common.by import By
# biblioteca para controlar o tempo de tela 
import time
# download do driver 
from webdriver_manager.chrome import ChromeDriverManager

# instalando o chromedriver 
service = Service(ChromeDriverManager().install())

# Inicialize o WebDriver com a instância de Service
driver = webdriver.Chrome(service=service)

# Acessar o Google Maps
driver.get('https://www.google.com/maps')

# Simulação de pesquisa de local
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Bar')
search_box.send_keys(Keys.RETURN)

time.sleep(20)  # Aguarde o carregamento da página

# Extração de dados (exemplo simplificado)
businesses = driver.find_elements(By.CLASS_NAME, 'hfpxzc')
for business in businesses:
    try:
        name = business.get_attribute('aria-label')
        print(name)
    except Exception as e:
        print(f"Error extracting name: {e}")

# Fechar o navegador
driver.quit()

