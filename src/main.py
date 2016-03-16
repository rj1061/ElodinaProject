from ebayAPICall import ebayAPICall
from getListPrice import getListPrice
import pprint
import sys

ebay = ebayAPICall()
dictEbay = ebay.getCompletedItemsByKeyword(sys.argv[1]).dict()

if sys.argv[2] == "print_data":
    pprint.pprint(dictEbay)
else:
    priceList = getListPrice(dictEbay).getList()
    print float(sum(priceList)/len(priceList))
