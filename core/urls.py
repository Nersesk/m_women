from django.urls import path
from core.views import (
    get_last_three_announcements,
    get_staff,
    get_partners,
    get_program_pages_count,
    get_programs,
    get_program,
    get_announcement
)

urlpatterns = [
    path('get_latest_announcements/<str:lang>', get_last_three_announcements, name='latest_announcements'),
    path('get_announcment/<str:lang>/<int:id>',get_announcement, name='job_announcement_detail'),
    path('get_partners/<str:lang>/<int:page>', get_partners, name="partners"),
    path('get_staff/<str:lang>/<int:page>', get_staff, name='main_staff'),
    path('get_programs_count/', get_program_pages_count, name="program_pages"),
    path('get_programs/<str:lang>/<int:page>', get_programs, name="programs"),
    path('get_program/<str:lang>/<int:id>',get_program, name='program_detail')
]

