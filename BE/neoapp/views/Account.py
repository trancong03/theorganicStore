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
@csrf_exempt
def SignUp_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            name = data.get('name')
            email= data.get('email')
            phone = data.get('phone')
            admin = data.get('admin')

            account_service = AccountService(neo4j_driver)
            results = account_service.create_person_and_account(name, email, phone, username, password, admin)
            if results['success']:
                return JsonResponse({'results': results['account']}, status=201)  
            else:
                return JsonResponse({'message': results['message']}, status=400) 
        except Exception as e:
            logger.error(f"Error during login: {str(e)}")
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            old_password = data.get('old_password')
            new_password = data.get('new_password')
            account_service  = AccountService(neo4j_driver)
            print(f"Data{data}")
            account = account_service.reset_password(username,old_password,new_password)
            if account:
                return JsonResponse({'message':'Reset password successfully'})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            print(f"Error in reset_password: {e}")
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)