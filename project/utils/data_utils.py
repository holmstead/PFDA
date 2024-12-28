# This module provides functions to:
# - Determine the number of header rows to skip in weather data CSV files
# - Parse metadata from weather data CSV files provided by Met Éireann

import re

def find_date_row(file_path):
    '''
    Function to find the row that contains the 'date' column using regex
    '''
    try:
        # Read the file content as text
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Search for the line that contains 'date' (case-insensitive)
        for idx, line in enumerate(lines):
            if re.search(r'\bdate,\b', line, re.IGNORECASE):
                return idx  # Return the line index where 'date' is found
        return 0  # Default to 0 if no 'date' is found, meaning skip no rows
    
    except Exception as e:
        print(f"Error reading the file for {file_path}: {e}")
        return 0  # Return 0 if something goes wrong, to avoid skipping rows


def extract_metadata_from_header(file_path):
    '''
    Function to extract metadata (station name, latitude, longitude, altitude) from CSV header using regex
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Initialize variables to store extracted values
        station_name, latitude, longitude, altitude = None, None, None, None

        # Define regex patterns for extracting metadata
        station_name_pattern = r"Station Name\s*[:=]?\s*([A-Za-z\s\(\)\-]+)"
        latitude_pattern = r"Latitude\s*[:=]?\s*([\d\.-]+)"
        longitude_pattern = r"Longitude\s*[:=]?\s*([\d\.-]+)"
        altitude_pattern = r"Station Height\s*[:=]?\s*([\d\.-]+)"
        
        # Loop through each line to search for these patterns
        for line in lines:
            station_name_match = re.search(station_name_pattern, line, re.IGNORECASE)
            if station_name_match:
                station_name = str(station_name_match.group(1).strip())

            latitude_match = re.search(latitude_pattern, line, re.IGNORECASE)
            if latitude_match:
                latitude = float(latitude_match.group(1))
            
            longitude_match = re.search(longitude_pattern, line, re.IGNORECASE)
            if longitude_match:
                longitude = float(longitude_match.group(1))
            
            altitude_match = re.search(altitude_pattern, line, re.IGNORECASE)
            if altitude_match:
                altitude = float(altitude_match.group(1))

        return station_name, latitude, longitude, altitude
    
    except Exception as e:
        print(f"Error extracting metadata from header: {e}")
        return None, None, None, None