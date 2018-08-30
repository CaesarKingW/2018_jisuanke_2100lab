echo 'Startting config environment!'
pip install requests
pip install djangorestframework
pip install pycryptodome
pip install pillow
pip install django-cors-headers
./manage.py makemigrations
./manage.py migrate
echo 'Config environment success!'
