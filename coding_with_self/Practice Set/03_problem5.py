import os

# Function to list directory contents
def list_directory_contents(directory_path):
    try:
        # Get list of files and directories in the specified path
        contents = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the directory path (change as needed)
    path = input("Enter the directory path: ")
    list_directory_contents(path)

