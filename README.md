# drf social network
## features
- registration
- token, refresh (JWT) 
- post creation, list view, detailed view
- post voting

## setup
- env: `python3 -m venv env`
- `source env/bin/activate`
- requirements: `pip install -r requirements.txt`
- apply migrations: `python manage.py migrate`

### .env file example
```
SECRET_KEY=<your_secret_key>
DEBUG=True
```

## db schema
![schema](https://github.com/dzhfrv/dzhfrv-starn/blob/master/drf_social.png?raw=true)
