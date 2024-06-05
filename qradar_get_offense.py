import requests

def qradar_get_offense(url, api_token):
    # Function to read offense ID from file
    def read_offense_id(file_path):
        try:
            with open(file_path, 'r') as file:
                offense_id = file.read().strip()
                return int(offense_id)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except ValueError:
            print(f"Invalid offense ID in file: {file_path}")
            return None
    
    offense_id_file = "offense_id.txt"

    # Read the offense ID from the file
    offense_id = read_offense_id(offense_id_file)

    if offense_id is not None:
        # Headers for the request
        headers = {
            "SEC": api_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        # Make the GET request to fetch the offense details
        response = requests.get(f"{url}/{offense_id}", headers=headers, verify=False)

        # Check if the request was successful
        if response.status_code == 200:
            offense_details = response.json()
            print("Offense details fetched successfully:")
            
            # Incrase by 1 the offense_id
            f = open(offense_id_file, 'w')
            next_offense_id = int(offense_id) + 1
            next_offense_id = str(next_offense_id)
            f.write(next_offense_id)
            f.close()
            
            return offense_details
            
        else:
            print(f"Failed to fetch offense details: {response.status_code}")
            return False
    else:
        print("No valid offense ID found. Please check the file content.")
        return False

