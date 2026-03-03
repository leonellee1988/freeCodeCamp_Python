# Build a travel weather planner

distance_mi = 10
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1 and is_raining == False:
    print(True)
elif (distance_mi > 1 and distance_mi <= 6) and (has_bike == True and is_raining == False):
    print(True)
elif distance_mi > 6 and (has_car == True or has_ride_share_app == True):
    print(True)
else:
    print(False)