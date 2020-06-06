
from .models import Website, Visitor,PaidUser,Hotel
from rest_framework import serializers


###### IMPORT YOUR USER MODEL ######



class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'nameOfSiteH', 'headingOneH', 'descriptionOneH', 'headingTwoH', 'descriptionTwoH',
                  'headingThreeH', 'descriptionThreeH', 'featureOneH', 'featureTwoH', 'featureThreeH', 'introductionA', 'whatWeDoA', 'titleC', 'emailC', 'descriptionC', 'phoneC', 'addressC', 'user', 'created_date', 'category', 'featureOneDesH', 'featureTwoDesH', 'featureThreeDesH', 'serviceOne', 'serviceOneDes', 'serviceTwo', 'serviceTwoDes', 'serviceThree', 'serviceThreeDes', 'backgroundColor'
                  ]


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id', 'user', 'first_name', 'last_name',
                  'email', 'address', 'message', 'shopId']

class PaidUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidUser
        fields = ['id', 'username','created_date']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
