from ebayAPICall import ebayAPICall
import pprint
import sys

ebay = ebayAPICall()
dictEbay = ebay.getCompletedItemsByKeyword(sys.argv[1]).dict()

pprint.pprint(dictEbay)
