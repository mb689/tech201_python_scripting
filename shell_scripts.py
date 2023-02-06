import os, subprocess

# Pythong doesn't actually run shell commands
# Instead we can use Python to run shell script files

script_dir = os.path.dirname(__file__)

script_absolute_path = os.path.join(script_dir + "script.sh")

subprocess.call(['sh', script_absolute_path])