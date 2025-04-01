# from .fixtures import api_client

# def test_cliente_realiza_pedido(api_client, live_server):
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     import time

#     #Configurar el navegador
#     driver = webdriver.Chrome()
    
#     driver.get(f'{live_server.url}/api/v1/productos')

#     try:
#         #Simular navegación
#         driver.find_element(By.CLASS_NAME, 'producto-item').click()
#         time.sleep(1)

#         #Añadir al carrito
#         driver.find_element(By.ID, 'btn-agregar').click()
#         time.sleep(1)

#         #Ir al checkout
#         driver.find_element(By.ID, "btn-checkout").click()
#         time.sleep(1)

#         #Completa el formulario
#         driver.find_element(By.ID, "btn-confirmar").click()
#         time.sleep(1)

#         # Verificar mensaje éxito
#         mensaje = driver.find_element(By.CLASS_NAME, "mensaje-exito").text
#         assert "Pedido realizado con éxito" in mensaje
#     finally:
#         driver.quit()


