import datetime
import sys
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

class ebayAPICall:

    def findItemsAdvanced(keywords):
        try:
            response = api.execute('findItemsAdvanced', {'keywords': sys.argv[1]})

            print type(response)
            assert(response.reply.ack == 'Success')
            assert(type(response.reply.timestamp) == datetime.datetime)
            assert(type(response.reply.searchResult.item) == list)

            item = response.reply.searchResult.item[0]
            assert(type(item.listingInfo.endTime) == datetime.datetime)
            assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

        return response

    def getCompletedItemsByKeyword(keywords):
        try:
            response = api.execute('findCompletedItems', {'keywords': keywords})
            print type(response)
            assert(response.reply.ack == 'Success')
            assert(type(response.reply.timestamp) == datetime.datetime)
            assert(type(response.reply.searchResult.item) == list)

            item = response.reply.searchResult.item[0]
            assert(type(item.listingInfo.endTime) == datetime.datetime)
            assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

        return response

    def __init__(self, appid='Elodina-Elodina-PRD-dd2d4c776-3a2daa78', config_file=None):
        self.api = Connection(appid, config_file)
