import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.PersonService import PersonService
from neoapp.services.AccountService import AccountService
import logging

logger = logging.getLogger(__name__)

# Khởi tạo driver một lần và sử dụng chung
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def update_person(request, person_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        # Lấy các giá trị từ request body
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        birth_date = data.get('birth_date')
        gender = data.get('gender')
        # Khởi tạo PersonService
        person_service = PersonService(neo4j_driver)
        try:
            updated_person = person_service.update_person(
                person_id, name, email, phone, address, birth_date, gender
            )
        except Exception as e:
            logger.error(f"Error updating person: {e}")
            return JsonResponse({'error': 'Update failed due to server error'}, status=500)

        if updated_person:
            return JsonResponse({
                'message': 'Person updated successfully',
                'person': {
                    'name': updated_person.get('Name'),
                    'email': updated_person.get('Email'),
                    'phone': updated_person.get('Phone'),
                    'address': updated_person.get('Address'),
                    'birth_date': updated_person.get('BirthDate'),
                    'gender': updated_person.get('Gender'),
                }
            })
        else:
            return JsonResponse({'error': 'Update failed'}, status=400)
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            account_service = AccountService(neo4j_driver)
            person_data = account_service.login(username, password)

            if person_data:
                return JsonResponse({'person': person_data})
            else:
                logger.warning(f"Invalid credentials for username: {username}")
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            logger.error(f"Error during login: {str(e)}")
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
