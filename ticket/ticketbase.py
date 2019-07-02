from abc import ABCMeta
from abc import abstractmethod
from pathlib import Path
import platform

from selenium import webdriver


class TicketBase(metaclass=ABCMeta):
    def __init__(self, config):
        self.config = config
        self.driver = self.init_driver()
        pass

    def init_driver(self):
        driver_path = None
        if platform.system() == "Windows":
            driver_path = Path("./chromedriver.exe")
        if platform.system() == "Linux" or platform.system() == "Darwin":
            driver_path = Path("./chromedriver")
        if not driver_path.exists():
            raise FileNotFoundError("Chrome Driver was not found.")
        return webdriver.Chrome(str(driver_path.absolute()))

    @abstractmethod
    def exectue(): pass
