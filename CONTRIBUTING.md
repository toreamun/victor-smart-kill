## Instructions for Contributions

To run this code, you'll need to have Python 3.8, 3.9, 3.10, 3.11, or 3.12 installed on your machine. You'll also need
to
install the required packages by running the following commands from inside the project folder:

```shell
python3 -m venv venv
```

```shell
source venv/bin/activate
```

```shell
python3 -m pip install -r requirements.txt
```

## Code Submissions

### Style

Code formatting is handled by [black](https://pypi.org/project/black/). Before committing, run `black .` in the project
folder and resolve any reported errors.

### Linting + Type Checking

Code linting is handled by [flake8](https://flake8.pycqa.org) and [mypy](https://www.mypy-lang.org/).
Before committing, run `flake8 victor_smart_kill` and `mypy -p victor_smart_kill` in the project folder and resolve any
reported errors.

### Tests

Pytest is used to simplify testing and avoid committing broken code. Before committing, please run `pytest` in the
project folder and resolve any reported errors.

### Process

1. Fork the repo
2. Make your code changes
3. Run linting and code style checking
4. Ensure your code passes pytest checks and functions normally
5. Create a pull request against [toreamun/victor-smart-kill](https://github.com/toreamun/victor-smart-kill)
