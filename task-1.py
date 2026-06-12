#Read a file and handle errors
try:
    file = open("sample.txt", "r")

    print("Reading file content:")

    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")