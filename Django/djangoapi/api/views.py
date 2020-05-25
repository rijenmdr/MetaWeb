from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Website, Member, Owner
from .serializers import BookSerializer, AuthorSerializer, OwnerSerializer, WebsiteSerializer
from django.core.exceptions import ObjectDoesNotExist
import json


# Create your views here.
@api_view(["GET"])
def test(request):
    return render('<h1>ahahhahaha</h1>')


@api_view(["GET"])
@csrf_exempt
def welcome(request):
    content = {"message": "Test works"}
    return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    if books:
        content = {'status': '200', "message": "Books found",
                   'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error', "message": "Books not found", 'data': 0}
        return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
def get_all_authors(request):
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    if author:
        content = {'status': '200', "message": "Authors found",
                   'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error',
                   "message": "Authors not found", 'data': 0}
        return JsonResponse(content)


@api_view(["POST"])
@csrf_exempt
def add_book(request):
    payload = json.loads(request.body)
    user = request.user
    print(payload)
    try:
        book = Website.objects.create(
            title=payload["title"],
            description=payload["description"],
            menus=payload["menus"],
            added_by=user,

        )
        print(book)
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
@csrf_exempt
def update_book(request, book_id):
    payload = json.loads(request.body)
    user = request.user.id
    try:
        book_item = Book.objects.find(id=book_id)
        # book_item.update(
        #     title=payload["title"],
        #     description=payload["description"],
        #     added_by=AuthorSerializer,
        # )
        book_item.update(**payload)
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
@csrf_exempt
def delete_book(request, book_id):
    # user = request.user.id
    try:
        book_item = Book.objects.get(id=book_id)
        # book_item.update(
        #     title=payload["title"],
        #     description=payload["description"],
        #     added_by=AuthorSerializer,
        # )
        book_item.delete()
        return JsonResponse({'message': "Book deleted successfully"}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@csrf_exempt
def get_book_by_id(request, book_id):
    # user = request.user.id
    try:
        print(book_id)
        book_item = Book.objects.get(id=book_id)
        print(book_item)
        serializer = BookSerializer(book_item)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def add_owner(request):
    payload = json.loads(request.body)
    user = request.user
    print(payload)
    try:

        owner = Owner.objects.create(
            username=payload["username"],
            email=payload["email"],
            phone=payload["phone"]


        )

        serializer = OwnerSerializer(owner)
        return JsonResponse({'owner': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def add_website(request):
    payload = json.loads(request.body)
    user = request.user
    print(payload)
    try:

        owner = Website.objects.create(
            title=payload["title"],
            description=payload["description"],
            user=payload["username"],
            menus=payload["menus"],



        )
        print("vayo")

        serializer = WebsiteSerializer(owner)
        return JsonResponse({'owner': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': "Something went wrong"}, safe=False, status=status.HTTP_404_NOT_FOUND)
