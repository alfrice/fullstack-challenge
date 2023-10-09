from django.db import models

from django.db import models

# Create your models here.
from django.db import models
from rest_framework import serializers


# Create your models here.
class Listing(models.Model):
    Address = models.CharField(max_length=200)
    Longitude = models.CharField(max_length=200)
    Latitude = models.CharField(max_length=200)
    Zip = models.CharField(max_length=200)
    REC_TYPE = models.CharField(max_length=200)
    PIN = models.CharField(max_length=200)
    OVACLS = models.CharField(max_length=200)
    CLASS_DESCRIPTION = models.CharField(max_length=200)
    CURRENT_LAND = models.CharField(max_length=200)
    CURRENT_BUILDING = models.CharField(max_length=200)
    CURRENT_TOTAL = models.CharField(max_length=200)
    ESTIMATED_MARKET_VALUE = models.CharField(max_length=200)
    PRIOR_LAND = models.CharField(max_length=200)
    PRIOR_BUILDING = models.CharField(max_length=200)
    PRIOR_TOTAL = models.CharField(max_length=200)
    PPRIOR_LAND = models.CharField(max_length=200)
    PPRIOR_BUILDING = models.CharField(max_length=200)
    PPRIOR_TOTAL = models.CharField(max_length=200)
    PPRIOR_YEAR = models.CharField(max_length=200)
    TOWN = models.CharField(max_length=200)
    VOLUME = models.CharField(max_length=200)
    LOC = models.CharField(max_length=200)
    TAX_CODE = models.CharField(max_length=200)
    NEIGHBORHOOD = models.CharField(max_length=200)
    HOUSENO = models.CharField(max_length=200)
    DIR = models.CharField(max_length=200)
    STREET = models.CharField(max_length=200)
    SUFFIX = models.CharField(max_length=200)
    APT = models.CharField(max_length=200)
    CITY = models.CharField(max_length=200)
    RES_TYPE = models.CharField(max_length=200)
    BLDG_USE = models.CharField(max_length=200)
    APT_DESC = models.CharField(max_length=200)
    COMM_UNITS = models.CharField(max_length=200)
    EXT_DESC = models.CharField(max_length=200)
    FULL_BATH = models.CharField(max_length=200)
    HALF_BATH = models.CharField(max_length=200)
    BSMT_DESC = models.CharField(max_length=200)
    ATTIC_DESC = models.CharField(max_length=200)
    AC = models.CharField(max_length=200)
    FIREPLACE = models.CharField(max_length=200)
    GAR_DESC = models.CharField(max_length=200)
    AGE = models.CharField(max_length=200)
    BUILDING_SQ_FT = models.CharField(max_length=200)
    LAND_SQ_FT = models.CharField(max_length=200)
    BLDG_SF = models.CharField(max_length=200)
    UNITS_TOT = models.CharField(max_length=200)
    MULTI_SALE = models.CharField(max_length=200)
    DEED_TYPE = models.CharField(max_length=200)
    SALE_DATE = models.CharField(max_length=200)
    SALE_AMOUNT = models.CharField(max_length=200)
    APPCNT = models.CharField(max_length=200)
    APPEAL_A = models.CharField(max_length=200)
    APPEAL_A_STATUS = models.CharField(max_length=200)
    APPEAL_A_RESULT = models.CharField(max_length=200)
    APPEAL_A_REASON = models.CharField(max_length=200)
    APPEAL_A_PIN_RESULT = models.CharField(max_length=200)
    APPEAL_A_PROPAV = models.CharField(max_length=200)
    APPEAL_A_CURRAV = models.CharField(max_length=200)
    APPEAL_A_RESLTDATE = models.CharField(max_length=200)


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ['Address', 'Zip', 'description', 'completed', 'created_at']
