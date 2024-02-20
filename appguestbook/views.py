from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TblGuest, TblEvent
from .serializers import EventSerializer, GuestSerializer
import requests
import psycopg2
import mysql.connector
from django.conf import settings
from django.utils import timezone

def index_view(request):
    return render(request, 'index.html')

class EventGet(APIView):
    def get(self, request):
        api_keys = TblEvent.objects.all()

        if not api_keys.exists():
            response_data = {
                "success": True,
                "message": "success",
                "data": [
                    {
                        "feedback": "N"
                    }
                ]
            }
            return Response(response_data)
        
        serializer = EventSerializer(api_keys, many=True)
        response_data = {
            "Success": True,
            "Message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    
class EventDetailGet(APIView):
    def get(self, request, id):
        api_keys = TblEvent.objects.filter(id=id)

        if not api_keys.exists():
            response_data = {
                "success": True,
                "message": "success",
                "data": [
                    {
                        "feedback": "N"
                    }
                ]
            }
            return Response(response_data)
        
        serializer = EventSerializer(api_keys, many=True)
        response_data = {
            "Success": True,
            "Message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    
class EventPost(APIView):
    def post(self, request):
        name = request.data.get('name')
        location = request.data.get('location')
        date = request.data.get('date')
        error_messages = {}
        
        if not location:
            error_messages['location'] = 'location is required.'
        if not name:
            error_messages['name'] = 'name is required.'
        if not date:
            error_messages['date'] = 'date is required.'

        if not error_messages:
            current_timestamp = timezone.now()
            formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

            new_answer = TblEvent.objects.create(name=name, date=date, location=location, created_by="admin", updated_by = "admin", created_at = formatted_timestamp,  updated_at = formatted_timestamp)
            response_data = {
                "name": name,
                "location": location,
                "date": date,
                "created_by": "admin",
                "updated_by": "admin",
            }
            
            return Response(response_data)
        else:
            response_data = {
                "success": False,
                "message": "Failed",
                "data": error_messages
            }
            return Response(response_data)
        
class EventPut(APIView):
    def put(self, request, id):
        name = request.data.get('name')
        location = request.data.get('location')
        date = request.data.get('date')
        error_messages = {}
        
        if not location:
            error_messages['location'] = 'location is required.'
        if not name:
            error_messages['name'] = 'name is required.'
        if not date:
            error_messages['date'] = 'date is required.'

        if not error_messages:
            current_timestamp = timezone.now()
            formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

            try:
                item = TblEvent.objects.get(id=id)
                item.name = name
                item.date = date
                item.location = location
                item.updated_at = formatted_timestamp
                item.save()

                response_data = {
                    "id": item.id,
                    "name": item.name,
                    "location": item.location,
                    "date": item.date,
                    "created_by": item.created_by,
                    "updated_by": "admin",
                }
                return Response(response_data)
            except TblEvent.DoesNotExist:
                response_data = {
                    "success": False,
                    "message": "Item not found.",
                    "data": {}
                }
                return Response(response_data, status=404)
        else:
            response_data = {
                "success": False,
                "message": "Failed",
                "data": error_messages
            }
            return Response(response_data)
        
class EventDelete(APIView):
    def delete(self, request, id):
        TblEvent.objects.filter(id = id).delete()

        response_data = {
            "success": True,
            "message": "Delete Data successfully",
        }
        return Response(response_data, status=200)
    
class GuestGet(APIView):
    def get(self, request):
        api_keys = TblGuest.objects.all()

        if not api_keys.exists():
            response_data = {
                "success": True,
                "message": "success",
                "data": [
                    {
                        "feedback": "N"
                    }
                ]
            }
            return Response(response_data)
        
        serializer = GuestSerializer(api_keys, many=True)
        response_data = {
            "Success": True,
            "Message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    
class GuestDetailGet(APIView):
    def get(self, request, id):
        api_keys = TblGuest.objects.filter(id=id)

        if not api_keys.exists():
            response_data = {
                "success": True,
                "message": "success",
                "data": [
                    {
                        "feedback": "N"
                    }
                ]
            }
            return Response(response_data)
        
        serializer = GuestSerializer(api_keys, many=True)
        response_data = {
            "Success": True,
            "Message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    
class GuestDetailByEventGet(APIView):
    def get(self, request, id):
        api_keys = TblGuest.objects.filter(event_id=id)

        if not api_keys.exists():
            response_data = {
                "success": True,
                "message": "success",
                "data": [
                    {
                        "feedback": "N"
                    }
                ]
            }
            return Response(response_data)
        
        serializer = GuestSerializer(api_keys, many=True)
        response_data = {
            "Success": True,
            "Message": "success",
            "data": serializer.data
        }
        return Response(response_data)
    
class GuestPost(APIView):
    def post(self, request):
        name = request.data.get('name')
        event_id = request.data.get('event_id')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        froms = request.data.get('froms')
        error_messages = {}
        
        if not email:
            error_messages['email'] = 'email is required.'
        if not name:
            error_messages['name'] = 'name is required.'
        if not phone_number:
            error_messages['phone_number'] = 'phone_number is required.'
        if not froms:
            error_messages['froms'] = 'froms is required.'

        if not error_messages:
            current_timestamp = timezone.now()
            formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

            new_answer = TblGuest.objects.create(event_id=event_id, name=name, email=email, phone_number=phone_number, froms=froms, date_time = formatted_timestamp)
            response_data = {
                "name": name,
                "email": email,
                "phone_number": phone_number,
                froms: froms,
            }
            
            return Response(response_data)
        else:
            response_data = {
                "success": False,
                "message": "Failed",
                "data": error_messages
            }
            return Response(response_data)
        
class GuestPut(APIView):
    def put(self, request, id):
        name = request.data.get('name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        froms = request.data.get('froms')
        error_messages = {}
        
        if not email:
            error_messages['email'] = 'email is required.'
        if not name:
            error_messages['name'] = 'name is required.'
        if not phone_number:
            error_messages['phone_number'] = 'phone_number is required.'
        if not froms:
            error_messages['froms'] = 'froms is required.'

        if not error_messages:
            current_timestamp = timezone.now()
            formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

            try:
                item = TblGuest.objects.get(id=id)
                item.name = name
                item.email = email
                item.phone_number = phone_number
                item.froms = froms
                item.date_time = formatted_timestamp
                item.save()

                response_data = {
                    "id": item.id,
                    "name": item.name,
                    "email": item.email,
                    "phone_number": item.phone_number,
                    "froms": item.froms,
                    "updated_by": "admin",
                }
                return Response(response_data)
            except TblGuest.DoesNotExist:
                response_data = {
                    "success": False,
                    "message": "Item not found.",
                    "data": {}
                }
                return Response(response_data, status=404)
        else:
            response_data = {
                "success": False,
                "message": "Failed",
                "data": error_messages
            }
            return Response(response_data)
        
class GuestDelete(APIView):
    def delete(self, request, id):
        TblGuest.objects.filter(id = id).delete()

        response_data = {
            "success": True,
            "message": "Delete Data successfully",
        }
        return Response(response_data, status=200)