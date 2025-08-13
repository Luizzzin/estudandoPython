a = 5
b = 10
print(f"A:{a}, B:{b}")

temp = a
a = b
b = temp

print(f"A:{a}, B:{b}")

a, b = b, a
print(f"A:{a}, B:{b}")

addr = "rm562399@gmail.com"
uname, domain = addr.split("@")
print(uname)
print(domain)