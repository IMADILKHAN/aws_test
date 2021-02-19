# Demo-Project



Database modeling with sqlalchemy
API to performance CRUD Operations on database with Flask (see app.py)
Automated testing (see test_server.sh)
Deployment on Heroku


To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```bash
  $ virtualenv --no-site-packages env_capstone
  $ source env_capstone/scripts/activate
  ```

2. Install the dependencies:
```bash
$ pip install -r requirements.txt
```
3. Setup the database:
```bash
$ python3 setupdatabase.py
```

4. Run the server:
```bash
$ python3 app.py
```


## API Documentation
Here you can find all existing endpoints, which methods can be used, how to work with them.

Additionally, common pitfalls & error messages are explained, if applicable.

Here is a short table about which ressources exist and which method you can use on them.

                          Allowed Methods
       Endpoints    |  GET |  POST |  DELETE | PATCH  |
                    |------|-------|---------|--------|
      /memes        |  [x] |  [x]  |         |        |   
      /memes/<id>   |  [x] |  [x]  |   [x]   |   [x]  |   



### 1. GET /memes
```bash
$ curl -X GET http://127.0.0.1:8081/memes
```
- Returns Json data of all Memes:
    1) Id
    2) Full Name
    3) Caption
    4) Url

### 2. GET /memes/<id>
```bash
$ curl -X GET http://127.0.0.1:8081/memes/<id>
```
- Returns Json data of Specific Meme:
        1) Id
        2) Full Name
        3) Caption
        4) Url

### 3. PATCH /memes/<id>
```bash
        $ curl -X GET http://127.0.0.1:8081/memes/<id>
```     
        Takes two arguments :
            1)Caption
            2) Url
- Returns Json data of Updated Meme:
                1) Id
                2) Full Name
                3) Caption
                4) Url

### 4. DELETE /memes/delete/<id>
```bash
$ curl -X GET http://127.0.0.1:8081/memes/delete/<int:id>
```     
Takes id
- Returns Json data of sucess message:
