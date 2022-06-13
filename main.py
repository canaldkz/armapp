import sys
from threading import Thread
from webapp import app
import webview
from localization import russian_localization

SERVER_HOST = "127.0.0.1"
PORT = "8765"


if __name__ == "__main__":
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

    webview.start(gui="mshtml", localization=russian_localization, debug=True)
    sys.exit(0)
