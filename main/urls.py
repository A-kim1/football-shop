from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product
from main.views import add_product_entry_ajax, edit_product_ajax, delete_product_ajax, ajax_register, ajax_login, ajax_logout

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),

    # ini harusnya yg <str:id> itu artinya adlh id yg di dpt dari models.py di fungsi show_p
    # roduct nya (yg pk itu)
    path('product/<str:id>/', show_product, name='show_product'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),

    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('ajax-login/', ajax_login, name='ajax_login'),
    path('ajax-register/', ajax_register, name='ajax_register'),
    path('ajax-logout/', ajax_logout, name='ajax_logout'),
]