# data-tracker

Web service to track crypto data

## Installation

### Requirements
- Linux or macOS or Windows
- Python 3.6+
- SQLite 3

#### SQLite installation (windows only)
1. Download DLL and binaries (32bits or 64bits) from the download page https://www.sqlite.org/download.html
2. Extract files from zip and run sqlite3.exe to verify it's working in your environment.


#### Project Installation

1. Clone the repo

    `git clone https://github.com/codeandrop/data-tracker.git`

2. cd into the project's folder

    `cd data-tracker`

3. Create a virtual enviroment

    `python3 -m venv env`

4. Activate the virtual environment

    `source env/bin/activate`

5. Install the project's requirements

    `pip3 install -r requirements.txt`

6. You can run the app by executing

    `python3 main.py`

7. You can leave the virtual env by executing

    `deactivate`


#### Running the tests

1. Follow the instructions to install the project

2. Activate the env if not already

    `source env/bin/activate`

3. The app must be stopped. To run the tests, execute:

    `python -m pytest tests/*`
