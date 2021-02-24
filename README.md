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

## Development

Create virtualenv

```shell
virtualenv -p python3.7 venv
source venv/bin/activate
```

## Packaging project

**Source distributions**

Minimally, you should create a Source Distribution:

```shell
python setup.py sdist
```

A “source distribution” is unbuilt (i.e. it’s not a Built Distribution), and requires a build step when installed by pip. Even if the distribution is pure Python (i.e. contains no extensions), it still involves a build step to build out the installation metadata from setup.py.

**Wheels**

You should also create a wheel for your project. A wheel is a built package that can be installed without needing to go through the “build” process. Installing wheels is substantially faster for the end user than installing from a source distribution.

If your project is pure Python (i.e. contains no compiled extensions) and natively supports both Python 2 and 3, then you’ll be creating what’s called a *Universal Wheel* (see section below).

If your project is pure Python but does not natively support both Python 2 and 3, then you’ll be creating a “Pure Python Wheel” (see section below).

If your project contains compiled extensions, then you’ll be creating what’s called a *Platform Wheel* (see section below).

Before you can build wheels for your project, you’ll need to install the wheel package:

```shell
python -m pip install wheel
```

## Testing

TODO

- How to test it?

<!-- Test this package, in root project run this command:

```shell
cd src
pytest
``` -->
