from ebayAPICall import ebayAPICall
import pprint

ebay = ebayAPICall()
dictEbay = ebay.getCompletedItemsByKeyword("guitar").dict()

pprint.pprint(dictEbay)
