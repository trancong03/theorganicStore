import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.ProductService import ProductService
import logging

logger = logging.getLogger(__name__)

# Khởi tạo driver một lần và sử dụng chung
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def get_all_product(request):
    if request.method == 'GET':
        try:
            product_service = ProductService(neo4j_driver)
            list_products = product_service.get_all_product()
            if list_products:
                return JsonResponse({'product':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_product_on_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            list_products = product_service.get_product_on_cart(idPerson)
            if list_products:
                return JsonResponse({'product':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def add_product_to_Cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idProduct = data.get('product_id')
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            result = product_service.add_product_to_Cart(idProduct, idPerson)
            if result:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)