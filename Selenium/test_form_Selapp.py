from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless') # Ejecutar el navegador en modo headless (sin interfaz gráfica)
    #driver = webdriver.Chrome(options=options)
    
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver # Asegurarse de que el driver está disponible globalmente
    driver.quit() # Cerrar el driver después de que se han ejecutado todas las pruebas

def test_envio_formulario(driver):
    # Abre la página principal de la aplicación web Flask
    driver.get('http://localhost:5000/')
    title = driver.title 
    print(title)

    # Encuentra el elemento de entrada de texto en la página y escribe algo en él
    nombre = driver.find_element(By.NAME, "nombre")
    apellido = driver.find_element(By.NAME, "apellido")
    fecha_nacimiento = driver.find_element(By.NAME, "fecha_nacimiento")
    edad = driver.find_element(By.NAME, "edad")

    nombre.send_keys('Hermas')
    apellido.send_keys('Ramirez')
    fecha_nacimiento .send_keys('01-03-2000')
    edad.send_keys('22')

    #nombre.send_keys(Keys.RETURN)
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    # Espera a que la página se cargue completamente
    driver.implicitly_wait(20)

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    
    assert value == "Datos Guardados" 

    assert 'Hermas' in driver.page_source
    assert 'Ramirez' in driver.page_source
    assert '2000-03-01' in driver.page_source
    assert '22' in driver.page_source

def test_elemento_existe(driver):
    # Cargar la página web
    driver.get('http://localhost:5000/')

    nombre = driver.find_element(By.NAME, "nombre")
    apellido = driver.find_element(By.NAME, "apellido")
    fecha_nacimiento = driver.find_element(By.NAME, "fecha_nacimiento")
    edad = driver.find_element(By.NAME, "edad")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    assert nombre.is_displayed()   
    assert apellido.is_displayed() 
    assert fecha_nacimiento .is_displayed() 
    assert edad .is_displayed() 
    assert submit_button.is_displayed() 

def test_elemento_no_existe(driver):
    # Cargar la página web
    driver.get('http://localhost:5000/')

    # Intentar encontrar un elemento que no existe en la página
    non_existent_element = driver.find_element_by_css_selector('input[type="checkbox"]', 'input[type="radio"]')    
    # Esto debería generar un error, ya que el elemento no existe
    assert non_existent_element.is_displayed()    



    
