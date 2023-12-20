import os
import argparse

def create_text_file(root_folder):
    # Output file name
    output_file = "data/test_data_list.txt"

    with open(output_file, 'w') as file:
        # Iterate over subfolders in the main folder
        for subfolder_name in sorted(os.listdir(root_folder)):
            subfolder_path = os.path.join(root_folder, subfolder_name)

            # Check if the item in the main folder is a subfolder
            if os.path.isdir(subfolder_path):
                # Iterate over sub-subfolders in each subfolder
                for subsubfolder_name in sorted(os.listdir(subfolder_path)):
                    if not ".DS_Store" in subsubfolder_name:
                        subsubfolder_path = os.path.join(subfolder_path, subsubfolder_name)

                        # Check if the item in the subfolder is a sub-subfolder
                        if os.path.isdir(subsubfolder_path):
                            # Find all WAV files in the sub-subfolder
                            wav_files = [file for file in os.listdir(subsubfolder_path) if file.endswith(".flac")]

                            # Write to the output file
                            for wav_file in wav_files:
                                id_name = subfolder_name
                                wav_path = os.path.join(subsubfolder_path, wav_file)
                                file.write(f"{id_name}\t{wav_path}\n")

    print(f"Output file '{output_file}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description="Create a text file with folder IDs and WAV file paths.")
    parser.add_argument("--main_folder", help="Path to the main folder containing subfolders.")

    args = parser.parse_args()
    main_folder_path = args.main_folder

    if not os.path.exists(main_folder_path):
        print(f"Error: The specified path '{main_folder_path}' does not exist.")
        return

    create_text_file(main_folder_path)

if __name__ == "__main__":
    main()
