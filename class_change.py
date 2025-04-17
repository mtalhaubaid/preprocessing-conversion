# Modifies text files in a controlled manner, replacing the first element in each line.
# Assumes the first element is separated by a space from the rest of the line.
# Warns about potential data loss as the original content is overwritten



# import os

# def replace_first_element(file_path, desired_number):
#     # Read the content of the file
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     # Modify each line by replacing the first element
#     modified_lines = [f"{desired_number} {line.split(' ', 1)[1]}" for line in lines]

#     # Write the modified content back to the file
#     with open(file_path, 'w') as file:
#         file.writelines(modified_lines)

# def process_files_in_folder(folder_path, desired_number):
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".txt"):
#             file_path = os.path.join(folder_path, filename)
#             replace_first_element(file_path, desired_number)

# if __name__ == "__main__":
#     folder_path = r"D:\dataset\animals_uav\yolo training\valid\labels"  # Replace this with the path to your folder
#     desired_number = 0  # Replace this with the desired number

#     process_files_in_folder(folder_path, desired_number)




import os

def replace_first_element(file_path, desired_number):
    updated_lines = 0
    skipped_lines = 0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            if ' ' in line:
                modified_lines.append(f"{desired_number} {line.split(' ', 1)[1]}")
                updated_lines += 1
            else:
                print(f"[!] Skipped line in {file_path} (no space found): '{line.strip()}'")
                skipped_lines += 1

        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        return updated_lines, skipped_lines

    except Exception as e:
        print(f"[X] Error processing '{file_path}': {e}")
        return 0, 0

def process_files_in_folder(folder_path, desired_number):
    total_files = 0
    total_lines_updated = 0
    total_lines_skipped = 0

    print(f"\n[+] Starting processing of text files in: {folder_path}\n")

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            total_files += 1
            file_path = os.path.join(folder_path, filename)
            print(f"[*] Processing file: {filename}")
            updated, skipped = replace_first_element(file_path, desired_number)
            print(f"    -> Lines updated: {updated}, Skipped: {skipped}")
            total_lines_updated += updated
            total_lines_skipped += skipped

    print("\n[✓] Done processing files.")
    print(f"    Total files processed : {total_files}")
    print(f"    Total lines updated   : {total_lines_updated}")
    print(f"    Total lines skipped   : {total_lines_skipped}")

if __name__ == "__main__":
    folder_path = r"D:\dataset\weapon\custom\labels"  # Update if needed
    desired_number = 0  # Update if needed

    process_files_in_folder(folder_path, desired_number)
