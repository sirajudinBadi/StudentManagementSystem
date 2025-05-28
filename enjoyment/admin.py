from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
  list_display = ('sports_id', 'sports_name', 'coach_name', 'start_year')
  search_fields = ('sports_name', 'coach_name')
  list_filter = ('start_year', 'coach_name')


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
  list_display = ('block', 'room_no', 'room_type', 'no_of_beds', 'cost_per_bed', 'room_status')
  search_fields = ("block", 'room_no')
  list_filter = ('block', 'room_no', 'room_type', 'no_of_beds', 'cost_per_bed', 'room_status')

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
  list_display = ("route_name", "vehicle_num", "driver_name", "license_num", "driver_mobile", "driver_address")
  search_fields = ('route_name', "vehicle_num", "driver_name", "license_num", "driver_mobile",)
  list_filter = ('route_name', "vehicle_num", "driver_name", "license_num", "driver_mobile",)