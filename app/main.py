import sys
  
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
            case "type":
                typeBuiltin(command)
                
            case _: print(f"{command}: command not found")          

def echo(command):
    string = command.split()
    new_string = string[1:]
    string = " ".join(new_string)
    print(string) 
    # todo implement the other features         


def typeBuiltin(command):
    builtins = ["cd","echo", "exit", "ls" ,"rm","type"]
    string = command.split()
    if len(string) < 2:
        return
    for type in builtins:
        if string[1] == type:
            print(f'{type} is a shell builtin')
            return 
    print(f"{string[1]}: not found")    

if __name__ == "__main__":
    main()


