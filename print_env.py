import os
import argparse

def write_environment_details(code_path):
    # Open file to write
    with open("_my_code.txt", "w") as file:
        # Writing the overview section
        file.write("OVERVIEW:\n")
        file.write("This document provides a description of the programming environment ")
        file.write("for a Python application. It includes sections detailing the current ")
        file.write("working directory, lists each file within the directory, and presents ")
        file.write("the name and contents of each relevant code file. The purpose of this ")
        file.write("document is to thoroughly explain the application's code base as it ")
        file.write("currently stands, serving as a foundation for understanding and ")
        file.write("further developing the code in a consistent and structured manner, ")
        file.write("building upon the existing base.\n")
        file.write("###########################\n\n")

        # Use provided code directory
        cwd = code_path
        file.write(f"Current Working Directory: {cwd}\n")
        file.write("###########################\n\n")

        # List all files in the provided code directory
        for filename in os.listdir(cwd):
            if filename.endswith(('.py', '.js', '.html')):
                file.write("###########################\n")
                file.write(f"Code file: {filename}\n")
                file.write("###########################\n")
                
                # Read and write the contents of the file
                with open(os.path.join(cwd, filename), 'r') as f:
                    contents = f.read()
                    file.write(f"Contents of {filename}:\n{contents}\n\n")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Generate a document with the code environment details.")
    parser.add_argument('--code-path', type=str, required=True, help="The path to the code directory")

    # Parse arguments
    args = parser.parse_args()

    # Call the function with provided code directory
    write_environment_details(args.code_path)

if __name__ == "__main__":
    main()