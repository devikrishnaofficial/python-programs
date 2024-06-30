def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found error.")
    except IOError:
       print("Error reading or writing file.")
source_file = "source.txt"  
destination_file = "destination.txt"  

copy_file(source_file, destination_file)
