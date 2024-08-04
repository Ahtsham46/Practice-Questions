def copy_file(source, destination):
    try:
        with open(source, 'r') as src:
            data = src.read()
        with open(destination, 'w') as dest:
            dest.write(data)
        print(f"Data copied from {source} to {destination} successfully.")
    except FileNotFoundError:
        print(f"Error: {source} not found.")
    except IOError:
        print("Error: An I/O error occurred while handling the file.")
source = 'practice1.txt'
destination = 'destination.txt'
copy_file(source, destination)
file = open("practice1.txt", "a+")
file.write("Ahtsham is best friend of ALi")
file.close()
f = open("destination.txt", "r")
for each in f:
    print(each, end=" ")
f.close()