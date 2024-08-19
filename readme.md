### Python Selenium 4

Create readme file readme.md\
Create git ignorefile\

**To download pytest and install allure report**

pip install pytest\
pip install allure-pytest\
pip install selenium

**To generate allure report**

download node.js from https://nodejs.org/en
verify download and installed
node -v
npm install -g npm allure-commandline

pytest EX_26072024/HomeWork/HM_1.py --alluredir=allure-results\
allure generate --clean\
allure serve .\allure-results\