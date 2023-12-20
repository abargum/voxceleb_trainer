import os
import argparse
import random

def create_samples_text_file(main_folder):
    # Output file name
    output_file = "data/test_list.txt"

    with open(output_file, 'w') as file:

        # Function to get a list of all valid WAV file paths from all subsubfolders within a speaker folder
        def get_valid_wav_paths(speaker_folder_path):
            wav_paths = []
            for subfolder_name in os.listdir(speaker_folder_path):
                subfolder_path = os.path.join(speaker_folder_path, subfolder_name)
                if os.path.isdir(subfolder_path):
                    wav_paths.extend([(os.path.join(subfolder_path, file)) for file in os.listdir(subfolder_path) if file.endswith(".flac")])
            return wav_paths

        # Iterate over subfolders in the main folder
        for speaker_folder_name in sorted(os.listdir(main_folder), key=lambda x: int(x)):
            speaker_folder_path = os.path.join(main_folder, speaker_folder_name)

            # Check if the item in the main folder is a subfolder
            if os.path.isdir(speaker_folder_path):
                # Get a list of all valid WAV file paths within the speaker folder
                wav_paths = get_valid_wav_paths(speaker_folder_path)

                # Iterate over WAV paths
                for wav_path in wav_paths:
                    # Draw 4 equal samples from the same speaker
                    for _ in range(4):
                        other_wav_path = random.choice(wav_paths)
                        while other_wav_path == wav_path:  # Ensure different file
                            other_wav_path = random.choice(wav_paths)
                        file.write(f"1\t{wav_path}\t{other_wav_path}\n")

                        # Draw 4 different samples from different speakers
                        other_speaker_folder_name = random.choice([name for name in os.listdir(main_folder) if name != speaker_folder_name])
                        other_speaker_folder_path = os.path.join(main_folder, other_speaker_folder_name)
                        other_wav_path = random.choice(get_valid_wav_paths(other_speaker_folder_path))
                        file.write(f"0\t{wav_path}\t{other_wav_path}\n")

    print(f"Output file '{output_file}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description="Create a text file with speaker samples.")
    parser.add_argument("--main_folder", help="Path to the main folder containing speaker subfolders.")

    args = parser.parse_args()
    main_folder_path = args.main_folder

    if not os.path.exists(main_folder_path):
        print(f"Error: The specified path '{main_folder_path}' does not exist.")
        return

    create_samples_text_file(main_folder_path)

if __name__ == "__main__":
    main()
