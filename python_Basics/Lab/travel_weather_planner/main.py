distance_mi = 10
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi:
    if distance_mi <= 1:
        if is_raining:
            print(False)
        else:
            print(True)
    elif distance_mi > 1 and distance_mi <= 7:
        if not is_raining and has_bike:
            print(True)
        else:
            print(False)
    elif distance_mi > 6 and has_ride_share_app:
        print(True)
    elif distance_mi > 6 and has_car:
        print(True)
    elif distance_mi > 6 and not has_car and not has_ride_share_app:
        print(False)
else:
    print(False)