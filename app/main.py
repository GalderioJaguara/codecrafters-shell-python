import sys
    


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        splited_command = command.split()
        if splited_command[0] == "exit":
            return
        print(f"{command}: command not found")

        

if __name__ == "__main__":
    main()


