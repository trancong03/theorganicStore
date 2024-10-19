from django.urls import path
from neoapp.views import Person,Account,Product
urlpatterns = [
    path('login/', Account.login_view, name='login'),
    path('signup/', Account.SignUp_view, name='signup'),
    path('reset-password/', Account.reset_password, name='reset_password'),
    path('person/<int:person_id>/', Person.update_person, name='update_person'),
    path('person-update-avatar/<int:person_id>/', Person.update_image_person, name='update_person_image'),
    path('product/', Product.get_all_product, name='get_all_product'),
    path('get_product_on_cart/', Product.get_product_on_cart, name='get_product_on_cart'),
    path('add_product_to_Cart/', Product.add_product_to_Cart, name='add_product_to_Cart'),
]
