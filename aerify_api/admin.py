from django.contrib import admin
from .models import aerifyDailyAPI, aerifyMonthlyAPI, aerifyYearlyAPI


class aerifyDailyAPIModelAdmin(admin.ModelAdmin):
    list_display = ["id", "daily_city", "daily_aqi", "daily_date", "daily_created", "daily_updated"]
    list_display_links = ["id"]
    list_filter = ["daily_city", "daily_date"]

admin.site.register(aerifyDailyAPI, aerifyDailyAPIModelAdmin)


class aerifyMonthlyAPIModelAdmin(admin.ModelAdmin):
    list_display = ["id", "monthly_city", "monthly_date", "monthly_created", "monthly_updated"]
    list_display_links = ["id"]
    list_filter = ["monthly_city", "monthly_date"]


admin.site.register(aerifyMonthlyAPI, aerifyMonthlyAPIModelAdmin)


class aerifyYearlyAPIModelAdmin(admin.ModelAdmin):
    list_display = ["id", "yearly_city", "yearly_date", "yearly_created", "yearly_updated"]
    list_display_links = ["id"]
    list_filter = ["yearly_city", "yearly_date"]


admin.site.register(aerifyYearlyAPI, aerifyYearlyAPIModelAdmin)
