# Alchemy_test
## Requirements
- Python3
- Pip3
- Venv

## Installation
1. Download the repository
2. Create a virtual environment
   ```commandline
   python3 -m venv ./venv
   ```
3. Activate the virtual environment
   ```commandline
   source venv/bin/activate
   ```
4. Install the required libraries
   ```commandline
   pip3 install -r requirements.txt
   ```
## Running tests
First activate the mocked API

*Windows*
```commandline
cd API/
set set FLASK_APP=hello.py
flask run
```

*Unix/Linux*
```bash
cd API/
export FLASK_APP=hello.py
flask run
```

To run the tests simply execute 
```commandline
behave features/
```
