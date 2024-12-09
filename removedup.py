import os

def delete_extra_files(directory):
    # Dictionary to store files by their 8-character prefix
    prefix_dict = {}

    # Iterate through all files in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.jpg') and len(filename) > 20:
            prefix = filename[:20]  # Extract the 8-character prefix
            if prefix not in prefix_dict:
                prefix_dict[prefix] = []
            prefix_dict[prefix].append(filename)
    
    # Process each prefix group
    for prefix, files in prefix_dict.items():
        if len(files) > 2:  # If there are more than 2 files with the same prefix
            # Keep the first two files and delete the rest
            files_to_delete = files[2:]  # All files except the first two
            for file in files_to_delete:
                file_path = os.path.join(directory, file)
                try:
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

# Directory containing the .jpg files
directory_path = "./train6"

# Run the function
delete_extra_files(directory_path)
