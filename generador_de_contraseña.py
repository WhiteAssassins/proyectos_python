import secrets
import tkinter as tk 

##class PasswordGenerator:
v = 10
k = secrets.token_hex(16)
print("".join((secrets.choice(k) for i in range(v))))