import os
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

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
    get_product_dict, get_product_detail_dict, get_report_qs, get_report_dict
)


def get_announcement_list(request: HttpRequest, lang: str, page: int) -> HttpResponse:
    lst = []
    announcements = get_announcements_qs()
    page_announcements = announcements[(page - 1) * 12: page * 12]
    for announcement in page_announcements:
        program_dict = get_dict_for_announcement_list(announcement, lang)
        lst.append(program_dict)

    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_announcements_page_count(request: HttpRequest) -> HttpResponse:
    announcements = get_announcements_qs()
    pages_count = int(1 + (len(announcements) / 12))
    return HttpResponse(
        json.dumps({'pages_count': pages_count}),
        content_type='application/json',
    )


def get_last_three_announcements(request: HttpRequest, lang: str) -> HttpResponse:
    lst = []
    announcements = get_announcements_qs()
    queryset = announcements[:3]
    for i in queryset:
        announcement_dict = get_dict_for_announcement_list(i, lang)
        lst.append(announcement_dict)
    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_announcement(request: HttpRequest, lang: str, id: int) -> HttpResponse:
    try:
        announcement = get_job_announcement_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Job Announcement does not exists"}), content_type='application/json')

    job_announcement_dict = get_job_announcement_detail_dict(announcement, lang)
    return HttpResponse(json.dumps(job_announcement_dict), content_type='application/json')


def get_open_competition(request: HttpRequest, lang: str, id: int) -> HttpResponse:
    try:
        open_competition = get_open_competition_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Open competition does not exists"}), content_type='application/json')

    open_competition_dict = get_open_competition_detail_dict(open_competition, lang)
    return HttpResponse(json.dumps(open_competition_dict), content_type='application/json')


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
    pages_count = int(1 + (programs.count() / 12))
    return HttpResponse(
        json.dumps({'pages_count': pages_count}),
        content_type='application/json',
    )


def get_programs(request: HttpRequest, lang: str, page=1) -> HttpResponse:
    lst = []
    programs = get_program_qs()
    page_programs = programs[(page - 1) * 12: page * 12]
    for program in page_programs:
        program_dict = get_program_list_dict(program, lang, 'program_detail')
        lst.append(program_dict)

    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_program(request: HttpRequest, lang: str, id: int) -> HttpResponse:
    try:
        program = get_program_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    program_dict = get_program_detail_dict(program, lang)
    return HttpResponse(json.dumps(program_dict), content_type='application/json')


def get_archive_program(request: HttpRequest, lang: str, id) -> HttpResponse:
    try:
        program = get_archive_programs_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    program_dict = get_program_detail_dict(program, lang)
    return HttpResponse(json.dumps(program_dict), content_type='application/json')


def get_archive_programs(request: HttpRequest, lang: str, page=1) -> HttpResponse:
    lst = []
    programs = get_archive_programs_qs()
    page_programs = programs[(page - 1) * 12: page * 12]
    for program in page_programs:
        program_dict = get_program_list_dict(program, lang, 'archive_program_detail')
        lst.append(program_dict)

    return HttpResponse(json.dumps(lst), content_type='application/json')


def get_archive_pages_count(request: HttpRequest) -> HttpResponse:
    programs = get_archive_programs_qs()
    pages_count = int(1 + (programs.count() / 12))
    return HttpResponse(
        json.dumps({'pages_count': pages_count}),
        content_type='application/json',
    )


def get_product_list(request: HttpRequest, lang: str, page: int) -> HttpResponse:
    lst = []
    queryset = get_product_qs()
    page_elems = 9
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for product in actual_qs:
        product_dict = get_product_dict(product, lang)
        lst.append(product_dict)

    return HttpResponse(json.dumps({'product_list': lst,
                                    'next_page': has_other_page}),
                        content_type='application/json'
                        )


def get_product_detail(request: HttpRequest, lang: str, id: int) -> HttpResponse:
    try:
        product = get_product_qs().get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({'msg': "Program does not exists"}), content_type='application/json')

    product_dict = get_product_detail_dict(product, lang)
    return HttpResponse(json.dumps(product_dict), content_type='application/json')


def get_report_list(request: HttpRequest, lang: str, page: int) -> HttpResponse:
    lst = []
    queryset = get_report_qs()
    page_elems = 9
    actual_qs = queryset[(page - 1) * page_elems: page * page_elems]
    has_other_page = page + 1 if queryset.count() > page * 9 else None
    for report in actual_qs:
        product_dict = get_report_dict(report, lang)
        lst.append(product_dict)

    return HttpResponse(json.dumps({'product_list': lst,
                                    'next_page': has_other_page}),
                        content_type='application/json'
                        )