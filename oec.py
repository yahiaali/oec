"""
This module serves as an API wrapper for The Observatory for Economic
Complexity (OEC).

OEC API documentation:
https://atlas.media.mit.edu/api/

Data attributes and field names:
https://github.com/alexandersimoes/oec/wiki/Attributes

List of avaiable language codes for visualizations:
'en'    English
'ar'    Arabic
'de'    German
'el'    Greek
'es'    Spanish
'fr'    French
'he'    Hebrew
'hi'    Hindi
'it'    Italian
'ja'    Japanese
'ko'    Korean
'mn'    Mongolian
'nl'    Dutch
'pt'    Portuguese
'ru'    Russian
'tr'    Turkish
'vi'    Vietnamese
'zh_cn' Chinese
"""

import requests
import csv


def build_call(*args):
    """
    Create a URL for a request to the OEC API.

    Args:
        *args (str): strings to be appended to the API call.

    Returns:
        str: url for the API request.
    """
    call_url = 'http://atlas.media.mit.edu/'
    for val in args:
        call_url += str(val) + '/'
    return call_url


def request_data(call_url):
    """
    Get the results of an API request.

    Args:
        call_url (str): URL for the API request specified as a string.

    Returns:
        list of dictionaries containing results of the API request.
    """
    r = requests.get(call_url)
    response_dict = r.json()
    json_list = response_dict['data']  # list of dicts containing data
    return json_list


def get_countries(filename=None):
    """
    Get a list of dictionaries with country attributes via an API request.

    Args:
        filename (str): write the result to this CSV file if specified.
        Defaults to None.

    Returns:
        list of dictionaries containing results of the API request.
    """
    call = build_call('attr', 'country')
    json_list = request_data(call)
    if filename is not None:
        data_to_csv(json_list, filename)
    return json_list


def get_products(classification, filename=None):
    """
    Get the results of an API request for product descriptions.

    Args:
        classification (str): string specifying which product classification to
        use (e.g. 'hs92', 'hs96', 'hs02', 'hs07', 'sitc').

    Returns:
        list of dictionaries containing results of the API request.
    """
    call = build_call('attr', classification)
    json_list = request_data(call)
    if filename is not None:
        data_to_csv(json_list, filename)
    return json_list


def get_trade(classification, trade_flow, year, origin, destination,
              product, filename=None):
    """
    Get the results of an API request for trade data.

    Args:
        classification (str): specifies which product classification to use
            (e.g. 'hs92', 'hs96', 'hs02', 'hs07', 'sitc').
        trade_flow (str): specifies which trade value to show
            (e.g. 'import', 'export').
        year (str): specifies which year or range of years to show
            (e.g. 2015, '2002.2005').
        origin (str): specifies a country of origin ('egy'), whether to show
            all countries ('show'), or whether to sum all imports regardless
            of origin ('all').
        destination (str): specifies a country of origin ('egy'), whether to
            show all countries ('show'), or whether to sum all exports
            regardless of origin ('all').
        product (str): specifies whether to show all products ('show'), sum the
            data regardless of product ('all'), or show a particular product
            designated by a four-digit HS or SITC id.
        filename (str): name of file to save results to. Defaults to None.

    Returns:
        list of dictionaries containing results of the API request.
    """
    call = build_call(classification, trade_flow, year, origin, destination,
                      product)
    json_list = request_data(call)
    if filename is not None:
        data_to_csv(json_list, filename)
    return json_list


def trade_params(classification, trade_flow, year, origin, destination,
                 product):
    """
    Return a dictionary of parameters for requesting trade data and
    visualizations.

    Args:
        classification (str): specifies which product classification to use
            (e.g. 'hs92', 'hs96', 'hs02', 'hs07', 'sitc').
        trade_flow (str): specifies which trade value to show
            (e.g. 'import', 'export').
        year (str): specifies which year or range of years to show
            (e.g. 2015, '2002.2005').
        origin (str): specifies a country of origin ('egy'), whether to show
            all countries ('show'), or whether to sum all imports regardless
            of origin ('all').
        destination (str): specifies a country of origin ('egy'), whether to
            show all countries ('show'), or whether to sum all exports
            regardless of origin ('all').
        product (str): specifies whether to show all products ('show'), sum the
            data regardless of product ('all'), or show a particular product
            designated by a four-digit HS or SITC id.

    Returns:
        dictionary of parameters.
    """
    parameters = {'classification': classification,
                  'trade_flow': trade_flow,
                  'year': year,
                  'origin': origin,
                  'destination': destination,
                  'product': product}
    return parameters


