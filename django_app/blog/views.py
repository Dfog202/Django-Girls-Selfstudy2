from django.shortcuts import render,HttpResponse

def main_view(request):
    return HttpResponse("음 ㅋㅋㅋㅋ 빨리!! .....")

def main_view2(request):
    return HttpResponse('이거시 메인뷰 2입니다! 2!!!')