import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.PersonService import PersonService
from neoapp.services.AccountService import AccountService
import logging

logger = logging.getLogger(__name__)

neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def update_person(request, person_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        birth_date = data.get('birth_date')
        gender = data.get('gender')
        person_service = PersonService(neo4j_driver)
        try:
            updated_person = person_service.update_person( person_id, name, email, phone, address, birth_date, gender)
        except Exception as e:
            logger.error(f"Error updating person: {e}")
            return JsonResponse({'error': 'Update failed due to server error'}, status=500)
        if updated_person:
            return JsonResponse({'person': updated_person}, status=200)  
        else:
            return JsonResponse({'error': 'Update failed'}, status=400)
        
@csrf_exempt
def update_image_person(request, person_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        avatar = data.get('avatar')

        person_service = PersonService(neo4j_driver)
        updated_person = person_service.update_avatar_person( person_id,avatar)
        if updated_person:
            return JsonResponse({'person': updated_person}, status=200)  
        else:
            return JsonResponse({'error': 'Update failed'}, status=400)