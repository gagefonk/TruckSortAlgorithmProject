# Gage Fonk
# ID - #003355709

from HashData import HashData
from Distance import Distance
from Route import Route
from TruckSort import TruckSort
import re

if __name__ == '__main__':
    # create objects and load csv data
    data = HashData()
    distance = Distance()
    route = Route(distance)
    ts = TruckSort()
    ts.sort_packages_into_priorities(data.packages)
    # optimize truck routes
    optimized_truck_1 = route.optimize_route(ts.truck1)
    optimized_truck_2 = route.optimize_route(ts.truck2)
    optimized_truck_3 = route.optimize_route(ts.truck3)
    truck_timeline_1 = distance.check_time(optimized_truck_1, 'truck1')
    truck_timeline_2 = distance.check_time(optimized_truck_2, 'truck2')
    truck_timeline_3 = distance.check_time(optimized_truck_3, 'truck3')
    # calc distance
    td1 = distance.get_total_distance_traveled(optimized_truck_1)
    td2 = distance.get_total_distance_traveled(optimized_truck_2)
    td3 = distance.get_total_distance_traveled(optimized_truck_3)
    total_distance = td1 + td2 + td3


    while(True):
        print("Please Enter a command\n'Report'\n'Lookup'\n'Timestamp\n'Exit'\n")
        start = input().lower()
        print(start)
        if start == 'exit':
            exit(0)
        elif start == 'report':
            # display
            distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
            distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
            distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)
            print('Total Distance = {} Miles\n'.format(total_distance))
        elif start == 'lookup':
            print('Please enter a package ID: \n')
            ans = int(input())
            search = ''
            truck = []
            truck_time = []
            for t in optimized_truck_1:
                if t.get_package_id() == ans:
                    p = t
                    search = ans
                    truck = optimized_truck_1
                    truck_time = truck_timeline_1
            for t in optimized_truck_2:
                if t.get_package_id() == ans:
                    p = t
                    search = ans
                    truck = optimized_truck_2
                    truck_time = truck_timeline_2
            for t in optimized_truck_3:
                if t.get_package_id() == ans:
                    p = t
                    search = ans
                    truck = optimized_truck_3
                    truck_time = truck_timeline_3
            if search != '':
                ed = distance.check_delivery_time(truck, truck_time, int(search))
                print('ID: {} - Address: {} {}, {} - Deadline: {} - Weight: {} - Status: {} - Expected Delivery: {}\n'.format(p.get_package_id(), p.get_address(), p.get_city(), p.get_zip(), p.get_deadline(), p.get_weight(), p.get_delivery_status(), ed))
            else:
                print("Sorry we didnt find a package with that ID number.\n")
        elif start == 'timestamp':
            print('Please Enter a timestamp in the format of HH:MM:SS\n')
            pattern = re.compile("^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$")
            ans = input()
            if pattern.search(ans):
                distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, ans, td1)
                distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, ans, td2)
                distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, ans, td3)
            else:
                print('Please enter timestamp info correctly matching the correct pattern')
        else:
            print('Please enter a valid command.\n')
            pass
