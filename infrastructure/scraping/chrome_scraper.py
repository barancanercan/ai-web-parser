import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.settings import CHROMEDRIVER_PATH

def srape_with_chreme(url: str, wait_time: int=5) -> str:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"[ChromeScraper] Navigating to {url} ...")
        driver.get(url)
        time.sleep(wait_time)
        return  driver.page_source
    finally:
        driver.quit()
