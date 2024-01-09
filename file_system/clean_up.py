with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup("Encountered some issues", excs)

f()

try:
    f()
except Exception as e:
    print(f"caught {type(e)}: e")