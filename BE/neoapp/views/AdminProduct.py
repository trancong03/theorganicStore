import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from neoapp.db import Neo4jDriver
from neoapp.services.AdminProductService import AdminProductService
import logging

logger = logging.getLogger(__name__)

# Initialize a single Neo4j driver instance for reuse
neo4j_driver = Neo4jDriver("bolt://localhost:7687", "neo4j", "cong3003", "neo4j")

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract variables from the request body
            id_product = data.get('product_id')
            id_person = data.get('person_id')
            image_ids = data.get('image_ids')
            name = data.get('name')
            price = data.get('price')
            unit = data.get('unit')
            origin = data.get('origin')
            expiration_date = data.get('expiration_date')
            
            # Call service with extracted variables
            product_service = AdminProductService(neo4j_driver)
            result = product_service.add_product(
                id_product, 
                id_person, 
                image_ids, 
                name, 
                price, 
                unit, 
                origin, 
                expiration_date
            )
            
            if result['success']:
                return JsonResponse({'product': result['product']})
            else:
                return JsonResponse({'message': result.get('message', 'Operation failed')}, status=400)
        except Exception as e:
            logger.error("Error adding product: %s", str(e))
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_product_store(request):
    if request.method == 'GET':
        try:
            id_store = request.GET.get('store_id')
            if not id_store:
                return JsonResponse({'message': 'Store ID is required.'}, status=400)
            
            # Fetch products for the given store
            product_service = AdminProductService(neo4j_driver)
            result = product_service.get_product_store(id_store)
            
            if result['success']:
                return JsonResponse({'products': result['data']['products'], 'stocks': result['data']['stocks']})
            else:
                return JsonResponse({'message': 'No products found for the given store.'}, status=404)
        except Exception as e:
            logger.error("Error fetching products for store: %s", str(e))
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
