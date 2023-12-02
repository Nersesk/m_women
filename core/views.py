import os
import json
from math import ceil
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import Program, JobAnnouncement, OpenCompetition, ArchiveProgram
from core.utils import (
    get_announcements_qs,
    get_dict_for_announcement_list,
    get_staff_members_queryset,
    get_dict_for_staff_members,
    get_dict_for_partners,
    get_partners_qs,
    get_program_qs,
    get_program_list_dict,
    get_program_detail_dict,
    get_job_announcement_detail_dict,
    get_job_announcement_qs,
    get_open_competition_qs,
    get_open_competition_detail_dict,
    get_archive_programs_qs,
    get_product_qs,
    get_product_dict,
    get_product_detail_dict,
    get_report_qs,
    get_report_dict,
    send_email, filter_announcement_qs, filter_programs_qs, get_banner_images
)


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = get_banner_images()
        return context


class About(TemplateView):
    template_name = 'core/about.html'


class Contact(TemplateView):
    template_name = 'core/contact.html'


class Announcements(TemplateView):
    template_name = 'core/announcement.html'


def programs_view(request):
    return render(request, 'core/programm.html')


class Archive(TemplateView):
    template_name = 'core/archives.html'


class Count(TemplateView):
    template_name = 'core/count.html'


class Research(TemplateView):
    template_name = 'core/research.html'


class ProgramDetail(TemplateView):
    template_name = 'core/programm1.html'

    def get(self, request, *args, **kwargs):
        program_id = self.kwargs.get('program_id')
        program = get_object_or_404(Program, id=program_id)
        context = self.get_context_data(program=program)
        context['program'] = get_program_detail_dict(program, self.kwargs.get('lang'))
        return self.render_to_response(context)


def program_detail(request, program_id, lang):
    program = get_object_or_404(Program, id=program_id)
    program_dict = get_program_detail_dict(program, lang)
    return render(request, 'core/programm1.html', context={'program': program_dict})


class ArchiveProgramDetail(TemplateView):
    template_name = 'core/anounce2.html'

    def get(self, request, *args, **kwargs):
        program_id = self.kwargs.get('program_id')
        program = get_object_or_404(ArchiveProgram, id=program_id)
        context = self.get_context_data(program=program)

        return self.render_to_response(context)


class JobAnnouncementDetail(TemplateView):
    template_name = 'core/anounce1.html'

    def get(self, request, *args, **kwargs):
        program_id = self.kwargs.get('job_id')
        program = get_object_or_404(JobAnnouncement, id=program_id)
        context = self.get_context_data(program=program)

        return self.render_to_response(context)


class OpenCompetitionDetail(TemplateView):
    template_name = 'core/anounce1.html'

    def get(self, request, *args, **kwargs):
        program_id = self.kwargs.get('comp_id')
        program = get_object_or_404(OpenCompetition, id=program_id)
        context = self.get_context_data(program=program)

        return self.render_to_response(context)


def get_announcement_list(request: WSGIRequest, lang: str, page: int) -> JsonResponse:
    lst = []
    announcements = get_announcements_qs()
    page_announcements = announcements[(page - 1) * 12: page * 12]
    for announcement in page_announcements:
        program_dict = get_dict_for_announcement_list(announcement, lang)
        lst.append(program_dict)
    dct = {'announcements': lst}
    return JsonResponse(dct)


def get_announcements_page_count(request: WSGIRequest) -> JsonResponse:
    announcements = get_announcements_qs()
    pages_count = ceil(len(announcements) / 12)
    return JsonResponse(
        {'pages_count': pages_count}
    )


def get_last_three_announcements(request: WSGIRequest, lang: str) -> HttpResponse:
    lst = []
    announcements = get_announcements_qs()
    queryset = announcements[:3]
    for i in queryset:
        announcement_dict = get_dict_for_announcement_list(i, lang)
        lst.append(announcement_dict)
    dct = {'announcements': lst}
    return JsonResponse(dct)


def get_announcement(request: WSGIRequest, lang: str, id: int) -> HttpResponse:
    try:
        announcement = get_job_announcement_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Job Announcement does not exists"}), content_type='application/json')

    job_announcement_dict = get_job_announcement_detail_dict(announcement, lang)
    return JsonResponse(job_announcement_dict)


def get_open_competition(request: WSGIRequest, lang: str, id: int) -> HttpResponse:
    try:
        open_competition = get_open_competition_qs().get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'msg': "Open competition does not exists"})

    open_competition_dict = get_open_competition_detail_dict(open_competition, lang)
    return JsonResponse(open_competition_dict)


