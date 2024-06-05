# TheHive QRadar Integration

This repository contains a Python script that integrates IBM QRadar with TheHive. The script retrieves offenses from QRadar and creates corresponding cases in TheHive.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Requirements

- Python 3.6 or higher
- `thehive4py` library
- `requests` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/YOUR_GITHUB_USERNAME/thehive-qradar-integration.git
    cd thehive-qradar-integration
    ```

2. Install the required Python libraries:

    ```sh
    pip install thehive4py requests
    ```

## Configuration

Edit the `main.py` file to include your TheHive and QRadar configurations:

```python
from thehive_create_case import thehive_create_case
from qradar_get_offense import qradar_get_offense

# Configuration
thehive_url = "http://YOUR_THEHIVE_URL"
thehive_api_key = "YOUR_THEHIVE_API_KEY"
qradar_url = "https://YOUR_QRADAR_URL/api/siem/offenses"
qradar_api_token = "YOUR_QRADAR_API_TOKEN"

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
```

Replace `YOUR_THEHIVE_URL`, `YOUR_THEHIVE_API_KEY`, `YOUR_QRADAR_URL`, and `YOUR_QRADAR_API_TOKEN` with your actual configuration values.

## Usage

Run the `main.py` script to start the integration process:

```sh
python main.py
```

The script will continuously fetch offenses from QRadar and create corresponding cases in TheHive.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize the README further based on your specific needs and additional information about your project. Make sure to replace placeholders with your actual GitHub username and repository details.
