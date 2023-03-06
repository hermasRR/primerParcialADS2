from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    service = Service(executable_path="/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver # Asegurarse de que el driver está disponible globalmente
    driver.quit() # Cerrar el driver después de que se han ejecutado todas las pruebas

def test_envio_formulario(driver):
    # Abre la página principal de la aplicación web Flask
    driver.get('http://localhost:5000/')
    title = driver.title 
    print(title)

    # Encuentra el elemento de entrada de texto en la página y escribe algo en él
    codigo = driver.find_element(By.NAME, "codigo")
    nombre = driver.find_element(By.NAME, "nombre")
    carrera = driver.find_element(By.NAME, "carrera")

    codigo.send_keys('785')
    nombre.send_keys('Analisis y Diseño de Sistemas 2')
    carrera.send_keys('Ingenieria en Ciencias y Sistemas')
 
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    # Espera a que la página se cargue completamente
    driver.implicitly_wait(20)

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    
    assert value == "Datos Guardados" 

    assert '785' in driver.page_source
    assert 'Analisis y Diseño de Sistemas 2' in driver.page_source
    assert 'Ingenieria en Ciencias y Sistemas' in driver.page_source

def test_elemento_existe(driver):
    # Cargar la página web
    driver.get('http://localhost:5000/')

    codigo = driver.find_element(By.NAME, "codigo")
    nombre = driver.find_element(By.NAME, "nombre")
    carrera = driver.find_element(By.NAME, "carrera")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    assert codigo.is_displayed() 
    assert nombre.is_displayed()    
    assert carrera.is_displayed() 
    assert submit_button.is_displayed() 


def test_elemento_no_existe(driver):
    # Cargar la página web
    driver.get('http://localhost:5000/')

    # Intentar encontrar un elemento que no existe en la página
    non_existent_element = driver.find_element_by_css_selector('input[type="checkbox"]', 'input[type="radio"]')    
    # Esto debería generar un error, ya que el elemento no existe
    assert non_existent_element.is_displayed()  



    
