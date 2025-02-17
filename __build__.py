# __build__.py

import os
import subprocess
import sys

def run_exec_script():
    src_folder = 'src'
    script_name = 'exec.py'
    script_path = os.path.join(src_folder, script_name)

    if not os.path.isdir(src_folder):
        print(f"Error: The folder '{src_folder}' does not exist.")
        return
    if not os.path.isfile(script_path):
        print(f"Error: The script '{script_name}' does not exist in the '{src_folder}' folder.")
        return

    try:
        subprocess.run(['python', script_path], check=True)
        print(f"Successfully ran '{script_name}' from '{src_folder}'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    run_exec_script()
    sys.exit()
