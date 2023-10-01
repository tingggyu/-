from collections import defaultdict

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from website.models import Resource, Notice, Introduction, NameLexemes, Illustrate
from django.http import HttpResponseRedirect
from .to_solr import SolrProcessor
from website.utils import Lexeme
from django import template
import json			
import xlwt
import xlrd
import pymysql
import os

@csrf_protect
def index(request):
    response = render(request, 'index.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def appendix(request):
    response = render(request, 'appendix.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def appendix2(request):
    response = render(request, 'appendix2.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def directions(request, cat='系統說明', sub='系統說明'):
    Illust = Illustrate.objects.filter(category=cat, subclass=sub)
    response = render(request, 'directions.html', {'ill': Illust})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def introduction(request):
    intro = Introduction.objects.all()
    response = render(request, 'introduction.html', {'intro': intro})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def name_search(request):
    if request.method == "POST":
        form_data = request.POST["name"]

        result = []

        if form_data and len(form_data) > 1:
            name_collection = {}

            # 根據每個單字去資料庫找到對應的資料
            # 並整理成一個 dict
            for d in form_data:
                name_list = NameLexemes.objects.filter(lexeme=d)
                tmp = defaultdict(list)

                for i in name_list:
                    tmp[i.accent].append(
                        {
                            "audio_name": i.audio_name,
                            "attribute": i.attribute,
                            "tone_pitch": i.tone_pitch,
                        }
                    )

                name_collection[d] = tmp

            lexeme = Lexeme([i for i in form_data], name_collection)
            result = lexeme.process_concat_data(lexeme.concat_lexeme())

        # 如果只有查詢一個字
        elif form_data and len(form_data) == 1:
            name_data = NameLexemes.objects.filter(lexeme=form_data)

            for d in name_data:
                tmp = {
                    "attribute": d.attribute,
                    "tone_pitch": d.tone_pitch,
                    "audio_name": d.audio_name,
                    "accent": d.accent,
                }

                result.append(tmp)

        return render(
            request,
            'name_search.html',
            {
                "data": result,
            },
        )

    response = render(request, 'name_search.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def news(request):
    new = Notice.objects.all()
    response = render(request, 'news.html', {'new': new})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def news_detail(request, i_id):
    new = Notice.objects.filter(id=i_id)
    response = render(request, 'news_detail.html', {'new': new})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def resource(request, sub='第二階層1'):
    reso = Resource.objects.filter(category="客語知識庫", subclass=sub)
    response = render(request, 'resource.html', {'reso': reso})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def resource_learning(request):
    res = Resource.objects.filter(category="客語學習資源")
    response = render(request, 'resource_learning.html', {'res': res})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def resource_download(request):
    res1 = Resource.objects.filter(category="客語資源下載", subclass="本辭典的文字")
    res2 = Resource.objects.filter(category="客語資源下載", subclass="詞條音檔")
    res3 = Resource.objects.filter(category="客語資源下載", subclass="例句音檔")
    res4 = Resource.objects.filter(category="客語資源下載", subclass="其他資源")
    response = render(
        request, 'resource_download.html', {'res1': res1, 'res2': res2, 'res3': res3, 'res4': res4}
    )
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def search_list(request):
    response = render(request, 'search_list.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def search_notlist(request):
    response = render(request, 'search_notlist.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def search_result(request):
    response = render(request, 'search_result.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def site_search(request):
    response = render(request, 'site_search.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def sitemap(request):
    response = render(request, 'sitemap.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_protect
def thesaurus(request):
    response = render(request, 'thesaurus.html', {})
    response['Strict-Transport-Security'] = 'max-age=2592000'
    response['X-Frame-Options'] = 'SAMEORIGIN'
    response['Referrer-Policy'] = 'no-referrer'
    response['X-XSS-Protection'] = '1; mode=block'
    response['X-Content-Type-Options'] = 'nosniff'
    response['Strict-Transport-Security'] = 'max-age=16070400; includeSubDomains'
    return response


@csrf_exempt
def backend_login(request):
    result = {'status': '', 'msg': '', 'data': {}}
    try:
        account = request.POST['account']
        pwd = request.POST['pwd']

        if check_illegal_parameter(account) or check_illegal_parameter(pwd):
            result['status'] = 'No'
            result['msg'] = 'illegal_parameter'
        else:
            result['status'] = 'Yes'
            request.session['backend_login'] = account
            print(request.session['backend_login'])
    except Exception as e:
        result['status'] = 'Error'
        result['msg'] = str(e)
    return JsonResponse(result, safe=False)


def check_illegal_parameter(parameter):
    sign_list = ["=", "%", "+", "$", "*", "/", "#", "!", "?", "^", "&", "<", ">", "'", '"']
    for sign in sign_list:
        if sign in parameter:
            return True
    return False

@csrf_exempt
def solr_search(request):
	result={}
	try:
		solr = SolrProcessor("http://localhost:8983/solr/mycore")
		keyword = request.POST['keyword']
		result = solr.search_solr(keyword)
		ret = []
		for each in  result['response']['docs'] :
			temp = {}
			temp['id'] = each['id']
			temp['file_name'] = each['File_Name_txt_ja']
			temp['file_path'] = each['File_Path_txt_ja']
			temp['file_content'] = result['highlighting'][each['id']]['File_Content_txt_ja'][0]
			ret.append(temp)	
		return JsonResponse(ret, safe=False)	
	except Exception as e:
		result['status'] = 'Error'
		result['msg'] = str(e)
		return JsonResponse({'status': 'Error', 'msg': str(e)})
	
@csrf_exempt	
def download_resource (request) :

	file_path = request.POST.get('file_path')
	print(file_path)
	filename = os.path.basename(file_path)
	print(filename)
	with open(file_path, 'rb') as f:
		response = HttpResponse(f.read(), content_type='application/octet-stream')
		response['Content-Disposition'] = f'attachment; filename="{filename}"'
	return response