class Package:

    def __init__(self, ID, delivery_address, city, state, zipcode, deadline, weight):
        self.ID = ID
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.status = "At Hub"
        self.departure_time = None
        self.delivery_time = None

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time < convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At Hub"

    def __str__(self) :
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.delivery_address, self.city, self.state, self.zipcode,
                                                       self.deadline, self.weight, self.delivery_time,
                                                       self.status)


