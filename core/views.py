import os
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from core.utils import (
    get_job_announcement_queryset,
    get_dict_for_job_announcement_list,
    get_staff_members_queryset,
    get_dict_for_staff_members,
    get_dict_for_partners,
    get_partners_qs,
    get_program_qs,
    get_program_list_dict,
    get_program_detail_dict,
    get_job_announcement_detail_dict
)


def get_last_three_announcements(request: HttpRequest, lang: str) -> HttpResponse:
    lst = []
    job_announcements = get_job_announcement_queryset()
    queryset = job_announcements[:3]
    for i in queryset:
        announcement_dict = get_dict_for_job_announcement_list(i, lang)
        lst.append(announcement_dict)
    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_announcement(request: HttpRequest, lang: str, id: int) -> HttpResponse:
    try:
        announcement = get_job_announcement_queryset().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Job Announcement does not exists"}), content_type='application/json')

    program_dict = get_job_announcement_detail_dict(announcement, lang)
    return HttpResponse(json.dumps(program_dict), content_type='application/json')


def get_staff(request: HttpRequest, lang: str, page=1) -> HttpResponse:
    staff_members = []
    page_elems = 9
    queryset = get_staff_members_queryset()
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for i in actual_qs:
        staff_dict = get_dict_for_staff_members(i, lang)
        staff_members.append(staff_dict)
    dct = {'staff_members': staff_members, 'next_page': has_other_page}
    return HttpResponse(json.dumps(dct), content_type='application/json')


def get_partners(request: HttpRequest, lang: str, page=1) -> HttpResponse:
    business_partners = []
    page_elems = 9
    queryset = get_partners_qs()
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for i in actual_qs:
        staff_dict = get_dict_for_partners(i, lang)
        business_partners.append(staff_dict)
    dct = {'business_partners': business_partners, 'next_page': has_other_page}
    return HttpResponse(json.dumps(dct), content_type='application/json')


def get_program_pages_count(request: HttpRequest) -> HttpResponse:
    programs = get_program_qs()
    programs_count = programs.count()
    return HttpResponse(
        json.dumps({'programs_count': programs_count}),
        content_type='application/json',
    )


def get_programs(request: HttpRequest, lang: str, page=1) -> HttpResponse:
    lst = []
    programs = get_program_qs()
    page_programs = programs[(page - 1) * 12: page * 12]
    for program in page_programs:
        program_dict = get_program_list_dict(program, lang)
        lst.append(program_dict)

    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_program(request: HttpRequest, lang: str, id) -> HttpResponse:
    try:
        program = get_program_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    program_dict = get_program_detail_dict(program, lang)
    return HttpResponse(json.dumps(program_dict), content_type='application/json')
