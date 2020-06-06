from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Website, Visitor, MetaWebFeedback, PaidUser, Hotel
from .serializers import WebsiteSerializer, VisitorSerializer, PaidUserSerializer, HotelSerializer
from django.core.exceptions import ObjectDoesNotExist
import json
import re
from email_validator import validate_email, EmailNotValidError
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.parsers import FileUploadParser


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
            category=payload["category"],
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
            user=payload["user"],
            featureOneDesH=payload['featureOneDesH'],
            featureTwoDesH=payload['featureTwoDesH'],
            featureThreeDesH=payload['featureThreeDesH'],
            serviceOne=payload['serviceOne'],
            serviceTwo=payload['serviceTwo'],
            serviceThree=payload['serviceThree'],
            serviceOneDes=payload['serviceOneDes'],
            serviceTwoDes=payload['serviceTwoDes'],
            serviceThreeDes=payload['serviceThreeDes'],
            backgroundColor=payload['backgroundColor']
        )

        # if not website.nameOfSiteH:
        #     return JsonResponse({'error': 'Name of site cannot be empty'},
        #              status=status.HTTP_400_BAD_REQUEST)

        # if len(website.nameOfSiteH)>10:
        #     return JsonResponse({'error': 'Length exceeded'},
        #                         status=status.HTTP_400_BAD_REQUEST)
        # if type(website.nameOfSiteH) != str:
        #     return JsonResponse({'error': 'Please enter valid letter only'},
        #                         status=status.HTTP_400_BAD_REQUEST)
        # if bool(re.search(r'\d', website.nameOfSiteH)):
        #     return JsonResponse({'error': 'Please enter valid letter only'},
        #                         status=status.HTTP_400_BAD_REQUEST)
        # #
        # if not bool(re.search(r'\d{10}', website.phoneC)):
        #     return JsonResponse({'error': 'Please enter valid phone number'},
        #                         status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     # Validate.
        #     valid = validate_email(website.emailC)
        # except EmailNotValidError as e:
        #     # email is not valid, exception message is human-readable
        #     return JsonResponse({'error': 'Please enter valid email'},
        #                         status=status.HTTP_400_BAD_REQUEST)

        serializer = WebsiteSerializer(website)

        return JsonResponse({'website': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@permission_classes([AllowAny])
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
    data = payload['user']
    website = Website.objects.filter(user=data)
    serializer = WebsiteSerializer(website, many=True)
    if website:
        content = {'status': '200', "message": "website found",
                   'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error',
                   "message": "website not found", 'data': 0}
        return JsonResponse(content)


@api_view(["POST"])
@csrf_exempt
def get_hotels(request):
    # payload = json.loads(request.body)
    # user=request.user
    # web = Website.objects.all()
    # print(web)
    # return JsonResponse({web}, safe=False, status=status.HTTP_201_CREATED)
    payload = json.loads(request.body)
    data = payload['user']
    hotels = Hotel.objects.filter(user=data)
    serializer = HotelSerializer(hotels, many=True)
    if hotels:
        content = {'status': '200', "message": "hotels found",
                   'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error',
                   "message": "website not found", 'data': 0}
        return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def search_hotels(request, id):
    hotels = Hotel.objects.filter(id=id)
    serializer = HotelSerializer(hotels, many=True)
    if hotels:
        content = {'status': '200', "message": "hotels found",
                   'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error',
                   "message": "hotel not found", 'data': 0}
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
def update_website(request, id):
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


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def get_review(request, shopid):

    try:
        visitor = Visitor.objects.filter(shopId=shopid)
        serializer = VisitorSerializer(visitor, many=True)
        return JsonResponse({'feedback': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([AllowAny])
def delete_feedback(request, id):
    try:
        feedback = Visitor.objects.get(id=id)
        feedback.delete()
        return JsonResponse({'message': "feedback deleted successfully"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def add_message(request):
    payload = json.loads(request.body)
    print(payload)
    try:
        feedback = MetaWebFeedback.objects.create(
            name=payload["name"],
            email=payload["email"],
            message=payload["message"])

        return JsonResponse({'visitor': "Successfully submitted feedback"}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_exempt
def search(request):
    payload = json.loads(request.body)
    try:
        keyword = payload['keyword']
        location = payload['location']
        category = payload['category']
        querry_list = Website.objects.order_by('created_date')
        if(keyword):
            querry_list = querry_list.filter(nameOfSiteH__icontains=keyword)
        if(location):
            querry_list = querry_list.filter(addressC__icontains=keyword)
        if(category):
            querry_list = querry_list.filter(category__icontains=keyword)
        print(querry_list)
        serializer = WebsiteSerializer(querry_list, many=True)
        return JsonResponse({'websites': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string(
        'email/user_reset_password.html', context)
    email_plaintext_message = render_to_string(
        'email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "bibeklama67@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()

    # for paid users


@api_view(["POST"])
@csrf_exempt
def set_paid_user(request):
    payload = json.loads(request.body)
    print(payload)
    try:
        paiduser = PaidUser.objects.create(
            username=payload["username"]
        )
        print('vayoo')
        serializer = PaidUserSerializer(paiduser)
        return JsonResponse({'paidUser': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def search_paid_user(request):
    payload = json.loads(request.body)
    try:
        print(payload)
        user = PaidUser.objects.filter(username=payload['username'])
        print(user)
        serializer = PaidUserSerializer(user, many=True)
        return JsonResponse({'paidUser': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)

# for hotel website


@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
@permission_classes(FileUploadParser)
def add_hotel(request):
    print(request)
    hotel_serializer = HotelSerializer(data=request.data)
    print(hotel_serializer)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse({'message': "hotel website addded success"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)
