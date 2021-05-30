from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .stats import get_stat_data
# from .daily_predicted_data_delhi import get_daily_delhi_pred
from .daily_predicted_data_delhi import get_daily_data_pred
from .monthly_predicted_data import get_monthly_pred
from .yearly_predicted_data import get_yearly_pred
from .live_data import get_live_data
from pprint import pprint
from .models import CityName
from aerify.settings import BASE_DIR
from aerify_api.models import aerifyDailyAPI, aerifyMonthlyAPI, aerifyYearlyAPI
import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CITY_NAME=''
# class Index(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(requests, "app_aerify/index.html", context)
#
#     def post(self, requests, *args, **kwargs):
#         city_n = requests.POST.get("clickedCity")
#         print(city_n)
#         q_set = CityName.objects.filter(id=1)
#         if q_set.count() != 0:
#             obj = q_set.first()
#         obj.city = city_n
#         obj.save()
#         context = {}
#         return render(request, "app_aerify/index.html", context)


# @csrf_exempt
# def indexView(request, *args, **kwargs):
#     if request.method == "GET":
#         context = {}
#         print(BASE_DIR)
#         return render(request, "app_aerify/index.html", context)
#     elif request.method == "POST":
#         city_n = request.POST.get("clickedCity")
#         print(city_n)
#         q_set = CityName.objects.filter(id=1)
#         if q_set.count() != 0:
#             obj = q_set.first()
#         obj.city = city_n
#         obj.save()
#         context = {}
#         return render(request, "app_aerify/index.html", context)

@csrf_exempt
def indexView(request, *args, **kwargs):
    if request.method == "GET":
        context = {}
        print(BASE_DIR)
        return render(request, "app_aerify/index.html", context)
    elif request.method == "POST":
        city_n = request.POST.get("clickedCity")
        CITY_NAME = city_n
        print(city_n)
        q_set = CityName.objects.filter(id=1)
        print("QSET BEFORE IF CLAUSE IS ",q_set)
        print("QSET BEFORE IF CLAUSE IS ",CityName.objects)
        if q_set.count() != 0:
            obj = q_set.first()
            print("QSET IS ",q_set)
        else:
            # q_set.city=city_n
            CityName.objects.create(id=1,city=city_n)

        print("QSET AFTER IF CLAUSE IS ",q_set)
        obj.city = city_n
        obj.save()
        context = {}
        return render(request, "app_aerify/index.html", context)




# @csrf_exempt
# def dataPageView(request, *args, **kwargs):
#     if request.method == "GET":
#         q_set = CityName.objects.filter(id=1)
#         if q_set.count() != 0:
#             obj = q_set.first()
#         city = obj.city
#         print("City Name Received: " + city)
#         live_data = get_live_data(city)
#         print(live_data)
#         context = {
#             "city_name": city,
#             "data": live_data
#         }
#         return render(request, "app_aerify/second.html", context)
#     elif request.method == "POST":
#         pass


@csrf_exempt
def dataPageView(request, *args, **kwargs):
    if request.method == "GET":
        q_set = CityName.objects.filter(id=1)
        # q_set=CityName.objects.filter(city=CITY_NAME)
        if q_set.count() != 0:
            q_set = CityName.objects.filter(id=1)
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        live_data = get_live_data(city)
        print(live_data)
        context = {
            "city_name": city,
            "data": live_data
        }
        return render(request, "app_aerify/second.html", context)
    elif request.method == "POST":
        pass



class LiveDataView(View):
    def get(self, request, *args, **kwargs):
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            q_set = CityName.objects.filter(id=1)
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        live_data = get_live_data(city)
        # pprint(stat_data)
        return JsonResponse(live_data, safe=False)


class DailyDataView(View):
    def get(self, request, *args, **kwargs):
        # daily_delhi_pred = get_daily_delhi_pred(BASE_DIR)
        # print(daily_delhi_pred)
        # return JsonResponse(daily_delhi_pred)

        print(" Inside DailyDataView")
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        daily_data = get_daily_data_pred(city, BASE_DIR)
        print(daily_data)
        print(" Exiting DailyDataView")        
        
        return JsonResponse(daily_data)


