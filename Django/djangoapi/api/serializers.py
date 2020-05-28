from rest_framework import serializers
from .models import Website


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'nameOfSiteH', 'headingOneH', 'descriptionOneH', 'headingTwoH', 'descriptionTwoH',
                  'headingThreeH', 'descriptionThreeH', 'featureOneH', 'featureTwoH', 'featureThreeH', 'introductionA', 'whatWeDoA', 'titleC', 'emailC', 'descriptionC', 'phoneC', 'addressC', 'user','created_date'
                  ]
