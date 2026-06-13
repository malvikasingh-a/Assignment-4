# Task 2: File Handling in Python
data = input("Enter data to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data successfully written to output.txt.")

# Append additional data to the file
additional_data = input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("Data successfully appended.")

print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())