class MonthlyDataView(View):
    def get(self, request, *args, **kwargs):
        print(" Inside MonthlyDataView")
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        monthly_data = get_monthly_pred(city, BASE_DIR)
        # pprint(monthly_data)
        print(" Exiting MonthlyDataView")
        return JsonResponse(monthly_data)


class YearlyDataView(View):
    def get(self, request, *args, **kwargs):
        q_set = CityName.objects.filter(id=1)
        if q_set.count() != 0:
            obj = q_set.first()
        city = obj.city
        print("City Name Received: " + city)
        # monthly_data = get_monthly_pred(city)
        yearly_data = get_yearly_pred(city, BASE_DIR)
        # pprint(yearly_data)
        return JsonResponse(yearly_data)


class StatisticsDataView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("<h1> This is the Home Page. </h1>")
        stat_data = get_stat_data(BASE_DIR)
        # pprint(stat_data)
        return JsonResponse(stat_data)


class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("<h1> This is the Home Page. </h1>")
        stat_data = get_stat_data(BASE_DIR)
        # pprint(stat_data)
        return render(request, "app_aerify/sidebar.html", stat_data)


class DatabaseDailyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        print("Inside DatabaseDailyPredictedDatafill")
        qs = aerifyDailyAPI.objects.all()
        for i in qs:
            print(i, type(i), i.daily_updated)
            i.delete()
            print("Object deleted")
        df = pd.read_csv(BASE_DIR+"/app_aerify/daily_predicted_data_delhi/predicted_delhi.csv")
        print(df.count())
        print(df.values)
        c = 0
        for j in df.values:
            print(j[0], j[1])
            obj = aerifyDailyAPI()
            obj.daily_city = "Delhi"
            obj.daily_date = j[0]
            obj.daily_aqi = j[1]
            obj.save()
            print(c)
            print("================================")
            c += 1
        print(c)
        print("Exiting DatabaseDailyPredictedDatafill")
        return HttpResponse("<h1> This is the Database Daily Predicted Data Fill Page. </h1>")


class DatabaseMonthlyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        print("Inside DatabaseMonthlyPredictedDatafill")
        qs = aerifyMonthlyAPI.objects.all()
        for i in qs:
            # print(i, type(i), i.daily_updated)
            i.delete()
            # print("Object deleted")
        folder_path = BASE_DIR + "/app_aerify/monthly_predicted_data/"
        dirs = os.listdir(
            BASE_DIR + "/app_aerify/monthly_predicted_data")
        # print(dirs)
        # c = 0
        for i in dirs:
            # print(folder_path+i)
            df = pd.read_csv(folder_path + i)
            # print(i[5:-4])
            # print(df.count())
            # print(df.values)
            for j in df.values:
                # print(j[0], j[6], i[5:-4])
                obj = aerifyMonthlyAPI()
                obj.monthly_city = i[5:-4]
                obj.monthly_date = j[0]
                obj.monthly_aqi = j[6]
                obj.save()
            # print(c)
            # print("================================")
            # c += 1
        # print(c)
        print("Exiting DatabaseMonthlyPredictedDatafill")
        return HttpResponse("<h1> This is the Database Monthly Predicted Data Fill Page. </h1>")


class DatabaseYearlyPredictedDatafill(View):
    def get(self, request, *args, **kwargs):
        print("Inside DatabaseYearlyPredictedDatafill")
        qs = aerifyYearlyAPI.objects.all()
        for i in qs:
            # print(i, type(i), i.daily_updated)
            i.delete()
            # print("Object deleted")
        folder_path = BASE_DIR + "/app_aerify/yearly_predicted_data/"
        dirs = os.listdir(
            BASE_DIR + "/app_aerify/yearly_predicted_data")
        # print(dirs)
        # c = 0
        for i in dirs:
            # print(folder_path+i)
            df = pd.read_csv(folder_path + i)
            # print(i[5:-4])
            # print(df.count())
            # print(df.values)
            for j in df.values:
                # print(j[0], j[6], i[5:-4])
                obj = aerifyYearlyAPI()
                obj.yearly_city = i[5:-4]
                obj.yearly_date = j[0]
                obj.yearly_aqi = j[6]
                obj.save()
            # print(c)
            # print("================================")
            # c += 1
        # print(c)
        print("Exiting DatabaseYearlyPredictedDatafill")
        return HttpResponse("<h1> This is the Database Yearly Predicted Data Fill Page. </h1>")
