from rest_framework import serializers
from .models import Website,Visitor


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'nameOfSiteH', 'headingOneH', 'descriptionOneH', 'headingTwoH', 'descriptionTwoH',
                  'headingThreeH', 'descriptionThreeH', 'featureOneH', 'featureTwoH', 'featureThreeH', 'introductionA', 'whatWeDoA', 'titleC', 'emailC', 'descriptionC', 'phoneC', 'addressC', 'user','created_date'
                  ]
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visitor
        fields=['id','user','first_name','last_name','email','address','message','shopId']