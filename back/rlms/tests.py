from django.test import TestCase

from rlms.models import Listing

test_listing ={"Address": "210 N JUSTINE ST, CHICAGO, IL", "Longitude": "-87.6656354999999", "Latitude": "41.8857718", "Zip": "60607", "REC_TYPE": "A-HD", "PIN": "17083150310000", "OVACLS": "211", "CLASS_DESCRIPTION": "Two to Six Apartments, Over 62 Years                                                         ", "CURRENT_LAND": "15,000", "CURRENT_BUILDING": "44,582", "CURRENT_TOTAL": "59,582", "ESTIMATED_MARKET_VALUE": "595,820", "PRIOR_LAND": "12,500", "PRIOR_BUILDING": "44,601", "PRIOR_TOTAL": "57,101", "PPRIOR_LAND": "12,500", "PPRIOR_BUILDING": "44,601", "PPRIOR_TOTAL": "57,101", "PPRIOR_YEAR": "2013", "TOWN": "77", "VOLUME": "590", "LOC": "CITY", "TAX_CODE": "77020", "NEIGHBORHOOD": "131", "HOUSENO": "210", "DIR": "N", "STREET": "JUSTINE ", "SUFFIX": "ST", "APT": "", "CITY": "CHICAGO", "RES_TYPE": "Two Story        ", "BLDG_USE": "Multi Family  ", "APT_DESC": "2", "COMM_UNITS": "0", "EXT_DESC": "Masonry    ", "FULL_BATH": "2", "HALF_BATH": "0", "BSMT_DESC": "Partial and Unfinished", "ATTIC_DESC": "None", "AC": "2", "FIREPLACE": "0", "GAR_DESC": "", "AGE": "127", "BUILDING_SQ_FT": "3007", "LAND_SQ_FT": "5000", "BLDG_SF": "", "UNITS_TOT": "", "MULTI_SALE": "0", "DEED_TYPE": "0", "SALE_DATE": "", "SALE_AMOUNT": "0", "APPCNT": "0", "APPEAL_A": "0", "APPEAL_A_STATUS": "", "APPEAL_A_RESULT": "", "APPEAL_A_REASON": "0", "APPEAL_A_PIN_RESULT": "", "APPEAL_A_PROPAV": "0", "APPEAL_A_CURRAV": "0", "APPEAL_A_RESLTDATE": ""}

class ListingTestCase(TestCase):
    def setUp(self):
        Listing.objects.create(**test_listing)

    def test_animals_can_speak(self):
        """Listings that can speak are correctly identified"""
        listing = Listing.objects.get(Address="210 N JUSTINE ST, CHICAGO, IL")

        self.assertEqual(listing.Address, '210 N JUSTINE ST, CHICAGO, IL')
