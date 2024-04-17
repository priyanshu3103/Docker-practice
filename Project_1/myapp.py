
try:
    # Open the file in write mode
    with open('servers.txt', 'w') as file:
        # Take input from the user
        num_servers = int(input("Enter the number: "))
        
        # Write content to the file based on user input
        for i in range(1, num_servers + 1):
            data = input(f"Enter name  {i}: ")
            file.write(data + "\n")
except Exception as e:
    # Handle exceptions
    print(e, type(e))
else:
    print("Content written to file successfully.")
try:
    with open('servers.txt', 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    print("Content of the file ")
    for line in content:
        print(f'{line.rstrip()}')
