import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AdminStoreService import AdminStoreService  # Giả sử bạn có service tương ứng cho Store

logger = logging.getLogger(__name__)

# Khởi tạo driver một lần và sử dụng chung
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def add_store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Kiểm tra dữ liệu đầu vào
            name = data.get('name')
            address = data.get('address')
            email = data.get('email')
            hotline = data.get('hotline')

            if not all([name, address, email, hotline]):
                return JsonResponse({'message': 'All fields are required.'}, status=400)

            # Tạo cửa hàng
            store_service = AdminStoreService(neo4j_driver)
            store = store_service.add_store(
                name=name,
                address=address,
                email=email,
                hotline=hotline
            )
            
            return JsonResponse({'id': store.id, 'name': store.name}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
        except Exception as e:
            logger.error("Error adding store: %s", str(e))
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_all_stores(request):
    if request.method == 'GET':
        try:
            store_service = AdminStoreService(neo4j_driver)
            result = store_service.get_all_stores()
            if result:
                return JsonResponse({'store':result})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
