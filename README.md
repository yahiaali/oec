# API Wrapper for The Observatory for Economic Complexity

Data source: [Observatory for Economic Complexity (OEC)](https://atlas.media.mit.edu/en/resources/data/)

## Directory Structure
`oec.py`				module that facilitates interaction with OEC database via API calls
`requirements.txt`		list of dependencies for running the Python code included in this repository

## Installation
`git clone https://github.com/yahiaali/oec-python.git`

## Usage
See the OEC website for details about acceptable parameters for an API call: https://atlas.media.mit.edu/api/

**Get data from the OEC website**
```
import oec

list_of_countries = oec.get_countries()
list_of_products = oec.get_products('hs92')
list_of_imports = oec.get_trade_data('hs07', 'export', 2015, 'egy', 'all', 'show')
```
These functions each return lists of dictionaries. Each of these dictionaries represents a "row" of data (e.g. one country or product). The fields of these dictionaries represent "columns" of data. This is easier to visualize if you convert your data into csv format.

**Output data to a CSV file***
```
oec.data_to_csv(list_of_dictionaries, 'results.csv')
```
