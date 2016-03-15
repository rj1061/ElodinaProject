import datetime
import sys
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

try:
    api = Connection(appid='Elodina-Elodina-PRD-dd2d4c776-3a2daa78', config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': sys.argv[1]})

    print type(response)
    f = open('response', 'w')
    f.write(response.json())
    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)
    print("Success\n")

except ConnectionError as e:
    print(e)
    print(e.response.dict())