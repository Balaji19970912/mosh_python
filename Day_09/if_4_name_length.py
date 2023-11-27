name = "Monkey D Luffy"
name_len = len(name)

if name_len > 3 and name_len <= 50:
    print("Name length is valid!")
elif name_len < 3:
    print("Name length should be 3 or more characters!")
else:
    print("Name length should be under 3 to 50 characters!")
print(name_len)