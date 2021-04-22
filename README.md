# code coverage step-by-step

1. create an environment using command
   python -m venv env

2. activating the environment using command
   env\Scripts\activate.bat

3. installing dependencies needed
   pip install -r requirements.txt

4. commands for testing & code coverage.
   pytest test_main.py # tests the functions.
   coverage run test_main.py # creates the coverage test.
   coverage report # provides the coverage report.
   coverage html # displays the coverage report in a webpage (for that you have to navigate to htmlcov folder then go to index.html).

5. deactivate the environment using command
   deactivate
