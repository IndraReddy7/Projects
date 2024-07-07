#!/usr/bin/env python
# coding: utf-8

# In[34]:


class Train:
    def __init__(self, train_number, name, source, destination, seats):
        self.train_number = train_number
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats

class ReservationSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def reserve_ticket(self, train_number, num_seats):
        for train in self.trains:
            if train.train_number == train_number:
                if train.seats >= num_seats:
                    train.seats -= num_seats
                    return f"Reserved {num_seats} seats on {train.name} (Train {train.train_number})."
                else:
                    return f"Sorry, not enough seats available on {train.name}."
        return f"Train with number {train_number} not found."

    def check_status(self, train_number):
        for train in self.trains:
            if train.train_number == train_number:
                return f"Seats available on {train.name} (Train {train.train_number}): {train.seats}"
        return f"Train with number {train_number} not found."

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please try again.")

def main():
    system = ReservationSystem()

    system.add_train(Train(123, "Express", "City A", "City B", 100))
    system.add_train(Train(456, "Superfast", "City B", "City C", 150))

    S = ['Guntur', 'guntur' , 'Vijayawada', 'vijayawada' , 'Bapatla', 'bapatla']
    D = ['Nellore' , 'nellore' , 'Sulurupeta' , 'sulurupeta' , 'Chennai Central' , 'chennai central']

    c = get_valid_input("Enter boarding station: ", S)
    print(f"Boarding station is: {c}")

    d = get_valid_input("Enter destination station: ", D)
    print(f"Destination station is: {d}")

    a = int(input("Enter the train number: "))
    if a in [train.train_number for train in system.trains]:
        b = int(input("Enter the number of seats: "))
        print(system.reserve_ticket(a, b), f'From {c} to {d}')
    else:
        print("Please enter a valid train number!")

if __name__ == "__main__":
    main()


# In[ ]:




