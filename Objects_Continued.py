class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []
    def spending(self, cost):
        self.total.append(cost)

sportStore = Shopping("Kayak", "High Quality")

sportStore.spending(20)
sportStore.spending(10)
sportStore.spending(15)

print(sportStore.total)