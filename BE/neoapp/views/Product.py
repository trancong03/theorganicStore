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

@csrf_exempt
def remove_product_from_Cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idProduct = data.get('product_id')
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            result = product_service.remove_product_from_Cart(idProduct, idPerson)
            if result:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_product_on_like(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            list_products = product_service.get_product_on_like(idPerson)
            if list_products:
                return JsonResponse({'product':list_products})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def add_product_to_like(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idProduct = data.get('product_id')
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            result = product_service.add_product_to_like(idProduct, idPerson)
            if result:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
@csrf_exempt
def remove_product_from_like(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idProduct = data.get('product_id')
            idPerson = data.get('person_id')
            product_service = ProductService(neo4j_driver)
            result = product_service.remove_product_from_like(idProduct, idPerson)
            if result:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
#Địa chỉ nhận hàng
@csrf_exempt
def create_delivery_address(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            person_id = data.get('person_id')
            recipient_name = data.get('recipient_name')
            phone_number = data.get('phone_number')
            delivery_address = data.get('delivery_address')

            product_service = ProductService(neo4j_driver)
            result = product_service.create_delivery_address(person_id,recipient_name,phone_number,delivery_address)
            if result:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error'}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def get_delivery_address(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            idPerson = data.get('person_id')
            if not idPerson:
                return JsonResponse({'message': 'Person ID is required'}, status=400)
            product_service = ProductService(neo4j_driver)
            delivery_address_list = product_service.get_delivery_address(idPerson)
            if delivery_address_list:
                return JsonResponse({'delivery_address': delivery_address_list})
            else:
                return JsonResponse({'message': 'No address found for the given person'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
@csrf_exempt
def update_delivery_address(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            person_id = data.get('person_id')
            old_delivery_address = data.get('old_delivery_address')
            new_delivery_address = data.get('new_delivery_address')
            new_recipient_name = data.get('recipient_name')
            new_phone_number = data.get('phone_number')

            product_service = ProductService(neo4j_driver)
            result = product_service.update_delivery_address(
                person_id,
                old_delivery_address,
                new_delivery_address,
                new_recipient_name,
                new_phone_number
            )
            if result['success']:
                return JsonResponse(result)
            else:
                return JsonResponse({'message': result['message']}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
@csrf_exempt
def delete_delivery_address(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            person_id = data.get('person_id')
            delivery_address = data.get('delivery_address')

            product_service = ProductService(neo4j_driver)
            result = product_service.delete_delivery_address(person_id, delivery_address)
            if result['success']:
                return JsonResponse({'message': 'Address deleted successfully'})
            else:
                return JsonResponse({'message': result['message']}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'Internal Server Error', 'error': str(e)}, status=500)
    return JsonResponse({'message': 'Method not allowed'}, status=405)
