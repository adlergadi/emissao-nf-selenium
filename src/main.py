from navegador import iniciar_navegador
from login import realizar_login
from planilha import carregar_clientes
from emissor import emitir_notas


def main():

    driver = iniciar_navegador()

    try:
        realizar_login(driver)

        clientes = carregar_clientes()

        emitir_notas(driver, clientes)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()