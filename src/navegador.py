from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import PASTA_DOWNLOAD


def iniciar_navegador():
    PASTA_DOWNLOAD.mkdir(parents=True, exist_ok=True)

    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    prefs = {
        "download.default_directory": str(PASTA_DOWNLOAD),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(
        service=service,
        options=options
    )