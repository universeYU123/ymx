from django.urls import path
from app import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logOut/', views.logOut, name='logOut'),
    path('home/', views.home, name='home'),
    path('changeSelfInfo/', views.changeSelfInfo, name='changeSelfInfo'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('tableData/', views.tableData, name='tableData'),
    path('tableData2/', views.tableData2, name='tableData2'),
    path('addComments/<int:id>', views.addComments, name='addComments'),
    path('addComments2/<int:id>', views.addComments2, name='addComments2'),
    path('cityChar/', views.cityChar, name='cityChar'),
    path('rateChar/', views.rateChar, name='rateChar'),
    path('priceChar/', views.priceChar, name='priceChar'),
    path('commentsChar/', views.commentsChar, name='commentsChar'),
    path('heartChar/', views.heartChar, name='heartChar'),
    path('bloodChar/', views.bloodChar, name='bloodChar'),
    path('comment/', views.comment, name='comment'),
]