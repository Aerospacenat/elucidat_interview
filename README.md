# Python Environment Setup #
### Create Python Virtual Environment ###
To create a virtual environment in Python, you can use the following command:
```bash 
 python3 -m venv venv
```
To activate the venv, For MacOS and Linux:
```bash 
source venv/bin/activate
```
For windows
```bash
venv\Scripts\activate
```
To deactivate 
```bash 
deactivate
```
To remove the venv:
For MacOS and Linux
```bash
rm -rf venv
```
For Windows
```bash
rmdir venv
```

### Install dependencies  ###

```bash
pip install -r requirements.txt 
```

### Run behave tests ###

```console
behave
```
### Reading the logs  ###


To read the logs you will get for example:
```bash 
Failing scenarios:
features/api_testing.feature:6  Verify Content Security Policy (CSP) header
features/ui_testing.feature:9  The score should be a number between 0 and 100
features/ui_testing.feature:13  Burger menu should be present from the Finding the truth page

0 features passed, 2 failed, 0 skipped
0 scenarios passed, 3 failed, 0 skipped
12 steps passed, 3 failed, 0 skipped, 0 undefined
Took 0m25.338s
````
And the by scrolling up you will see the error message for each failed scenario

When the tests are passing you will see: 
```bash 
2 features passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
15 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m25.338s
```


### Run Flake8 ###

```bash
flake8 features/steps/steps.py
```