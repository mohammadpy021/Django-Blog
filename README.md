# django project for univeristy
### برنامه نویسی مبتنی بر وب
#### استاد : افشاری

 ## نام اعضای گروه  

`حمید رضا بصیری ` 
<br>
` محمد گلیم باف ` 
<br>
` رضا نصرالهی  ` 
<br>
` محمد پارسا حسینی  `
<br>
`  دانیال مهرداد  ` 

# creating Virtual environment 
### Linux 
``` console
python -m venv venv
source venv\bin\activate
```
### Windows 
``` console
py  -m venv venv
venv\Script\activate
```
# install packages 
``` console
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
# create Superuser
``` console
python manage.py createsuperuser 
```
# Run on localserver
``` console
python manage.py runserver
```