def get_staff(request: WSGIRequest, lang: str, page=1) -> HttpResponse:
    staff_members = []
    page_elems = 9
    queryset = get_staff_members_queryset()
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for i in actual_qs:
        staff_dict = get_dict_for_staff_members(i, lang)
        staff_members.append(staff_dict)
    dct = {'staff_members': staff_members, 'next_page': has_other_page}
    return JsonResponse(dct)


def get_partners(request: WSGIRequest, lang: str, page=1) -> HttpResponse:
    business_partners = []
    page_elems = 9
    queryset = get_partners_qs()
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for i in actual_qs:
        staff_dict = get_dict_for_partners(i, lang)
        business_partners.append(staff_dict)
    dct = {'business_partners': business_partners, 'next_page': has_other_page}
    return JsonResponse(dct)


def get_program_pages_count(request: WSGIRequest) -> HttpResponse:
    programs = get_program_qs()
    pages_count = ceil(programs.count() / 12)
    return JsonResponse({'pages_count': pages_count})


def get_programs(request: WSGIRequest, lang: str, page=1) -> HttpResponse:
    lst = []
    programs = get_program_qs()
    page_programs = programs[(page - 1) * 12: page * 12]
    for program in page_programs:
        program_dict = get_program_list_dict(program, lang, 'program_detail')
        lst.append(program_dict)

    return JsonResponse({'programs': lst})


def get_program(request: WSGIRequest, lang: str, id: int) -> HttpResponse:
    try:
        program = get_program_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    program_dict = get_program_detail_dict(program, lang)
    return JsonResponse(program_dict)


def get_archive_program(request: WSGIRequest, lang: str, id) -> HttpResponse:
    try:
        program = get_archive_programs_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    program_dict = get_program_detail_dict(program, lang)
    return JsonResponse(program_dict)


def get_archive_programs(request: WSGIRequest, lang: str, page=1) -> HttpResponse:
    lst = []
    programs = get_archive_programs_qs()
    page_programs = programs[(page - 1) * 12: page * 12]
    for program in page_programs:
        program_dict = get_program_list_dict(program, lang, 'archive_program_detail')
        lst.append(program_dict)

    return JsonResponse({'archive_programs': lst})


def get_archive_pages_count(request: WSGIRequest) -> HttpResponse:
    programs = get_archive_programs_qs()
    pages_count = int(1 + (programs.count() / 12))
    return JsonResponse({'pages_count': pages_count})


def get_product_list(request: WSGIRequest, lang: str, page: int) -> HttpResponse:
    lst = []
    queryset = get_product_qs()
    page_elems = 9
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for product in actual_qs:
        product_dict = get_product_dict(product, lang)
        lst.append(product_dict)

    return JsonResponse({'product_list': lst,
                         'next_page': has_other_page})


def get_product_detail(request: WSGIRequest, lang: str, id: int) -> HttpResponse:
    try:
        product = get_product_qs().get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'msg': "Program does not exists"})

    product_dict = get_product_detail_dict(product, lang)
    return JsonResponse(product_dict)


def get_report_list(request: WSGIRequest, lang: str, page: int) -> HttpResponse:
    lst = []
    queryset = get_report_qs()
    page_elems = 9
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for report in actual_qs:
        product_dict = get_report_dict(report, lang)
        lst.append(product_dict)

    return JsonResponse({'product_list': lst, 'next_page': has_other_page})


@csrf_exempt
def send_message(request: WSGIRequest) -> HttpResponse:
    if request.method == "GET":
        return HttpResponseNotAllowed('GET')
    from_email = request.POST.get('from_email')
    phone_number = request.POST.get('phone_number')
    message_text = request.POST.get('message_text')
    if (
            not from_email or
            not phone_number or
            not message_text):
        return HttpResponseBadRequest()
    status = send_email(from_email, phone_number, message_text)
    return JsonResponse({'status': status})


@csrf_exempt
def search_announcements(request: WSGIRequest, lang: str) -> HttpResponse:
    if request.method == "GET":
        return HttpResponseNotAllowed('GET')
    lst = []
    pattern = request.POST.get('search_pattern')
    if not pattern:
        announcements = get_announcements_qs()
    else:
        announcements = filter_announcement_qs(lang, pattern)
    for announcement in announcements:
        program_dict = get_dict_for_announcement_list(announcement, lang)
        lst.append(program_dict)
    dct = {'announcements': lst}
    return JsonResponse(dct)


@csrf_exempt
def search_programs(request: WSGIRequest, lang: str) -> HttpResponse:
    if request.method == "GET":
        return HttpResponseNotAllowed('GET')
    lst = []
    pattern = request.POST.get('search_pattern')
    if not pattern:
        programs = get_program_qs()
    else:
        programs = filter_programs_qs(lang, pattern)

    for program in programs:
        lst.append(get_program_list_dict(program, lang, 'program_detail'))
    dct = {'programs': lst}
    return JsonResponse(dct)
