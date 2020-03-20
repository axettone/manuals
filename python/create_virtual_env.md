# How to create a virtual environment for python

So you will be able to create and independent sandbox, without
secondary effects on your system (that probably will run 2.7 only).

## First, install python3-venv

`sudo apt-get install python3-venv`

or equivalent on your system.

## Second: the magic

Build your virtual env with

`sudo python3 -m venv your_project_name_venv`

Now step into the virtual environment with:

`source your_project_name_venv/bin/activate`

You have to use this command everytime you want to
launch your project.

## Upgrade pip and install packages

Inside your venv, you can upgrade pip anytime

`pip install --upgrade pip`

Install whatever you want... it'll be put inside
your venv only.

`pip install <yourlib>`

>Author Paolo Niccolò Giubelli