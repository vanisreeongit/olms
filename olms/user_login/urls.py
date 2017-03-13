from django.conf.urls import url
from . import views,registration,leave_application

urlpatterns = [
	url(r'^$',views.home,name='home'),
    url(r'^login/',views.user_login.as_view(),name='login'),
    url(r'^register/',registration.register,name='register'),
    url(r'^hello/',views.userpage,name='userpage'),
	url(r'^logout/',views.user_logout,name='userlogout'),
	url(r'^apply_leave/',leave_application.leave_apply.as_view(),name='leave_apply')  
]
