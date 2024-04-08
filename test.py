# write some test code here
import threading
import time

s = "sql "
command, text = s.split(" ", 1)
print(command)
t = ("This", "is", "a", "test")
print(str(t))
def test():
    while True:
        print("here")
t = threading.Thread(target=test)
t.start()
t.join(10)