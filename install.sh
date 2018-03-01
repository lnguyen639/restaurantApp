# Main flow: https://docs.djangoproject.com/en/2.0/topics/install/#database-installation

# Install SQLite
wget https://www.sqlite.org/2018/sqlite-tools-osx-x86-3220000.zip
unzip sqlite-tools-osx-x86-3220000.zip

# Create contained python env, install django
virtualenv -p $(which python3.6) pythonenv
pythonenv/bin/pip install Django==2.0.2

# Create restaurant project
# https://docs.djangoproject.com/en/2.0/intro/tutorial02/
export PATH=$(pwd)/pythonenv/bin/:$PATH
echo $PATH
#django-admin startproject restaurantProj
cd restaurantProj
#python manage.py startapp restaurantApp
python manage.py migrate
python manage.py runserver
