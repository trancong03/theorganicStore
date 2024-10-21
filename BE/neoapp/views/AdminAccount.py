import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AdminAccountService import AdminAccountService  # Import the corresponding service for Account

logger = logging.getLogger(__name__)

# Initialize the Neo4j driver once and use it across requests
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def add_account(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate input data
            id_account = data.get('id_account')
            role = data.get('role')
            username = data.get('username')
            password = data.get('password')

            if not all([id_account, role, username, password]):
                return JsonResponse({'message': 'All fields are required.'}, status=400)

            # Create account
            account_service = AdminAccountService(neo4j_driver)
            result = account_service.add_account(
                id_account=id_account,
                role=role,
                username=username,
                password=password
            )
            
            if result['success']:
                return JsonResponse({'message': 'Account created successfully'}, status=201)
            else:
                return JsonResponse({'message': 'Failed to create account'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
        except Exception as e:
            logger.error("Error adding account: %s", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_all_accounts(request):
    if request.method == 'GET':
        try:
            account_service = AdminAccountService(neo4j_driver)
            result = account_service.get_all_accounts()
            if result['success']:
                return JsonResponse({'accounts': result['data']['accounts']}, status=200)
            else:
                return JsonResponse({'message': 'No accounts found'}, status=404)
        except Exception as e:
            logger.error("Error retrieving accounts: %s", str(e))
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)
