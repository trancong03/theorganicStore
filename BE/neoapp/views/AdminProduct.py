import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AdminProductService import AdminProductService
import logging

logger = logging.getLogger(__name__)

# Khởi tạo driver một lần và sử dụng chung
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def add_product(request):
    if request.method == 'GET':
        try:
            product_service = AdminProductService(neo4j_driver)
            list_products = product_service.add_product()
            if list_products:
                return JsonResponse({'product':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_product_store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_store = data.get('id_store')

            # Kiểm tra xem id_store có tồn tại hay không
            if id_store is None:
                return JsonResponse({'message': 'Store ID is required'}, status=400)

            # Ép giá trị id_store về số nguyên
            try:
                id_store = int(id_store)
            except (ValueError, TypeError):
                return JsonResponse({'message': 'Invalid store ID format'}, status=400)

            product_service = AdminProductService(neo4j_driver)
            list_products = product_service.get_product_store(id_store)

            if list_products['success']:
                products_with_stock = [
                    {"product": product, "stock": stock}
                    for product, stock in zip(list_products['data']['products'], list_products['data']['stocks'])
                ]
                return JsonResponse({'products_with_stock': products_with_stock})
            else:
                return JsonResponse({'message': 'No products found for this store'}, status=404)
        except Exception as e:
            print(f"Error: {e}")  # Ghi lại lỗi để phục vụ cho việc gỡ lỗi
            return JsonResponse({'message': 'Internal Server Error'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)