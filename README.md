# django-operations
A Django Application that handles Database operations via UIs.

## Installing the dependencies to run on a local environment
### 1. Create and Activate Virtual Environment: 
    virtualenv <name_of_your_env>             
    source <name_of_your_env>/bin/activate    #to activate the environment
    deactivate                                #to deactivate the environment

### 2. Installing the dependencies using pip:
    pip3 install -r requirements.txt

## Deploy the application on an Amazon EC2 Instance or a DigitalOcean Droplet
### Simply run the deploy script:
    sudo ./deploy.sh
    