# PythonAssignment2
 Web Scrapping tool for Cryptocurrencies 

### Installation 

To do web scrapping tool ```beautifulsoup4```, ```selenium```, and ```webdriver-manager``` libraries are required. Below shown their installation

```python
pip install beautifulsoup4
pip install selenium
pip install webdriver-manager
```

### Install script

```
git clone https://github.com/saku-bara/PythonAssignment2.git
cd PythonAssignment2
```

#### Edit path in the script

Provide the path to the file where data will be saved. You need to edit `test.py` file. In my case it is:

```python
sys.path.append('D:\\assignment2\\src')
```

### Usage

```python
from scrapper import Parser
parser = Parser()
parser.getting('bitcoin')
```

```python
# after you installed the project and changed path
cd
