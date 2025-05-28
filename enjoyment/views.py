from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
#---------------------------------------------------SPORTS Section-----------------------------------------------

@login_required
def add_sports(request):
  if request.method == "POST":
    sports_id = request.POST.get('sports_id')
    sports_name = request.POST.get('sports_name')
    coach_name = request.POST.get('coach_name')
    start_year = request.POST.get('start_year')

    sport = Sports.objects.create(
      sports_id = sports_id,
      sports_name = sports_name,
      coach_name = coach_name,
      start_year = start_year,
    )
    messages.success(request, "Sports Added Successfully")
  return render(request, "enjoyment/add-sports.html")

@login_required
def view_sports(request):
  sports_list = Sports.objects.all()
  context = {
    "sports_list" : sports_list,
  }
  return render(request, "enjoyment/sports.html", context)


@login_required
def edit_sports(request, slug):
  sport = get_object_or_404(Sports, slug=slug)

  if request.method == "POST":
    sports_id = request.POST.get('sports_id')
    sports_name = request.POST.get('sports_name')
    coach_name = request.POST.get('coach_name')
    start_year = request.POST.get('start_year')

    sport.sports_id = sports_id
    sport.sports_name = sports_name
    sport.coach_name = coach_name
    sport.start_year = start_year
    sport.save()

    return redirect('view_sports')
  return render(request, "enjoyment/edit-sports.html", {"sport" : sport})
    


@login_required
def delete_sports(request, slug):
  if request.method == "POST":
    sport = get_object_or_404(Sports, slug=slug)
    sport.delete()
    return redirect('view_sports')
  return HttpResponseForbidden()


#---------------------------------------------------HOSTEL Section-----------------------------------------------

@login_required
def add_hostel(request):
  if request.method == "POST":
    block = request.POST.get('block')
    room_no = request.POST.get('room_no')
    room_type = request.POST.get('room_type')
    no_of_beds = request.POST.get('no_of_beds')
    cost_per_bed = request.POST.get('cost_per_bed')
    room_status = request.POST.get('room_status')

    room = Hostel.objects.create(
      block = block,
      room_no = room_no,
      room_type = room_type,
      no_of_beds = no_of_beds,
      cost_per_bed = cost_per_bed,
      room_status = room_status,
    )
    messages.success(request, "Room Added Successfully")
  return render(request, "enjoyment/add-room.html")

@login_required
def view_hostel(request):
  room_list = Hostel.objects.all()
  context = {
    "room_list" : room_list,
  }
  return render(request, "enjoyment/hostel.html", context)


@login_required
def edit_hostel(request, slug):
  room = get_object_or_404(Hostel, slug = slug)
  if request.method == "POST":
    block = request.POST.get('block')
    room_no = request.POST.get('room_no')
    room_type = request.POST.get('room_type')
    no_of_beds = request.POST.get('no_of_beds')
    cost_per_bed = request.POST.get('cost_per_bed')
    room_status = request.POST.get('room_status')

    room.block = block
    room.room_no = room_no
    room.room_type = room_type
    room.no_of_beds = no_of_beds
    room.cost_per_bed = cost_per_bed
    room.room_status = room_status
    room.save()

    return redirect('view_hostel')
  return render(request, "enjoyment/edit-room.html", {"room" : room})


@login_required
def delete_hostel(request, slug):
  if request.method == 'POST':
    room = get_object_or_404(Hostel, slug=slug)
    room.delete()
    return redirect('view_hostel')
  return HttpResponseForbidden()



#---------------------------------------------------TRANSPORT Section-----------------------------------------------

@login_required
def add_transport(request):
  if request.method == "POST":
    route_name = request.POST.get('route_name')
    vehicle_num = request.POST.get('vehicle_num')
    driver_name = request.POST.get('driver_name')
    license_num = request.POST.get('license_num')
    driver_mobile = request.POST.get('driver_mobile')
    driver_address = request.POST.get('driver_address')

    route = Transport.objects.create(
      route_name = route_name,
      vehicle_num = vehicle_num,
      driver_name = driver_name,
      license_num = license_num,
      driver_mobile = driver_mobile,
      driver_address = driver_address,
    )
    messages.success(request, "Route Added Successfully")
  return render(request, "enjoyment/add-transport.html")


@login_required
def view_transport(request):
  route_list = Transport.objects.all()
  context = {
    "route_list" : route_list,
  }
  return render(request, "enjoyment/transport.html", context)

@login_required
def edit_transport(request, slug):
  route = get_object_or_404(Transport, slug=slug)
  if request.method == "POST":
    route_name = request.POST.get('route_name')
    vehicle_num = request.POST.get('vehicle_num')
    driver_name = request.POST.get('driver_name')
    license_num = request.POST.get('license_num')
    driver_mobile = request.POST.get('driver_mobile')
    driver_address = request.POST.get('driver_address')

    route.route_name = route_name
    route.vehicle_num = vehicle_num
    route.driver_name = driver_name
    route.license_num = license_num
    route.driver_mobile = driver_mobile
    route.driver_address = driver_address
    route.save()

    return redirect('view_transport')
  return render(request, "enjoyment/edit-transport.html", {"route" : route})


@login_required
def delete_transport(request, slug):
  if request.method == "POST":
    route = get_object_or_404(Transport, slug=slug)
    route.delete()
    return redirect('view_transport')
  return HttpResponseForbidden()