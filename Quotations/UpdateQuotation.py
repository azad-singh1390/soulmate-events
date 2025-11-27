import os
from pathlib import Path
from datetime import datetime

# You are already inside the Quotation directory
BASE_DIR = Path(".")
OUTPUT_FILE = "quotation_list.html"

def generate_html():
    rows = []
    s_no = 1

    # Collect subdirectories with their mtime
    subdirs = [d for d in BASE_DIR.iterdir() if d.is_dir()]

    # Sort by last modified time (most recent first)
    subdirs_sorted = sorted(subdirs, key=lambda d: d.stat().st_mtime, reverse=True)

    for subdir in subdirs_sorted:
        # Find PDF (first one)
        pdf_files = [f for f in subdir.iterdir() if f.suffix.lower() == ".pdf"]
        # Find Word (first one)
        word_files = [f for f in subdir.iterdir() if f.suffix.lower() in (".doc", ".docx")]

        pdf_link = (
            f'<a href="{subdir.name}/{pdf_files[0].name}" target="_blank">{pdf_files[0].name}</a>'
            if pdf_files else "No PDF"
        )

        word_link = (
            f'<a href="{subdir.name}/{word_files[0].name}" target="_blank">{word_files[0].name}</a>'
            if word_files else "No Word"
        )

        # Folder last updated time (based on folder mtime)
        last_updated = datetime.fromtimestamp(subdir.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

        rows.append(f"""
            <tr>
                <td>{s_no}</td>
                <td>{subdir.name}</td>
                <td>{pdf_link}</td>
                <td>{word_link}</td>
            </tr>
        """)
        s_no += 1

    # HTML output
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>Quotation Document List</title>
        <style>
            body {{
                text-align: center;
                font-family: Arial, sans-serif;
            }}
            table {{
                width: 90%;
                margin: 20px auto;
                border-collapse: collapse;
                text-align: center;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background: #f2f2f2;
                font-weight: bold;
            }}
            a {{
                text-decoration: none;
                color: blue;
            }}
            /* Responsive small-screen tweak */
            @media (max-width: 700px) {{
                table {{ width: 100%; font-size: 14px; }}
            }}
        </style>
    </head>
    <body>
        <h2>Quotation Document List </h2>
        <table>
            <thead>
                <tr>
                    <th>S.NO</th>
                    <th>Name</th>
                    <th>PDF</th>
                    <th>Word</th>
                </tr>
            </thead>
            <tbody>
                {''.join(rows)}
            </tbody>
        </table>
    </body>
    </html>
    """

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML file generated:", OUTPUT_FILE)

if __name__ == "__main__":
    generate_html()
