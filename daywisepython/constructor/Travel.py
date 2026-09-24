class Travel:
    def __init__(self, name, source, destination, price):
        self.name = name
        self.source = source
        self.destination = destination
        self.price = price

    def display(self):
        print("Passenger:", self.name)
        print("From:", self.source)
        print("To:", self.destination)
        print("Ticket Price:", self.price)

t = Travel("Kalyani", "Pune", "Satara", 1000)
t.display()