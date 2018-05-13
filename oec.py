import requests
import csv


def build_call(*args):
    """Create a URL for a call to the OEC API"""
    call = 'http://atlas.media.mit.edu/'
    for val in args:
        call += str(val) + '/'
    return call


def request_data(call_url):
    """Return the results of an API request"""
    r = requests.get(call_url)
    response_dict = r.json()
    json_list = response_dict['data']  # list of dicts containing data
    return json_list


def get_countries():
    """Return the results of an API request for country attributes"""
    call = build_call('attr', 'country')
    return request_data(call)


def get_products(classification):
    """Return the results of an API request for product descriptions"""
    call = build_call('attr', classification)
    return request_data(call)


def get_trade_data(classification, trade_flow, year, origin, destination,
                   product):
    """Return the results of an API request for trade data"""
    call = build_call(classification, trade_flow, year, origin, destination,
                      product)
    return request_data(call)


def get_header(json_list):
    """Return a list of header strings for the give list of dictionaries"""
    header = set()
    for dict in json_list:
        header.update(dict.keys())
    return list(header)


def data_to_csv(json_list, filename='out.csv'):
    """Convert received list of JSON objects into a csv file"""
    with open('out.csv', 'w') as csvfile:
        header = get_header(json_list)
        cw = csv.writer(csvfile)
        cw.writerow(header)
        for dict in json_list:
            row = dict_to_list(dict, header)
            cw.writerow(row)


def dict_to_list(dict, header):
    """Convert a dictionary into a list in the order specified by the header"""
    row = []
    for field in header:
        if field in dict:
            row.append(str(dict[field]))
        else:
            row.append(None)
    return row
