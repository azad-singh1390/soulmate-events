import os
import re

# Set your target directory
parent_directory = r'd:\soulmate-events\Sound Setups'

# Allowed extensions
extensions = {'.jpeg', '.jpg', '.png', '.mp4'}

for child in os.listdir(parent_directory):
    child_path = os.path.join(parent_directory, child)
    if os.path.isdir(child_path):
        album_files = []
        for filename in os.listdir(child_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                album_files.append(filename)
        print(f"Files in '{child}': {album_files}")

        # Update script.js if it exists
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