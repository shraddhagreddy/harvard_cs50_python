def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


#__name__ var whose value ="main" when u run from command line 
"""
we should not call it uncontionally like this
main()
"""
if __name__ == "__main__":
    main()