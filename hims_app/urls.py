from django.urls import path
from hims_app import views

urlpatterns = [
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('room/',views.roomview,name="rooms"),
    path('customer/',views.customersview,name='customers'),
    path('booking/',views.bookingsview,name='bookings'),
    path('room/add/',views.addroomview,name='add-room'),
    path('room/update/<int:room_id>',views.updateroomview,name='update-room'),
    path('room/delete/<int:room_id>',views.deleteroomview,name='delete-room'),
    path('customer/add/',views.addcustomerview,name='add-customer'),
    path('customer/update/<int:customer_id>',views.updatecustomerview,name='update-customer'),
    path('customer/delete/<int:customer_id>',views.deletecustomerview,name='delete-customer'),
    
    # admin authentication
    path('admin/login',views.admin_login,name='admin-login'),
    path('admin/logout',views.admin_logout,name='admin-logout'),

    path('',views.homepageview,name='home'),
    path('view/',views.displayrooms,name='view-room'),

]