def get_header(json_list):
    """
    Return a list of header strings for the give list of dictionaries.

    Args:
        json_list (list): list of dictionaries produced by an API request

    Returns:
        list: fieldnames used in the data.
    """
    header = set()
    for dict in json_list:
        header.update(dict.keys())
    header = list(header)
    header.sort()
    return header


def data_to_csv(json_list, filename):
    """
    Convert received list of JSON objects into a CSV file.

    Args:
        json_list (list): list of dictionaries produced by an API request.
        filename (str): name of file to save results to.
    """
    with open(filename, 'w') as csvfile:
        header = get_header(json_list)
        cw = csv.writer(csvfile)
        cw.writerow(header)
        for dict in json_list:
            row = dict_to_list(dict, header)
            cw.writerow(row)


def dict_to_list(dict, header):
    """
    Convert a dictionary into a list in the order specified by the header.

    Args:
        dict (dict): dictionary containing data from an API request
        header (str): list of fieldnames present in the data

    Returns:
        list: contents of dictionary in the order specified by the header
    """
    row = []
    for field in header:
        if field in dict:
            row.append(str(dict[field]))
        else:
            row.append(None)
    return row


def embed_visual(classification, trade_flow, year, origin, destination,
                 product, visualization='tree_map', language='en', width=930,
                 height=400, name=None, id=None):
    """
    Return HTML code for embedding a visualization into a webpage.

    Args:
        classification (str): specifies which product classification to use
            (e.g. 'hs92', 'hs96', 'hs02', 'hs07', 'sitc').
        trade_flow (str): specifies which trade value to show
            (e.g. 'import', 'export').
        year (str): specifies which year or range of years to show
            (e.g. 2015, '2002.2005').
        origin (str): specifies a country of origin ('egy'), whether to show
            all countries ('show'), or whether to sum all imports regardless
            of origin ('all').
        destination (str): specifies a country of origin ('egy'), whether to
            show all countries ('show'), or whether to sum all exports
            regardless of origin ('all').
        product (str): specifies whether to show all products ('show'), sum the
            data regardless of product ('all'), or show a particular product
            designated by a four-digit HS or SITC id.
        visualization (str): specifies which visualization to show. Defaults
            to 'tree_map'.
        language (str): specifies the language used for the visualization.
        width (int): width of visualization in pixels.
        height (int): height of visualization in pixels.
        name (str): optional iframe parameter.
        id (str): optional iframe parameter.

    Returns:
        str: HTML code for embedding the visualization as an iframe
    """
    src = build_call(language, 'visualize', 'embed', visualization,
                     classification, trade_flow, origin, destination,
                     product, year)
    iframe = '<iframe src="{:s}" width={:d} height={:d}'.format(src, width,
                                                                height)
    if name is not None:
        iframe += ' name="{:s}"'.format(str(name))
    if id is not None:
        iframe += ' id="{:s}"'.format(str(id))
    iframe += '></iframe>'
    return iframe


def url_visual(classification, trade_flow, year, origin, destination,
               product, visualization='tree_map', language='en', embed=False):
    """
    Return URL for displaying a visualization in a browser.

    Args:
        classification (str): specifies which product classification to use
            (e.g. 'hs92', 'hs96', 'hs02', 'hs07', 'sitc').
        trade_flow (str): specifies which trade value to show
            (e.g. 'import', 'export').
        year (str): specifies which year or range of years to show
            (e.g. 2015, '2002.2005').
        origin (str): specifies a country of origin ('egy'), whether to show
            all countries ('show'), or whether to sum all imports regardless
            of origin ('all').
        destination (str): specifies a country of origin ('egy'), whether to
            show all countries ('show'), or whether to sum all exports
            regardless of origin ('all').
        product (str): specifies whether to show all products ('show'), sum the
            data regardless of product ('all'), or show a particular product
            designated by a four-digit HS or SITC id.
        visualization (str): specifies which visualization to show. Defaults
            to 'tree_map'.
        language (str): specifies the language used for the visualization.
        embed (bool): specifies whether the embed URL or regular URL is used

    Returns:
        str: URL for viewing the visualization
    """
    if embed:
        src = build_call(language, 'visualize', 'embed', visualization,
                         classification, trade_flow, origin, destination,
                         product, year)
    else:
        src = build_call(language, 'visualize', visualization,
                         classification, trade_flow, origin, destination,
                         product, year)
    return src
