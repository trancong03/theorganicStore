import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AdminUserService import AdminUserService
import logging

logger = logging.getLogger(__name__)

# Initialize the Neo4j driver once and use it across requests
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract variables from the request body
            id_person = data.get('person_id')
            name = data.get('name')
            address = data.get('address')
            phone = data.get('phone')
            birth = data.get('birth')
            gender = data.get('gender')
            
            # Call the service with extracted variables
            user_service = AdminUserService(neo4j_driver)
            result = user_service.add_user(
                id_person, 
                name, 
                address, 
                phone, 
                birth, 
                gender
            )
            
            if result['success']:
                return JsonResponse({'user': result['user']}, status=201)
            else:
                return JsonResponse({'message': result.get('message', 'Failed to add user')}, status=400)
        except Exception as e:
            logger.error(f"Error in add_user: {e}")
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        try:
            # Retrieve all users through the service
            user_service = AdminUserService(neo4j_driver)
            result = user_service.get_all_users()
            
            if result['success']:
                return JsonResponse({'users': result['data']}, status=200)
            else:
                return JsonResponse({'message': 'No users found.'}, status=404)
        except Exception as e:
            logger.error(f"Error in get_all_users: {e}")
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
