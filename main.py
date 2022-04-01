from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import Edge
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

driver = Chrome()
timeout= 3
driver.get("https://www.tse.jus.br/eleitor/titulo-e-local-de-votacao/copy_of_consulta-por-nome")

try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="modal-lgpd"]/div/div/div[2]/button'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
   print("Tempo de espera para carregamento da página excedido.")

driver.implicitly_wait(3)
# CLIQUE PARA ACEITAR O COOKIE
driver.find_element(By.XPATH, '//*[@id="modal-lgpd"]/div/div/div[2]/button').click()

#CLIQUE PARA COLOCAR OS DADOS COMPLETOS E APERTAR EM ENTER
#driver.find_element(By.XPATH,'//*[@id="SE_NomeTituloCPF"]').send_keys('087952660817' + Keys.ENTER)

#CLIQUE PARA COLOCAR DE 3 EM 3 NÚMEROS NO PREENCHIMENTO
driver.find_element(By.XPATH,'//*[@id="SE_NomeTituloCPF"]').send_keys('087')
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="SE_NomeTituloCPF"]').send_keys('952')
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="SE_NomeTituloCPF"]').send_keys('660')
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="SE_NomeTituloCPF"]').send_keys('817')
driver.implicitly_wait(3)

#CLIQUE NO BOTÃO CONSULTAR
driver.find_element(By.XPATH,'//*[@id="consulta-situacao-eleitoral-form-submit"]').click()
driver.implicitly_wait(3)
#SEGUNDO CLIQUE NO BOTÃO CONSULTAR
driver.find_element(By.XPATH,'//*[@id="consulta-situacao-eleitoral-form-submit"]').click()




