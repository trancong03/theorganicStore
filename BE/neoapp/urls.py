from django.urls import path
from neoapp.views import Person,Account
urlpatterns = [
    path('login/', Account.login_view, name='login'),
    path('person/<int:person_id>/', Person.update_person, name='update_person'),
    path('person-update-avatar/<int:person_id>/', Person.update_image_person, name='update_person_image'),
]
