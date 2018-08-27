#!/usr/bin/env
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('there is index')


def page_not_found(request):
    return render(request,'404.html')


def page_error(request):
    return HttpResponse('500.html')


def permission_denied(request):
    return HttpResponse('403.html')


def bad_request(request):
    return HttpResponse('400.html')