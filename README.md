# Python Wrapper for The Observatory for Economic Complexity API

**Language:** Python 3  
**Data Source:** [Observatory for Economic Complexity (OEC)](https://legacy.oec.world/en/resources/data/)

## Status

As of June 2021, the OEC has migrated to a new website at [oec.world](https://oec.world/), and this new site no longer hosts a free API. There is a legacy version of the site hosted at [legacy.oec.world](https://legacy.oec.world/en/), and this library has been updated to refer to that legacy version.

## Installation

```bash
pip install oec
```

## Usage

### Get data from OEC

```python
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

### Export to CSV

```python
oec.data_to_csv(list_of_dictionaries, 'results.csv')
```

These CSV files can then be opened up in the spreadsheet editor of your choice for further analysis.

### Generate links to visualizations

```python
>>> oec.url_visual(**params)
'https://legacy.oec.world/en/visualize/tree_map/hs92/export/egy/all/show/2015/'
>>> oec.embed_visual(**params)
'<iframe src="https://legacy.oec.world/en/visualize/embed/tree_map/hs92/export/egy/all/show/2015/" width=930 height=400></iframe>'
>>> oec.url_visual(**params, language='fr')
'https://legacy.oec.world/fr/visualize/tree_map/hs92/export/egy/all/show/2015/'
```

## Documentation

**Function-level documentation and language list:** see [`help.txt`](https://github.com/yahiaali/oec/blob/master/help.txt) or run `python -m pydoc oec`   
**[OEC API documentation](https://legacy.oec.world/api/)**
**[Data attributes and field names](https://github.com/alexandersimoes/oec/wiki/Attributes)

## Acknowledgements

Credits to [Alex Simoes](https://github.com/alexandersimoes) for the development of [The Observatory for Economic Complexity](https://legacy.oec.world/en/). This module was developed by [Yahia Ali](https://github.com/yahiaali), who is not affiliated in any way with the OEC team.
