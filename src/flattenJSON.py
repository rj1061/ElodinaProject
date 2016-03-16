from pandas.io.json import json_normalize

def flattenJSONPandas(json):
    json_normalize(json)
    return json

def flattenJSON(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + str(i) + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)

     flatten(y)
     return out
