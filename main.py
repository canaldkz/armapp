import sys
from threading import Thread
from webapp import app
import webview
from winotify import Notification
from localization import russian_localization

SERVER_HOST = "127.0.0.1"
PORT = "8765"

toast = Notification(app_id="Arm App",
                     title="Запуск",
                     msg="Добро пожаловать!")

def run():
    server_thread = Thread(
        target=app.run, kwargs={"host": SERVER_HOST, "port": PORT}, daemon=True
    )
    server_thread.start()
    main_window = webview.create_window(
        "ARMApp",
        f"http://127.0.0.1:{PORT}",
        min_size=(800, 600),
        text_select=True,
        easy_drag=False,
        background_color="#63c",
        confirm_close=True,
    )
    toast.show()
    webview.start(gui="mshtml", localization=russian_localization, debug=False)
    sys.exit(0)


if __name__ == "__main__":
    run()
