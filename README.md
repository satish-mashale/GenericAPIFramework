
# Purpose
Building Generalised API test automation framework with Python  , which can be used across the organization 

# Setup
Ensure you have pipenv already installed:

# How to Activate virtualenv
pipenv shell

# How Install all dependencies in your virtualenv
pipenv install

You can either use your IDE or terminal to switch to that branch and see the last updated commit.

# How to run tests in parallel 
pytest tests/ -n auto 

# Checkout the entire branch
git checkout master 

# Generate pytest automation report
pytest --html <path to report folder> test_suites_path


example:
pytest --html reports\report.html tests\test_publisheronboarding.py

# Discuss?
Feel free to use the Github discussions in this repo 

# Packages Used in this framework and their documenttion 
assertpy : https://github.com/assertpy/assertpy ( This is used for performing assertion)
requests : https://pypi.org/project/requests/ ( this used to perform CRUD operations)
Pytest : https://docs.pytest.org/en/7.1.x/contents.html 
pytest-xdist : https://pypi.org/project/pytest-xdist/ ( For running tests in parallel)


