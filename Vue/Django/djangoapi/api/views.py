from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Website
from .serializers import WebsiteSerializer
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth.models import User
# from django.dispatch import receiver
# # from django_rest_passwordreset.signals import reset_password_token_created
# # from django.core.mail import EmailMultiAlternatives
# # from django.template.loader import render_to_string
# # # from vuedj.constants import site_url, site_full_name, site_shortcut_name
# # from rest_framework.views import APIView
# # from rest_framework import parsers, renderers, status
# # from rest_framework.response import Response
# # from .serializers import CustomTokenSerializer
# # from django_rest_passwordreset.models import ResetPasswordToken
# # from django_rest_passwordreset.views import get_password_reset_token_expiry_time
# # from django.utils import timezone
# # from datetime import timedelta
# from django.core.mail import EmailMultiAlternatives
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created

@api_view(["GET"])
@csrf_exempt
def welcome(request):
    content = {"message": "Test works"}
    return JsonResponse(content)

@api_view(["POST"])
@csrf_exempt
def add_website(request):
    payload = json.loads(request.body)
    user = request.user
    print(payload)
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
        print(serializer.data)
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


@api_view(["PUT"])
@csrf_exempt
def update_website(request,id):
    payload = json.loads(request.body)
    user = request.user.id
    try:
        website_item = Website.objects.find(id=id)
        website_item.update(**payload)
        website = Website.objects.get(id=id)
        serializer = WebsiteSerializer(website)
        return JsonResponse({'websites': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


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


# class CustomPasswordResetView:
#     @receiver(reset_password_token_created)
#     def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
#         """
#           Handles password reset tokens
#           When a token is created, an e-mail needs to be sent to the user
#         """
#         # send an e-mail to the user
#         context = {
#             'current_user': reset_password_token.user,
#             'username': reset_password_token.user.username,
#             'email': reset_password_token.user.email,
#             'reset_password_url': "{}/password-reset/{}".format(site_url, reset_password_token.key),
#             'site_name': site_shortcut_name,
#             'site_domain': site_url
#         }
#
#         # render email text
#         email_html_message = render_to_string('email/user_reset_password.html', context)
#         email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
#
#         msg = EmailMultiAlternatives(
#             # title:
#             "Password Reset for {}".format(site_full_name),
#             # message:
#             email_plaintext_message,
#             # from:
#             "noreply@{}".format(site_url),
#             # to:
#             [reset_password_token.user.email]
#         )
#         msg.attach_alternative(email_html_message, "text/html")
#         msg.send()
#
#
# class CustomPasswordTokenVerificationView(APIView):
#     """
#       An Api View which provides a method to verifiy that a given pw-reset token is valid before actually confirming the
#       reset.
#     """
#     throttle_classes = ()
#     permission_classes = ()
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
#     renderer_classes = (renderers.JSONRenderer,)
#     serializer_class = CustomTokenSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         token = serializer.validated_data['token']
#
#         # get token validation time
#         password_reset_token_validation_time = get_password_reset_token_expiry_time()
#
#         # find token
#         reset_password_token = ResetPasswordToken.objects.filter(key=token).first()
#
#         if reset_password_token is None:
#             return Response({'status': 'invalid'}, status=status.HTTP_404_NOT_FOUND)
#
#         # check expiry date
#         expiry_date = reset_password_token.created_at + timedelta(hours=password_reset_token_validation_time)
#
#         if timezone.now() > expiry_date:
#             # delete expired token
#             reset_password_token.delete()
#             return Response({'status': 'expired'}, status=status.HTTP_404_NOT_FOUND)
#
#         # check if user has password to change
#         if not reset_password_token.user.has_usable_password():
#             return Response({'status': 'irrelevant'})
#
#         return Response({'status': 'OK'})

# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }
#
#     # render email text
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
#
#     msg = EmailMultiAlternatives(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()


from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
from .serializers import WebsiteSerializer
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters




class WebsiteListView(generics.ListAPIView):
    serializer_class = WebsiteSerializer
    queryset = Website.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['nameOfSiteH']
