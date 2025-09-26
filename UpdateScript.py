import os
import re

# List of parent directories
parent_directories = [
    r'd:\soulmate-events\Sound Setups',
    r'd:\soulmate-events\Artist',
    r'd:\soulmate-events\Barat',
    r'd:\soulmate-events\Special Effects',
    r'd:\soulmate-events\Basic Setup',
    r'd:\soulmate-events\Single Screen',
    r'd:\soulmate-events\Double Screen'
]

# Allowed extensions
image_exts = {'.jpeg', '.jpg', '.png', '.gif'}
video_exts = {'.mp4'}

for parent_directory in parent_directories:
    print(f"Processing directory: {parent_directory}")
    if not os.path.exists(parent_directory):
        continue

    # For "Sound Setups", process child directories
    if parent_directory.endswith('Sound Setups') or parent_directory.endswith('Artist') or parent_directory.endswith('Special Effects')or parent_directory.endswith('Barat'):
        for child in os.listdir(parent_directory):
            child_path = os.path.join(parent_directory, child)
            if os.path.isdir(child_path):
                files = [
                    f for f in os.listdir(child_path)
                    if f.lower() != "background.jpg"
                ]
                image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_exts]
                video_files = [f for f in files if os.path.splitext(f)[1].lower() in video_exts]
                album_files = image_files + video_files

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
        files = [
            f for f in os.listdir(parent_directory)
            if f.lower() != "background.jpg"
        ]
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_exts]
        video_files = [f for f in files if os.path.splitext(f)[1].lower() in video_exts]
        album_files = image_files + video_files

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