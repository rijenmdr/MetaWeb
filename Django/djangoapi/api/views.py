from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Website,Visitor
from .serializers import WebsiteSerializer,VisitorSerializer
from django.core.exceptions import ObjectDoesNotExist
import json

@api_view(["GET"])
@permission_classes([AllowAny])
@csrf_exempt
def welcome(request):
    content = {"message": "Test works"}
    return JsonResponse(content)

@api_view(["POST"])
@csrf_exempt
def add_website(request):
    payload = json.loads(request.body)
    user = request.user
    # web = Website.objects.filter(user=user).count()
    try:
        website = Website.objects.create(
            nameOfSiteH=payload["nameOfSiteH"],
            headingOneH=payload["headingOneH"],
            descriptionOneH=payload["descriptionOneH"],
            headingTwoH=payload["headingTwoH"],
            descriptionTwoH=payload["descriptionTwoH"],
            headingThreeH=payload["headingThreeH"],
            descriptionThreeH=payload["descriptionThreeH"],
            featureOneH=payload["featureOneH"],
            featureTwoH=payload["featureTwoH"],
            featureThreeH=payload["featureThreeH"],
            introductionA=payload["introductionA"],
            whatWeDoA=payload["whatWeDoA"],
            titleC=payload["titleC"],
            emailC=payload["emailC"],
            descriptionC=payload["descriptionC"],
            phoneC=payload["phoneC"],
            addressC=payload["addressC"],
            user=payload["user"]
        )
        serializer = WebsiteSerializer(website)

        return JsonResponse({'website': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@csrf_exempt
def get_website(request, id):
    # user = request.user.id
    try:
        print(id)
        website = Website.objects.get(id=id)
        print(website)
        serializer = WebsiteSerializer(website)
        return JsonResponse({'website': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def get_dashboard(request):
    # payload = json.loads(request.body)
    # user=request.user
    # web = Website.objects.all()
    # print(web)
    # return JsonResponse({web}, safe=False, status=status.HTTP_201_CREATED)
    payload = json.loads(request.body)
    data=payload['user']
    website = Website.objects.filter(user=data)
    serializer = WebsiteSerializer(website, many=True)
    if website:
        content = {'status': '200', "message": "website found", 'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error', "message": "website not found", 'data': 0}
        return JsonResponse(content)
    
@api_view(["DELETE"])
@csrf_exempt
def delete_website(request, id):
    try:
        website = Website.objects.get(id=id)
        website.delete()
        return JsonResponse({'message': "Website deleted successfully"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
@csrf_exempt
def update_website(request,id):
    payload = json.loads(request.body)
    user = request.user.id
    print(id)
    try:
        website_item = Website.objects.filter(id=id)
        website_item.update(**payload)
        website = Website.objects.get(id=id)
        serializer = WebsiteSerializer(website)
        return JsonResponse({'websites': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def add_review(request):
    payload = json.loads(request.body)
    print(payload)
    # user = request.user
    # web = Website.objects.filter(user=user).count()
    try:
        website = Website.objects.get(id=payload["shopId"])
        visitor = Visitor.objects.create(
            user=website,
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            email=payload["email"],
            address=payload["address"],
            message=payload["message"],
            shopId=payload["shopId"]
        )
        print('vayoo')
        serializer = VisitorSerializer(visitor)

        return JsonResponse({'visitor': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)
