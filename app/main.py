import sys

def echo(command):
    string = command.split()
    new_string = string[1:]
    string = " ".join(new_string)
    print(string) 
    # todo implement the other features   


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        splited_command = command.split()

        #commands actions
        match splited_command[0]:
            case "exit":
                return
            case "echo":
                echo(command)
            case _: print(f"{command}: command not found")          

        

if __name__ == "__main__":
    main()


