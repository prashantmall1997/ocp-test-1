import time

count = 0
while True:
    print("Hello World!")
    time.sleep(5)
    print("Goodbye World!")

    count += 1
    if count == 1:
        break