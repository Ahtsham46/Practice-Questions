def copy_file_data(source,destination):
    try:
        with open(source, "r") as src:
            data = src.read()
        with open(destination, 'w') as dest:
            dest.write(data)
            print(f"Data copied from {source} to {destination} successfully.")
    except FileNotFoundError:
        print(f"Error: {source} not found.")
    except IOError:
        print("Error: An I/O error occurred while handling the file.")
source = "practice.txt"
destination = "copy.txt"
copy_file_data(source, destination)