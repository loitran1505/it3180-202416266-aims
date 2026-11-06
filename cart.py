MAX_NUMBERS_ORDERED = 20

class Cart:
    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(disc)
        print("The disc has been added")
        return True

    def total_cost(self):
        return sum(disc.cost for disc in self.items)