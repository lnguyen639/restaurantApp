# Main flow: https://docs.djangoproject.com/en/2.0/topics/install/#database-installation

# Install SQLite
wget https://www.sqlite.org/2025/sqlite-tools-osx-x64-3490200.zip
unzip sqlite-tools-osx-x64-3490200.zip

# Create contained python env, install django
python -m venv pythonenv
pythonenv/bin/pip install Django

# Create restaurant project
# https://docs.djangoproject.com/en/2.0/intro/tutorial02/
export PATH=$(pwd)/pythonenv/bin/:$PATH
echo $PATH
#django-admin startproject restaurantProj
cd restaurantProj
#python manage.py startapp restaurantApp
python manage.py migrate
python manage.py runserver
