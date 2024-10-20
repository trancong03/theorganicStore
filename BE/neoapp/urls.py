from django.urls import path
from neoapp.views import Person,Account,Product,AdminProduct
urlpatterns = [
    path('login/', Account.login_view, name='login'),
    path('signup/', Account.SignUp_view, name='signup'),
    path('reset-password/', Account.reset_password, name='reset_password'),
    path('person/<int:person_id>/', Person.update_person, name='update_person'),
    path('person-update-avatar/<int:person_id>/', Person.update_image_person, name='update_person_image'),
    path('product/', Product.get_all_product, name='get_all_product'),
    path('get_product_on_cart/', Product.get_product_on_cart, name='get_product_on_cart'),
    path('add_product_to_Cart/', Product.add_product_to_Cart, name='add_product_to_Cart'),
    path('remove_product_from_Cart/', Product.remove_product_from_Cart, name='remove_product_from_Cart'),

    path('get_product_on_like/', Product.get_product_on_like, name='get_product_on_like'),
    path('add_product_to_like/', Product.add_product_to_like, name='add_product_to_like'),
    path('remove_product_from_like/', Product.remove_product_from_like, name='remove_product_from_Cart'),

    path('get_delivery_address/', Product.get_delivery_address, name='get_delivery_address'),
    path('create_delivery_address/', Product.create_delivery_address, name='create_delivery_address'),
    path('update-delivery-address/', Product.update_delivery_address, name='update_delivery_address'),
    path('delete-delivery-address/', Product.delete_delivery_address, name='delete_delivery_address'),

    #admin
     path('get_product_store/', AdminProduct.get_product_store, name='get_product_store'),
     
]
