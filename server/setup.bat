python3 -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
.\venv\Scripts\activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
cd server
python manage.py migrate
python manage.py runserver
