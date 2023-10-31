from django.urls import path
from core import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('contacts', views.Contact.as_view(), name='contacts'),
    path('announcments', views.Announcement.as_view(), name='announcement'),
    path('programs', views.Programs.as_view(), name='programs-view'),
    path('archive',views.Archive.as_view(), name='archive'),
    path('count',views.Count.as_view(), name='count'),
    path('research', views.Research.as_view(), name='research'),
    path('get_announcements_page_count', views.get_announcements_page_count, name='announcement_count'),
    path('get_latest_announcements/<str:lang>', views.get_last_three_announcements, name='latest_announcements'),
    path('get_announcment_list/<str:lang>/<int:page>', views.get_announcement_list, name='announcement_list'),
    path('get_open_competition_detail/<str:lang>/<int:id>', views.get_open_competition, name='open_competition_detail'),
    path('get_announcment_detail/<str:lang>/<int:id>', views.get_announcement, name='job_announcement_detail'),
    path('get_partners/<str:lang>/<int:page>', views.get_partners, name="partners"),
    path('get_staff/<str:lang>/<int:page>', views.get_staff, name='main_staff'),
    path('get_program_pages_count/', views.get_program_pages_count, name="program_pages"),
    path('get_programs/<str:lang>/<int:page>', views.get_programs, name="programs"),
    path('get_program_detail/<str:lang>/<int:id>', views.get_program, name='program_detail'),
    path('get_archive_programs/<str:lang>/<int:page>', views.get_archive_programs, name='archive_programs'),
    path('get_archive_program_detail/<str:lang>/<int:id>', views.get_archive_program, name='archive_program_detail'),
    path('get_archive_program_pages_count/', views.get_archive_pages_count, name="program_pages"),
    path('product_list/<str:lang>/<int:page>', views.get_product_list, name="product_list"),
    path('product_detail/<str:lang>/<int:id>', views.get_product_detail, name="product_detail"),
    path('get_reports/<str:lang>/<int:page>', views.get_report_list, name='report_list'),
    path('send_email', views.send_message, name='send_email'),
    path('search_announcments/<str:lang>', views.search_announcements, name='search_announcements'),
    path('search_programs/<str:lang>', views.search_programs, name='search_program')
]
