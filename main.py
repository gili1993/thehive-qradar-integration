from thehive_create_case import thehive_create_case
from qradar_get_offense import qradar_get_offense

import time

# Configuration
thehive_url = "http://10.100.102.110:9000"
thehive_api_key = "sbDn88JU1MU9kM+2Fh3fGnMoAL/y8+zU"
qradar_url = "https://10.100.102.85/api/siem/offenses"
qradar_api_token = "8f70b094-2ae1-4d9f-ac34-5953369ad8a6"

offense_info = qradar_get_offense(qradar_url, qradar_api_token)

while(offense_info):
    # TheHive case detail
    title = f"QRadar Incident - {offense_info['description']}"
    description = offense_info['description']
    severity = offense_info['severity']
    startDate = offense_info['start_time']
    tags = offense_info['categories']
    status = offense_info['status']

    # Create Case in TheHive
    thehive_create_case(url=thehive_url, api_key=thehive_api_key, title=title,  description=description, startDate=startDate, tags=tags, status=status)
    offense_info = qradar_get_offense(qradar_url, qradar_api_token)
else:
    print("QRADAR Offense ID not valid!")

