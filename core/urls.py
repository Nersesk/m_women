from django.urls import path
from core.views import (
    get_last_three_announcements,
    get_staff,
    get_partners,
    get_program_pages_count,
    get_programs,
    get_program,
    get_announcement,
    get_announcement_list,
    get_open_competition,
    get_announcements_page_count,
    get_archive_pages_count,
    get_archive_program,
    get_archive_programs,
    get_product_list,
    get_product_detail,
    get_report_list,
    send_email
)

urlpatterns = [
    path('get_announcements_page_count', get_announcements_page_count, name='announcement_count'),
    path('get_latest_announcements/<str:lang>', get_last_three_announcements, name='latest_announcements'),
    path('get_announcment_list/<str:lang>/<int:page>', get_announcement_list, name='announcement_list'),
    path('get_open_competition_detail/<str:lang>/<int:id>', get_open_competition, name='open_competition_detail'),
    path('get_announcment_detail/<str:lang>/<int:id>', get_announcement, name='job_announcement_detail'),
    path('get_partners/<str:lang>/<int:page>', get_partners, name="partners"),
    path('get_staff/<str:lang>/<int:page>', get_staff, name='main_staff'),
    path('get_program_pages_count/', get_program_pages_count, name="program_pages"),
    path('get_programs/<str:lang>/<int:page>', get_programs, name="programs"),
    path('get_program_detail/<str:lang>/<int:id>', get_program, name='program_detail'),
    path('get_archive_programs/<str:lang>/<int:page>', get_archive_programs, name='archive_programs'),
    path('get_archive_program_detail/<str:lang>/<int:id>', get_archive_program, name='archive_program_detail'),
    path('get_archive_program_pages_count/', get_archive_pages_count, name="program_pages"),
    path('product_list/<str:lang>/<int:page>', get_product_list, name="product_list"),
    path('product_detail/<str:lang>/<int:id>', get_product_detail, name="product_detail"),
    path('get_reports/<str:lang>/<int:page>', get_report_list, name='report_list'),
    path('send_email', send_email, name='send_email')
]
