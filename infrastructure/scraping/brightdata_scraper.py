from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common.by import By

from config.settings import SBR_WEBDRIVER
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

def scrape_with_brightdata(url: str, detect_timeout: int=1000) -> str:
    print("[BrightDataScraper] Connecting to BrightDataScraper Browser...]")

    connetion = ChromeRemoteConnection(SBR_WEBDRIVER, "goog","chrome")
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-dev-shm-usage")

    with Remote(command_executor= connetion, options=options) as driver:
        driver.get(url=url)
        print(f"[BrightDataScraper] waiting for CAPTCHA solve...")

        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": detect_timeout},
            },
        )

        print("Captcha solve status:", solve_res["value"]["status"])
        return driver.page_source