from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('userHomePage',views.userHomePage,name="userHomePage"),
    path('adminHomePage',views.adminHomePage,name="adminHomePage"),
    path('<int:item_id>/',views.userDetails,name="userDetails"),
    path('<int:item_id>/',views.adminDetails,name="adminDetails"),
    path('add/',views.addItems,name="addItems"),
    path('update/<int:item_id>',views.editItem,name="editItem"),
    path('delete/<int:item_id>',views.deleteItem,name="deleteItem"),
    path('',views.credentials,name="credentials"),
    path('userlogIn/',views.userlogIn,name="userlogIn"),
    path('userSignUp/',views.userSignUp,name="userSignUp"),
    path('adminlogIn/',views.adminlogIn,name="adminlogIn"),
    path('adminSignUp/',views.adminSignUp,name="adminSignUp"),
]