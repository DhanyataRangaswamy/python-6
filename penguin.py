class Bird:
    def __init__(self):
        print("The bird is ready")

    def whoisit(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
      super().__init__()
      print("Penguin is ready")

    def whoisit(self):
          print(Penguin)
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisit()
peggy.swim()
peggy.run()

    