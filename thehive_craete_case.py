"""
The thehive_create_case function is designed to create a new case in TheHive.
This function uses the thehive4py library to interact with TheHive's REST API, allowing the user to automate the process of case creation with predefined attributes.
"""

from thehive4py.api import TheHiveApi
from thehive4py.models import Case
from datetime import datetime

def thehive_create_case(url, api_key, title, description, startDate, tags, status):

    # Initialize TheHive API
    api = TheHiveApi(url, api_key)

    # Define case details
    case = Case(
    	title=title,
    	description=description,
    	#severity=severity,
    	startDate=startDate,
    	tags=tags,
    	#tlp=2,  # Traffic Light Protocol level
    	#pap=2,  # Protocol for Announcing Proposals level
    	status=status
    )

	# Create the case
    response = api.create_case(case)

	# Chack of the request was successful
    if response.status_code == 201:
        print("Case created successfully.")
        print(response.json())  # Print the details of the created case.
    else:
        print(f"Failed to create case: {response.status_code}")
        print(response.json())  # Print the error details
