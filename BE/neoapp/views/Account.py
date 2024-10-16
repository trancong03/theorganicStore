import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AccountService import AccountService
import logging

logger = logging.getLogger(__name__)

# Khởi tạo driver một lần và sử dụng chung
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

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
