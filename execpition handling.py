try:
    x = int(input())
    if x < 20:
        raise Exception("Entered number below 20")
    t=x*5
    print(t)
except:
    print("ERROR  HANDLING ")