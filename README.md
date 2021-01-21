# Funny endpoints
Simple python-application that interacts with different open api's to create text that you can receive on GET endpoints. See [swagger.yml](swagger.yml).

It uses [poetry](https://python-poetry.org/) for dependency management, [flask](https://github.com/pallets/flask) for the web server and [requests](https://github.com/psf/requests) for the http requests.

## Testing
Testing is done using [pytest](https://docs.pytest.org/en/stable/). Testing of [funny.py](./funny-endpoints/funny_endpoints/funny.py) is done using dependency injection. Mocking of [requests](https://github.com/psf/requests) is done in [requester_mock.py](./funny-endpoints/tests/requester_mock.py).

Testing of [router.py](./funny-endpoints/funny_endpoints/router.py) is done using [flask test_client](https://github.com/pallets/flask/blob/master/docs/testing.rst).

To run the tests invoke:

```bash
poetry run pytest
```

## Running
To run use [poetry](https://python-poetry.org/). Invoke:
```bash
$ cd funny-endpoints
$ poetry run funny
```

## Docker
### Building
To build for docker invoke:
```bash
docker-compose build
```

### Running
To run the application in docker invoke:
```bash
docker-compose up -d
```

## Examples of using it
### Get an advice
```bash
$ curl http://localhost:5000/v1/advice
{"message":"If you don't want something to be public, don't post it on the Internet."}
```

### Get a Chuck Norris Joke
```bash
$ curl http://localhost:5000/v1/chucknorris
{"message":"there is no use crying over spilled milk, unless its Chuck Norris' milk because then your gonna die"}
```

### Get a dad joke
```bash
$ curl http://localhost:5000/v1/dadjoke
{"message":"What do you call an eagle who can play the piano? Talonted!"}
```

### Get a random message
```bash
$ curl http://localhost:5000/v1/random
{"message":"Advice: When painting a room, preparation is key. The actual painting should account for about 40% of the work."}
```
