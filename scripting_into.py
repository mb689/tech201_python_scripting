# Scripting

# Shorter pieces of code that allow us to do things we would otherwise have to do manually
# Unlike programs, scripts are one file and do not need to be compiled
# API's tend to use scripts

# Scripts use less or no abstraction and are not as flexible as programs. But they are much easier to read and write.

# Scripts almost always written in 'high level' languages (easy to read) - Python, Bash, Ruby

# Why is python?

# Open Source
# Many libraries
# Easy to understand
# Large community
# Language interoperability (can talk to other languages, OS's and softwares)


# Why is Scripting important for DevOps engineers?

# Automation -> Of mundane tasks

# 7 core modules in python:

# OS
# Sys
# Subprocesses
# DateTime
# JSON
# Random
# Math

# Sys module script
import sys

print(sys.version)

# OS module script
import os

print(os.getcwd())

# Subprocess module script
# Can be used to create and interact with subprocess being managed by our Python interpreter.
import subprocess

subprocess.run(["python", "hello_world.py"])

# Math module script
import math

pi = math.pi
pi_string = str(pi)
print(f"The value of pi is {pi_string}")

# Random module script
import random

random = random.randrange(1, 10)
print(random)

# DateTime module script
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module script
import json

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(y)
