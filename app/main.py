import sys


def command():
    sys.stdout.write("$ ")
    command = input()
    print(f"{command}: command not found")

def main():
    while True:
        command()


if __name__ == "__main__":
    main()


