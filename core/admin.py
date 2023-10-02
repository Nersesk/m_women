from django import forms
from django.utils.translation import gettext_lazy as _
from .models import (Staff,
                     JobAnnouncement,
                     BusinessPartners,
                     Programs,
                     ProgramsPhoto,
                     ProgramFiles,
                     Product,
                     ProductFiles,
                     Report,
                     )
from django.contrib import admin
from image_uploader_widget.admin import ImageUploaderInline



admin.site.site_title =_('M women ')
admin.site.index_title = _('M women')
admin.site.site_header =_('M women')
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng', 'position_eng')
    list_display_links = ('id', 'name_eng', 'position_eng')
    search_fields = ('name_eng', 'name_arm', 'position_eng', 'position_arm')
    view_on_site = False
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "position_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "position_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", ],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]


class JobAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm', 'company_name_eng', 'company_name_arm')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "description_eng", "company_name_eng", 'duration_eng',
                           'assessment_desc_eng', 'appraiser_requirements_eng', 'application_procedure_eng',
                           'about_company_eng', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "description_arm", "company_name_arm", 'duration_arm',
                           'assessment_desc_arm', 'appraiser_requirements_arm', 'application_procedure_arm',
                           'about_company_arm', ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ['contacts', 'image', 'created', 'updated', 'active'],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]
    readonly_fields = ('created', 'updated')


class BusinessPartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'duration', 'projects_count'],
                "classes": ["wide", "extrapretty"],
            }

        ),
    ]


class PhotoInline(ImageUploaderInline):
    model = ProgramsPhoto
    add_image_text = "add_image_text"


class FileInline(admin.TabularInline):
    model = ProgramFiles
    max_num = 10


class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_eng',)
    list_display_links = ('id', 'name_eng',)
    search_fields = ('name_eng', 'name_arm',)
    view_on_site = False
    inlines = [PhotoInline, FileInline]
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", "title_eng", "article_eng"],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", "title_arm", "article_arm"],
                "classes": ["wide", "extrapretty"],
            },
        ),

    ]


class ProductFilesInline(admin.StackedInline):
    model = ProductFiles


class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductFilesInline]


class ReportAdmin(admin.ModelAdmin):
    search_fields = ('name_eng', 'name_arm')
    fieldsets = [

        (
            _('Fields in English'),
            {
                "fields": ["name_eng", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _("Fields in Armenian"),
            {
                "fields": ["name_arm", ],
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            _('General Fields'),
            {
                "fields": ["image", 'report_file', ],
                "classes": ["wide", "extrapretty"],
            }

        ),

    ]


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Programs, ProgramModelAdmin)
admin.site.register(JobAnnouncement, JobAnnouncementAdmin)
admin.site.register(BusinessPartners, BusinessPartnersAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Report, ReportAdmin)
