from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def preencher_campo(driver, nome_campo, valor):
    campo = driver.find_element(By.NAME, nome_campo)
    campo.clear()
    campo.send_keys(str(valor))

def selecionar_uf(driver, uf):
    campo_uf = Select(driver.find_element(By.NAME, "uf"))
    campo_uf.select_by_value(str(uf).strip().upper())

def emitir_notas(driver, clientes):
    wait = WebDriverWait(driver, 10)

    for _, cliente in clientes.iterrows():
        try:
            wait.until(
                EC.presence_of_element_located((By.NAME, "nome"))
            )

            preencher_campo(driver, "nome", cliente["Cliente"])
            preencher_campo(driver, "endereco", cliente["Endereço"])
            preencher_campo(driver, "bairro", cliente["Bairro"])
            preencher_campo(driver, "municipio", cliente["Municipio"])
            preencher_campo(driver, "cep", cliente["CEP"])

            selecionar_uf(driver, cliente["UF"])
            
            preencher_campo(driver, "cnpj", cliente["CPF/CNPJ"])
            preencher_campo(driver, "inscricao", cliente["Inscricao Estadual"])
            preencher_campo(driver, "descricao", cliente["Descrição"])
            preencher_campo(driver, "quantidade", cliente["Quantidade"])
            preencher_campo(driver, "valor_unitario", cliente["Valor Unitario"])
            preencher_campo(driver, "total", cliente["Valor Total"])

            driver.find_element(By.CSS_SELECTOR, "button.registerbtn").click()

            print(f"Nota emitida para {cliente['Cliente']}")

        except Exception as erro:
            print(f"Erro ao emitir nota para {cliente['Cliente']}: {erro}")