import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.CategoryService import CategoryService
import logging

logger = logging.getLogger(__name__)
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def get_all_category(request):
    if request.method == 'GET':
        try:
            category_service = CategoryService(neo4j_driver)
            list_products = category_service.get_all_category()
            if list_products:
                return JsonResponse({'category':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_product_category(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_category = data.get('id_category')
            try:
                id_category = int(id_category)
            except (ValueError, TypeError):
                return JsonResponse({'message': 'Invalid store ID format'}, status=400)
            category_service = CategoryService(neo4j_driver)
            list_products = category_service.get_product_category(id_category)
            if list_products:
                return JsonResponse({'product':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=500)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
@csrf_exempt
def get_product_search(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_name = data.get('product_name')
            print(f"Product name:{product_name}")
            category_service = CategoryService(neo4j_driver)
            list_products = category_service.get_product_search(product_name)
            if list_products:
                return JsonResponse({'product': list_products }) 
            else:
               return JsonResponse({'product':  []}) 
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

