f = open('workfile', 'w', encoding="utf-8")

with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# we can check that the file is autmatically closed.
f.closed
f.close()
f.open('workfile', encoding="utf-8")
f.read()