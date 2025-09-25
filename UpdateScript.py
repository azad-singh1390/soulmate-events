import os
import re

# List of parent directories
parent_directories = [
    r'd:\soulmate-events\Sound Setups',
    r'd:\soulmate-events\Basic Setup',
    r'd:\soulmate-events\Single Screen',
    r'd:\soulmate-events\Double Screen'
]

# Allowed extensions
extensions = {'.jpeg', '.jpg', '.png', '.mp4'}

for parent_directory in parent_directories:
    print(f"Processing directory: {parent_directory}")
    if not os.path.exists(parent_directory):
        continue

    # For "Sound Setups", process child directories
    if parent_directory.endswith('Sound Setups'):
        for child in os.listdir(parent_directory):
            child_path = os.path.join(parent_directory, child)
            if os.path.isdir(child_path):
                album_files = [
                    f for f in os.listdir(child_path)
                    if os.path.splitext(f)[1].lower() in extensions and f.lower() != "background.jpg"
                ]

                script_path = os.path.join(child_path, 'script.js')
                if os.path.exists(script_path):
                    js_array = ',\n    '.join(f'"{file}"' for file in album_files)
                    new_album_files = f'const albumFiles = [\n    {js_array}\n];'

                    with open(script_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    content = re.sub(
                        r'const albumFiles = \[[^\]]*\];',
                        new_album_files,
                        content,
                        flags=re.DOTALL
                    )

                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                    print(f"Updated albumFiles in {script_path}")
    else:
        # For other directories, update script.js directly in the path
        album_files = [
            f for f in os.listdir(parent_directory)
            if os.path.splitext(f)[1].lower() in extensions and f.lower() != "background.jpg"
        ]

        script_path = os.path.join(parent_directory, 'script.js')
        if os.path.exists(script_path):
            js_array = ',\n    '.join(f'"{file}"' for file in album_files)
            new_album_files = f'const albumFiles = [\n    {js_array}\n];'

            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()

            content = re.sub(
                r'const albumFiles = \[[^\]]*\];',
                new_album_files,
                content,
                flags=re.DOTALL
            )

            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Updated albumFiles in {script_path}")