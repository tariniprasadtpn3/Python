class Computer:
    def __init__(self,cpu,ram) -> None:
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print("Hii Computer have ",self.cpu,self.ram)    

obj1 = Computer("i5",8)
obj1.config()        