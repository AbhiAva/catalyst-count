# catalyst-count
A Django Application that handles Database operations via UIs.

## Installing the dependencies to run on a local environment
### 1. Create and Activate Virtual Environment: 
    virtualenv <name_of_your_env>             
    source <name_of_your_env>/bin/activate    #to activate the environment
    deactivate                                #to deactivate the environment

### 2. Installing the dependencies using pip:
    pip3 install -r requirements.txt

## Setting up the Database
### Simply run the postgres script:
    sudo ./postgres.sh
### Setup the postgres user and change the user and database passwords:
    sudo passwd postgres
    
#### Login to the postgres user and create a database:
    sudo su - postgres
    
    createdb <your_db_name>
    
    psql <your_db_name>
    
#### Change the db password:
    psql -c "ALTER USER postgres WITH PASSWORD 'newpassword'"

## Deploy the application on an Amazon EC2 Instance or a DigitalOcean Droplet
### Simply run the deploy script:
    sudo ./deploy.sh
    
