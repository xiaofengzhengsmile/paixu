from django.shortcuts import render
from django.views import View
# Create your views here.


class SendScore(View):
    """用户上传数据"""

    def post(self, request):

        return render(request, 'index.html')


class ScoreSort(View):

    """查询排序"""
    def get(self, request):
        context = {}
        return render(request, 'paiming.html', context)
