import os

def warn(message):
    raise Exception(f"[WARNING]: {message}")

def print_function(*args):
    print(*args)

def error(message):
    raise Exception(f"[ERROR]: {message}")

def read_file(file_path):
    if not os.path.isfile(file_path):
        error(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return file.read()

def hook_meta_method(table, method_name, new_function):
    original_method = getattr(table, method_name, None)
    if original_method is None:
        error(f"Method '{method_name}' does not exist.")
    
    def hooked_method(*args, **kwargs):
        return new_function(original_method, *args, **kwargs)
    
    setattr(table, method_name, hooked_method)

def print_identity(value):
    return id(value)

def get_raw_meta_table(obj):
    return obj.__class__

def read_game_url(game_id):
    return f"https://www.roblox.com/games/{game_id}"
