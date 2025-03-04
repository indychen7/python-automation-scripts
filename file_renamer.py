import os

def rename_files(folder_path, prefix="file_", extension="txt"):
    files = os.listdir(folder_path)
    count = 1

    for file in files:
        old_path = os.path.join(folder_path, file)
        if os.path.isfile(old_path):  # Ignore directories
            new_name = f"{prefix}{count:03d}.{extension}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
            count += 1

# Example usage
if __name__ == "__main__":
    folder = input("Enter the folder path where files should be renamed: ")
    rename_files(folder)
