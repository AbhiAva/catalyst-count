# Taking the latest pull
echo Taking latest pull ....
git pull

# Copying env variables
echo Copying Environment Variables ....
cp catalyst_count/catalyst_count/.env.local catalyst_count/catalyst_count/.env

# Activating the Environment
echo Activating the Environment ....
source ~/django-app/bin/activate

# Restart a supervisor server instance
# echo Restarting supervisor ....
# supervisorctl stop all
# supervisorctl start all

# Run the File