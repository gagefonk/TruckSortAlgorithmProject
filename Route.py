class Route:

    def __init__(self, distance):
        self.d = distance

    # This is the algorithm for optimizing the route
    def optimize_route(self, truck):

        main_route = []
        prev_location = 0
        while len(truck) > 0:
            weight = 50.0
            existing_address = []
            for a in main_route:
                existing_address.append(a.get_address())
            for t in truck:
                if t.get_address in existing_address:
                    temp_package = t
                else:
                    new_location = self.d.check_location_num_from_address(t.get_address())
                    p_miles = float(self.d.check_distance(new_location, prev_location))
                    if p_miles <= weight:
                        weight = p_miles
                        temp_package = t
            main_route.append(temp_package)
            prev_location = self.d.check_location_num_from_address(temp_package.get_address())
            truck.remove(temp_package)
        return main_route

