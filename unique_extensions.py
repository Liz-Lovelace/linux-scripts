#!/bin/python3
import os

# Set to store unique file extensions
unique_extensions = set()

# Recursive function to walk through the directory
def find_unique_file_extensions(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            # Split the extension from the file
            _, ext = os.path.splitext(file)
            if ext:  # Check if there is an extension
                unique_extensions.add(ext)

# Start the search from the current directory
find_unique_file_extensions('.')

# Output the unique file extensions
for ext in sorted(unique_extensions):
    print(ext)

