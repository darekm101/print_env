import os
import argparse

def write_environment_details(code_path):
    # Open file to write
    with open("_my_code.txt", "w") as file:
        # Writing the overview section
        file.write("OVERVIEW:\n")
        file.write("This document provides a description of the sybase database environment")
        file.write("If influes store procedurex, schema, queries, etc. ")
        file.write("The text file  lists each file within the directory, and presents ")
        file.write("the name and contents of each relevant database description file. The purpose of this ")
        file.write("document is to thoroughly explain the Sybase Schmea and queries as it ")
        file.write("currently stands, serving as a foundation for understanding and ")
        file.write("further developing qureies or stored procedures in a consistent and structured manner, ")
        file.write("building upon the existing base.\n")
        file.write("###########################\n\n")

        # Use provided code directory
        cwd = code_path
        file.write(f"Current Working Directory: {cwd}\n")
        file.write("###########################\n\n")

        # List all files in the provided code directory
        for filename in os.listdir(cwd):
            if filename.endswith(('.txt', '.py')):
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