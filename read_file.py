def read_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    filename = "example.txt"  # replace with your file name
    read_file(filename)
