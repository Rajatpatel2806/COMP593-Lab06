import hashlib
import os
import subprocess
import requests

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    """Downloads the text file containing the expected SHA-256 value for the VLC installer file from the 
    videolan.org website and extracts the expected SHA-256 value from it.

    Returns:
        str: Expected SHA-256 hash value of VLC installer
    """
    # TODO: Step 1
    # Hint: See example code in lab instructions entitled "Extracting Text from a Response Message Body"
    # Hint: Use str class methods, str slicing, and/or regex to extract the expected SHA-256 value from the text 


    response = requests.get("http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256")
    response.raise_for_status()
    expected_sha256 = response.text.strip()
    return expected_sha256

def download_installer():
    """Downloads, but does not save, the .exe VLC installer file for 64-bit Windows.Returns:
        bytes: The VLC installer file as bytes
    """
    # TODO: Step 2
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"

    response = requests.get("http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe")
    response.raise_for_status()
    return response.content

def installer_ok(installer_data, expected_sha256):
    """Computes the SHA-256 hash value of the VLC installer data and compares it to the expected SHA-256 hash value.

    Args:
        installer_data (bytes): The VLC installer file as bytes
        expected_sha256 (str): Expected SHA-256 hash value of VLC installer

    Returns:
        bool: True if the SHA-256 hash values match, False otherwise
    """
    # TODO: Step 3
    # Hint: See example code in lab instructions entitled "Computing the Hash Value of a Response Message Body"


    actual_sha256 = hashlib.sha256(installer_data).hexdigest()
    return actual_sha256 == expected_sha256

def save_installer(installer_data):
    """Saves the VLC installer data to disk.

    Args:
        installer_data (bytes): The VLC installer file as bytes

    Returns:
        str: The path to the saved VLC installer file
    """
    # TODO: Step 4
    # Hint: See example code in lab instructions entitled "Downloading a Binary File"

    installer_path = os.path.join(os.getenv("TEMP"), "vlc-3.0.18.4-win64.exe")
    with open(installer_path, "wb") as installer_file:
        installer_file.write(installer_data)
    return installer_path

def run_installer(installer_path):
    """Runs the VLC installer silently.

    Args:
        installer_path (str): The path to the VLC installer file
    """
    # TODO: Step 5
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"

    subprocess.run([installer_path, "/S", "/L=1033"], check=True)

def delete_installer(installer_path):
    # TODO: Step 6
    # Hint: See example code in lab instructions entitled "Running the VLC Installer"
    
    """Deletes the VLC installer file from disk.

    Args:
        installer_path (str): The path to the VLC installer file
    """
    if os.path.exists(installer_path):
        os.remove(installer_path)

if __name__ == "__main__":
    main()