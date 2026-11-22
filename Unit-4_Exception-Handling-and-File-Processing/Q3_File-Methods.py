# Q3. File Methods and Exception Handling

filename = input("Enter the name of an existing text file (for example student.txt): ")

try:
    file = open(filename, "r", encoding="utf-8")
    print("File name:", file.name)
    print("File mode:", file.mode)

    print("\nread() - complete contents:")
    print(file.read())

    print("\nCurrent position after read():", file.tell())

    file.seek(0)
    print("\nreadline() - first line:")
    print(file.readline())
    print("Position after readline():", file.tell())

    file.seek(0)
    print("\nreadlines() - all lines as a list:")
    print(file.readlines())

except FileNotFoundError:
    print("Error: The requested file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except OSError as error:
    print("File operation error:", error)
else:
    print("\nFile operations completed successfully.")
finally:
    # Close the file if it was successfully opened.
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("No file was opened, so there is no file to close.")
