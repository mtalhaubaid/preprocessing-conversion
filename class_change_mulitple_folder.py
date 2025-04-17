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

    print(f"\n[✓] Done processing files in folder: {folder_path}")
    print(f"    Total files processed : {total_files}")
    print(f"    Total lines updated   : {total_lines_updated}")
    print(f"    Total lines skipped   : {total_lines_skipped}")
    print("-" * 50)

    return {
        'folder': folder_path,
        'files': total_files,
        'updated': total_lines_updated,
        'skipped': total_lines_skipped
    }

def process_multiple_folders(folder_paths, desired_number):
    summary = []
    print("[*] Processing multiple folders...\n")

    for path in folder_paths:
        if os.path.isdir(path):
            stats = process_files_in_folder(path, desired_number)
            summary.append(stats)
        else:
            print(f"[X] Skipped invalid folder: {path}")

    print("\n\n[✓] All folders processed. Summary:\n")
    for s in summary:
        print(f"[✓] Done processing files in folder: {s['folder']}")
        print(f"    Total files processed : {s['files']}")
        print(f"    Total lines updated   : {s['updated']}")
        print(f"    Total lines skipped   : {s['skipped']}\n")

if __name__ == "__main__":
    # List of folders to process
    folder_paths = [
        r"D:\dataset\animal_uav\yolo training\test\labels",
        r"D:\dataset\animal_uav\yolo training\train\labels",
        r"D:\dataset\animal_uav\yolo training\valid\labels"
    ]


    desired_number = 2  # Set your desired number here

    process_multiple_folders(folder_paths, desired_number)
