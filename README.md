## pynotify - A Python package built to send email notifications which can be integrated into any existing piece of software.

## Functionalities

Sends a simple email with a subject and a message body.
```
send_email(destinaiton, subject=" ", msg=" "):
    '''
    Arguements:
        destination: Takes in destionation email of type string
        subject(optional arguement): Takes in a string as an input (Default arg: None)
        msg(optional arguement): Takes in a message of type string as input (Default arg: None)
    '''
```
Sends an email with attachment(s) included.
```
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

A demo script of this in action is shown below
```
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

Naive implementation of this can be found [here](https://github.com/hasibzunair/neuralert)

## Motivations
<<<<<<< HEAD
Was not patient enough to keep checking the progress of the neural network while it learned how to correctly recognize a human as a gorilla!
=======
<p> 
I'm to lazy to keep watching my naive neural network finish training and also to write up a thorough tutorial on this. I also train models in CPU which takes hours or in the worst case even days. Hence wrote a program to notify me when the task is done and also providing details of it. More time to play Counter Strike! 
</p>

## What this notebook does?

* Runs a simple Convnet on **CIFAR10** dataset
* Generates and saves the model's train/test **loss** and **accuracy** graphs
* Makes a template with model parameters and saved graphs
* Sends the template as an email to the pre-defined user **after** completion of training, providing the neccesary model information.
<br>

## How to use this?

* open a **new** gmail account and set it's application status to [**less secured**](https://myaccount.google.com/intro/security) (DO NOT USE YOUR PERSONAL EMAIL ADDRESS FOR THIS. HIGHLY  RECOMMENDED TO USE NEW EMAIL)
* put the new account's credentials in **fromaddr** and **password**
* put the address to which you want to send in **toaddr**
* After you set the credentials, you are good to goooo!
* Click **RUN ALL CELLS**

**YOU HAVE TO SETUP THE NEW EMAIL ACCOUNT ONLY ONCE!**


## Trick or treat

Too lazy to set all of these up? I wrapped everything in a python package which is uploaded in TestPyPi and ready for use. You can get it [here](https://test.pypi.org/project/pynotify/)

## Takeaways

* Program written in Python 3.6
* Nothing here. What did you expect? A cookie!?

## License
[MIT](https://github.com/hasibzunair/boss-detector/blob/master/LICENSE)
>>>>>>> 6e6f40297edf71debea1db5548ed5d236d8daffa

## Author
Made with ❤️ by [Hasib Zunair](https://github.com/hasibzunair)
