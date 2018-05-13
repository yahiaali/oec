# Python Wrapper for The Observatory for Economic Complexity API

**Language:** Python 3   
**Data Source:** [Observatory for Economic Complexity (OEC)](https://atlas.media.mit.edu/en/resources/data/)

## Installation
```
git clone https://github.com/yahiaali/oec.git
pip3 install -r oec/requirements.txt
```

## Usage
See the OEC website for details about acceptable parameters for an API call: https://atlas.media.mit.edu/api/

**Get data from the OEC website**
```
import oec

list_of_countries = oec.get_countries()
list_of_products = oec.get_products('hs92')
list_of_exports = oec.get_trade_data('hs07', 'export', 2015, 'egy', 'all', 'show')
```
These functions each return lists of dictionaries. Each of these dictionaries represents a "row" of data (e.g. one country or product). The fields of these dictionaries represent "columns" of data. This is easier to visualize if you output your data to a CSV file.

**Output data to a CSV file**
```
oec.data_to_csv(list_of_dictionaries, 'results.csv')
```
These CSV files can then be opened up in the spreadsheet editor of your choice for further analysis.

## Acknowledgements
Credits to [Alex Simoes](https://github.com/alexandersimoes) for the development of [The Observatory for Economic Complexity](https://atlas.media.mit.edu/en/). This module was developed by [Yahia Ali](https://github.com/yahiaali), who is not affiliated in any way with the OEC team.
