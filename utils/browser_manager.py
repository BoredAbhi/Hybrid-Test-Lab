from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import os

class BrowserManager:

    @staticmethod
    def get_driver(browser="chrome"):
        """
        Initialize and return the appropriate WebDriver instance.
        """
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # Add any desired Chrome options here
            options.add_argument("--headless")  # Optional: headless mode for CI
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            # Add any desired Firefox options here
            options.add_argument("--headless")  # Optional: headless mode for CI
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Optional: Set browser window size for consistent screenshots or testing
        driver.set_window_size(1920, 1080)

        return driver

    @staticmethod
    def close_driver(driver):
        """
        Close the browser window and quit the driver.
        """
        if driver:
            driver.quit()
