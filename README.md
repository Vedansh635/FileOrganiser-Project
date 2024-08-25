# Project-Description

- This Python script is a simple file organizer that renames files in a specified directory to a sequential numbering format.

# How it works:

1. The script takes two parameters: file_path and file_type. <br>
2. It lists all files in the specified file_path directory using os.listdir(). <br>
3. It then iterates through the list of files and renames each file to a sequential numbering format, e.g., 1.txt, 2.txt, 3.txt, etc. <br>
4. The file_type parameter specifies the file extension to be used for the renamed files. <br>


# Example:

If you have a directory `test_folder` containing files file1.txt, file2.txt, file3.txt, etc., running the script with the command organisefile('test_folder', 'txt') will rename the files to 1.txt, 2.txt, 3.txt, etc.
