# MoviesAPI
This project is a simple REST API, it allows to perform CRUD operations on a movies database.

## Prerequisites
To run the project you need to have pipenv installed, pipenv is tool that manages the python virtual envirenment and the dependencies of the project for you.

I have a windows OS, in my case I installed pipenv using the following command:
```bat
py -m install pipenv
```
Create a folder named databases in the root of the project, it will contain the sqlite .db files.
## Running the server
First of all you need to activate the virtual envirenment:
```bat
py -m pipenv shell
```
The above command also loads the envirenment variables from the .env file.

Finally to run the flask app use the following command:
```bat
flask run
```
The app is served by default on localhost:5000/ URL.

## Tests
The project has a set of unit and integration tests, I used [pytest](https://docs.pytest.org/en/latest/) framework for the testing.

To run all tests use the following command:
```bat
pytest
```
To run sepecific tests (unit tests for example), use the following command:
```bat
pytest tests/unit
```
