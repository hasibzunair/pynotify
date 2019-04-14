## pynotify 

A Python package built to send email notifications which can be integrated into any existing piece of python software.

## Features

Sends a simple email with a subject and a message body.
```python
send_email(destinaiton, subject=" ", msg=" "):
    '''
    Arguements:
        destination: Takes in destionation email of type string
        subject(optional arguement): Takes in a string as an input (Default arg: None)
        msg(optional arguement): Takes in a message of type string as input (Default arg: None)
    '''
```
Sends an email with attachment(s) included.
```python
send_email_with_attachment(destination, files, sub="Subject", text= "No text"):
    '''
    Arguements:
        destination: Takes in destionation email of type string
        files: Take in a list of strings as input
        sub(optional arguement): Takes in a string as an input (default arg empty)
        text(optional arguement): Takes in a message of type string as input (default arg empty)
    '''
```

## Usage
Import the library from TestPyPi (Test Python Packaging Index)

```python
pip install -i https://test.pypi.org/simple/ pynotify
```


A demo script of this in action is shown below
```python
from pynotify import send_email, send_email_with_attachment

subject = "Killer Robot"
message = "Hi there!"
dest = "youremail@youremail.com" # add your email here

# attachment paths are stored in an array
image = ["cat.jpg"]
images = ["cat.jpg", "dog.jpg"]

# sends an email
send_email(dest, "Hello!")

# sends an email with attachements
send_email_with_attachment(dest, images, subject, message)

```

## Takeaways

* Program written in Python 3.6
* Nothing here. What did you expect? A cookie!?

## Author
Made with ❤️ by [Hasib Zunair](https://github.com/hasibzunair)
