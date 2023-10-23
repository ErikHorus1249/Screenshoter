import time
from utils.screenshoter import Screenshoter
from utils.log import Logger


if __name__ == "__main__":
    while True:
        scr = Screenshoter(Logger(), "admin", "****", "https://test.com")
        scr.take_photo()
        time.sleep(3)