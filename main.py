from controllers.botcontroller import createBotController
import time

if __name__ == "__main__":
    bc = createBotController()
    bc.start()
    while True:
        time.sleep(5)