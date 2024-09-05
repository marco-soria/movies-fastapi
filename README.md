#Instal virtual environment
python -m venv venv

#Activate virtual env
source venv/Scripts/activate

#install dependencies
create a requirements.txt. Then add the libraries and run pip install -r requirements.txt

"to run the app
uvicorn main:app --reload
