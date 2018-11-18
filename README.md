# taxi-app-rest
Rest api for taxi application

## How to install

1. Download city database and copy it to the project directory
http://download.maxmind.com/download/worldcities/worldcitiespop.txt.gz

2. Unzip it 

        tar -xzvf worldcitiespop.txt.gz

3. Create local settings file

        cp settings_local.dist settings_local.py
        
4. Install dependencies and start api

        pip install -r requirements.txt

        python run.py >> /dev/null &
        
5. Run country and cities import

        python import.py
        
6. Try the API

        http -a admin:admin http://127.0.0.1:5000/cities/