# Pyworks Mailer

PyWork Mailer provide fast way to use SMTP mail and the most email templates.

## Features

- Setup SMTP mail easily.
- Most popular mail templates for Register, Forgot password, Daily, Weekly news, Payment, Place Order..etc.
- Compress mail before send.

... and more

## Requies

- Python 3.7+
- Virtualenv
- Pytest

## Development

### Create virtual environment

```shell
virtualenv -p python3.7 venv
source venv/bin/activate
```

Install Python dependencies:

```shell
pip install pytest
pip install wheel
```

### Test package locally

To run tests for project run this command:

pytest --pyargs <your_package_name>

```shell
pytest --pyargs src
```

Results

```
# ==================== test session starts ====================
# platform linux2 -- Python 2.7.17, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
# rootdir: /home/quanvh/FireLabs/TOOLS/pworks/pyworks-mailer, inifile: pytest.ini
# collected 1 item                                                                                                    

# src/tests/test_simple.py .                                                                                    [100%]

# ================= 1 passed in 0.02 seconds ==================
```

**Run tests with python 3**

```shell
pip3 install pytest
python3 -m pytest --pyargs src
```

Result

```
========= test session starts ==========
platform linux -- Python 3.7.9, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /home/quanvh/FireLabs/TOOLS/pworks/pyworks-mailer, configfile: pytest.ini
collected 1 item                                                                                                                                       
src/tests/test_simple.py .                                                                                                                       [100%]

========== 1 passed in 0.02s ===========
```


## Packaging project

**Create Source Distributions**

Minimally, you should create a Source Distribution for publish to PyPI:

```shell
python setup.py sdist
```

**Create Wheels**

Create a wheel for project. A wheel is a built package that can be installed without needing to go through the “build” process. Installing wheels is substantially faster for the end user than installing from a source distribution.

If your project is pure Python (i.e. contains no compiled extensions) and natively supports both Python 2 and 3, then you’ll be creating what’s called a *Universal Wheel*.

If your project is pure Python but does not natively support both Python 2 and 3, then you’ll be creating a “Pure Python Wheel”.

If your project contains compiled extensions, then you’ll be creating what’s called a *Platform Wheel*.

Before you can build wheels for your project, you’ll need to install the wheel package:

```shell
python3 -m pip install wheel
```
