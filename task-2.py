#Write and append data to a file
data = input("Enter data to write to the file: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

print("Data successfully written to output.txt.")
additional_data = input("Enter additional data to append: ")

# Append data to the file
file = open("output.txt", "a")
file.write(additional_data + "\n")
file.close()

print("Data successfully appended.")

print("\nFinal content of output.txt:")

file = open("output.txt", "r")

for line in file:
    print(line.strip())

file.close()