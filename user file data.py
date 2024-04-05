def main():
    user_input = input("Enter text to write to output.txt: ")

    with open("output.txt", "w") as file:
        file.write(user_input)

    print("User input has been written to output.txt.")

if __name__ == "__main__":
    main()
