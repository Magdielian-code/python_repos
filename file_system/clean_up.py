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
    print(f"caught {type(e)}: e"
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

tests = [1,2,3,4,]
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)



# Enriching exceptions with notes

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

)
