# Python Wrapper for The Observatory for Economic Complexity API

**Language:** Python 3   
**Data Source:** [Observatory for Economic Complexity (OEC)](https://atlas.media.mit.edu/en/resources/data/)

## Installation
```
pip install oec
```

## Usage
See the OEC website for details about acceptable parameters for an API call: https://atlas.media.mit.edu/api/   

Check out `help.txt` or run `pydoc oec` to view function-level documentation.

**Get data from the OEC website**
```
import oec

# Set parameters in accordance with API documentation
params = {'classification': 'hs92',
		  'trade_flow': 'export',
		  'year': 2015,
		  'origin': 'egy',
		  'destination': 'all',
		  'product': 'show'}

list_of_countries = oec.get_countries()
list_of_products = oec.get_products(params['classification'])
list_of_exports = oec.get_trade(**params)
```
These functions each return lists of dictionaries. Each of these dictionaries represents a "row" of data (e.g. one country or product). The fields of these dictionaries represent "columns" of data. This is easier to visualize if you output your data to a CSV file.

**Output data to a CSV file**
```
oec.data_to_csv(list_of_dictionaries, 'results.csv')
```
These CSV files can then be opened up in the spreadsheet editor of your choice for further analysis.

**Display visualizations**
```
>>> oec.url_visual(**params)
'http://atlas.media.mit.edu/en/visualize/tree_map/hs92/export/egy/all/show/2015/'
>>> oec.embed_visual(**params)
'<iframe src="http://atlas.media.mit.edu/en/visualize/embed/tree_map/hs92/export/egy/all/show/2015/" width=930 height=400></iframe>'
>>> oec.url_visual(**params, language='fr')
'http://atlas.media.mit.edu/fr/visualize/tree_map/hs92/export/egy/all/show/2015/'
```

## Acknowledgements
Credits to [Alex Simoes](https://github.com/alexandersimoes) for the development of [The Observatory for Economic Complexity](https://atlas.media.mit.edu/en/). This module was developed by [Yahia Ali](https://github.com/yahiaali), who is not affiliated in any way with the OEC team.
