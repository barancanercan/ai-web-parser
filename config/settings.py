import os
from dotenv import load_dotenv

load_dotenv()

# oLLaMa Modeli:
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Chorme Driver:
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", os.path.join(os.getcwd(), "drivers","chromedriver"))

#Bright Data WebDriver Adress:
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
