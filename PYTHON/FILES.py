import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

def write_text_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
            print(f"Text written to {file_path}")
    except IOError as e:
        print(f"An error occurred: {e}")

def read_file_stream(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

def read_random_access(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

def read_file_at_index(file_path, index):
    try:
        with open(file_path, 'r') as file:
            file.seek(index)
            print(file.read())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred: {e}")

def check_file_permissions(file_path):
    if os.path.exists(file_path):
        read_permission = os.access(file_path, os.R_OK)
        write_permission = os.access(file_path, os.W_OK)
        print(f"Read permission: {'Yes' if read_permission else 'No'}")
        print(f"Write permission: {'Yes' if write_permission else 'No'}")
    else:
        print(f"The file {file_path} does not exist.")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Read a text file")
        print("2. Write text to a .txt file")
        print("3. Read a file stream")
        print("4. Read a file stream supporting random access")
        print("5. Read a file at a particular index using seek()")
        print("6. Check file read and write access permissions")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the file path: ")
            read_text_file(file_path)
        elif choice == '2':
            file_path = input("Enter the file path: ")
            text = input("Enter the text to write: ")
            write_text_file(file_path, text)
        elif choice == '3':
            file_path = input("Enter the file path: ")
            read_file_stream(file_path)
        elif choice == '4':
            file_path = input("Enter the file path: ")
            read_random_access(file_path)
        elif choice == '5':
            file_path = input("Enter the file path: ")
            index = int(input("Enter the index to seek to: "))
            read_file_at_index(file_path, index)
        elif choice == '6':
            file_path = input("Enter the file path: ")
            check_file_permissions(file_path)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
