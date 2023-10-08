from django.urls import path
from core.views import (
    get_last_three_announcements,
    get_staff
)

urlpatterns = [
    path('get_latest_announcements/<str:lang>', get_last_three_announcements, name='latest_announcements'),
    path('get_staff/<str:lang>/<int:page>', get_staff, name='main_staff'),

]