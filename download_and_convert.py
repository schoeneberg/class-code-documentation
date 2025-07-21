import requests
import os

# --- Configuration for external repository ---
EXTERNAL_REPO_OWNER = "lesgourg"
EXTERNAL_REPO_NAME = "class_public"
EXTERNAL_REPO_BRANCH = "master"

# List of files to download from the external repository
# Format: { 'path/in/external/repo/file.ext': 'local/path/to/save/file.ext' }
FILES_TO_DOWNLOAD = {
    "explanatory.ini": "explanatory.ini",
    "scripts/warmup.py": "warmup.py",
}

# Directory where files will be saved locally (relative to script execution)
# Assuming script runs from root, and docs are in 'docs/'
LOCAL_BASE_DIR = "docs/temp"

# --- Main download logic ---
def download_file(external_path, local_relative_path):
    raw_url = f"https://raw.githubusercontent.com/{EXTERNAL_REPO_OWNER}/{EXTERNAL_REPO_NAME}/{EXTERNAL_REPO_BRANCH}/{external_path}"
    local_full_path = os.path.join(LOCAL_BASE_DIR, local_relative_path)

    # For private repositories, add authentication (not needed for CLASS_PUBLIC)
    # GITHUB_TOKEN = os.environ.get("GITHUB_PATH_FOR_EXTERNAL_REPO")
    # headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    # pass headers=headers to requests.get()

    print(f"Downloading {external_path} from {raw_url}")
    try:
        os.makedirs(os.path.dirname(local_full_path), exist_ok=True)
        response = requests.get(raw_url, stream=True) # use headers=headers for private repos
        response.raise_for_status() # Raise an exception for bad status codes

        with open(local_full_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to {local_full_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {external_path}: {e}")
        return False
  
# Create the base directory if it doesn't exist
os.makedirs(LOCAL_BASE_DIR, exist_ok=True)

# Download all specified files
all_downloads_successful = True
for external_path, local_relative_path in FILES_TO_DOWNLOAD.items():
    if not download_file(external_path, local_relative_path):
        all_downloads_successful = False
        break # Stop if any download fails

if not all_downloads_successful:
    print("One or more required files failed to download. Exiting.")
    exit(1) # Fail the build

# --- Conversion of custom file (now located at os.path.join(LOCAL_BASE_DIR, FILES_TO_DOWNLOAD["path/to/custom_file.data"])) ---
custom_file_to_convert = os.path.join(LOCAL_BASE_DIR, FILES_TO_DOWNLOAD["explanatory.ini"])
print(f"Proceeding to convert custom file: {custom_file_to_convert}")
# Add your custom file parsing and RST generation logic here
# This logic will use custom_file_to_convert as input
# And output RST files into your main docs directory, e.g., 'docs/generated_docs.rst'

from .convert_explanatory import convert_explanatory

# Example of reading the downloaded custom file:
with open(custom_file_to_convert, 'r', encoding='utf-8') as f:
    custom_content = f.read()
    new_content = convert_explanatory(custom_content)

# Now put the new content into the generated file
generated_rst_path = "docs/wrapper_set.rst"
with open(generated_rst_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print(f"Successfully generated RST file: {generated_rst_path}")
