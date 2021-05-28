class TruckSort:
    truck1 = []
    truck2 = []
    truck3 = []

    # sort the packages onto the trucks - semi random
    def sort_packages_into_priorities(self, packages):
        priority_truck_1 = []
        np_truck_1 = []
        priority_truck_2 = []
        np_truck_2 = []
        non_priority = []
        for p in packages:
            notes = p.get_notes()
            deadline = p.get_deadline()
            address = p.get_address()

            if id == 13 or id == 15 or id == 19:
                priority_truck_1.append(p)
            elif 'Can only be on' in notes or 'Delayed on flight' in notes:
                priority_truck_2.append(p)
            elif 'Wrong address listed' in notes:
                p.set_address('410 S State St')
                p.set_zip('84111')
                non_priority.append(p)
            elif 'Must be delivered' in notes and deadline != 'EOD':
                priority_truck_1.append(p)
            elif deadline != 'EOD':
                ft_address = []
                for t in priority_truck_1:
                    ft_address.append(t.get_address())
                if address in ft_address:
                    np_truck_1.append(p)
                else:
                    np_truck_2.append(p)
            elif '10:30' not in deadline:
                non_priority.append(p)
            else:
                non_priority.append(p)

        for t in priority_truck_1:
            if len(self.truck1) < 16:
                self.truck1.append(t)
        for t in np_truck_1:
            if len(self.truck1) < 16:
                self.truck1.append(t)
        for t in priority_truck_2:
            if len(self.truck2) < 16:
                self.truck2.append(t)
        for t in np_truck_2:
            if len(self.truck1) < 16:
                self.truck1.append(t)
            elif len(self.truck2) < 16:
                self.truck2.append(t)
            else:
                self.truck3.append(t)
        for t in non_priority:
            if len(self.truck3) < 16:
                self.truck3.append(t)
            elif len(self.truck2) < 16:
                self.truck2.append(t)
            elif len(self.truck1) < 16:
                self.truck1.append(t)
            else:
                print('Not enough room on trucks')
