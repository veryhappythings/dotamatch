import os.path


def get_key():
    key_path = os.path.expanduser("~/.steamapi")
    if os.path.exists(key_path):
        with open(key_path, 'r') as f:
            key = f.read().strip()
    else:
        key = raw_input("Enter Steam API key: ")
    return key
