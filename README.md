# PythonAssignment2 Web Scrapping tool
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
git clone https://github.com/saku-bara/WebScrappingTool.git
cd WebScrappingTool
```

#### Edit path in the script

Provide the path to the file where data will be saved. You need to edit `test.py` file. In my case it is:

```python
sys.path.append('D:\\assignment2\\src')
```

### Usage

```
# after you installed the project and changed path
cd WebScrappingTool\test
python test.py
```

### Examples

```python
from scrapper import Parser
parser = Parser()
parser.getting('bitcoin')
```
 The output will look like:
```
{'title': "Vitalik Buterin: El Salvador's Bitcoin Approach Is 'Contrary to the Ideals' of Crypto", 'description': 'The Ethereum creator railed that Nayib Bukele "loves being praised" and said "shame on Bitcoin maximalists who are uncritically praising him."', 'img': 'https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2021/09/vitalik_buterin_2029298183-gID_2.jpg'}
```
