from rest_framework import serializers
from CupDraft.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Country
        fields = ('CountryId','CountryFlag','CountryName','CountryCode','CountryRank','CountryConf')
        

