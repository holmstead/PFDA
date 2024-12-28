# This module contains a function to download and extract ZIP files 

import os
import requests
import zipfile

def download_and_extract_zip(url, download_dir, file_name=None):
    """
    Downloads a ZIP file from a given URL, saves it to a specified directory,
    extracts its contents, and then deletes the ZIP file.
    """
    try:
        # Determine the file name if not provided (based on the last part of the URL)
        if not file_name:
            file_name = url.split("/")[-1]

        # Define the file path to save the ZIP file
        file_path = os.path.join(download_dir, file_name)
        
        # Send a GET request to download the file
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to the file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Successfully downloaded {file_path}")
            
            try:
                # Open the ZIP file
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    # Extract all contents into the specified directory
                    zip_ref.extractall(download_dir)
                    print(f"Extracted {file_path} in {download_dir}")
                
                # After extraction, delete the ZIP file
                os.remove(file_path)
                print(f"Deleted {file_path} after extraction")
            
            except zipfile.BadZipFile:
                print(f"Failed to extract {file_path}: Bad ZIP file")
            except Exception as e:
                print(f"Error extracting {file_path}: {e}")
        
        else:
            print(f"Failed to download {url}: {response.status_code}")
    
    except Exception as e:
        print(f"Error downloading {url}: {e}")