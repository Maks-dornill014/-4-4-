class Device:
    def __init__(self, name):
        
        self.name = name
        self.is_on = False

    def turn_on(self):
        
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} увімкнено.")
        else:
            print(f"{self.name} вже увімкнений.")

    def turn_off(self):
        
        if self.is_on:
            self.is_on = False
            print(f"{self.name} вимкнено.")
        else:
            print(f"{self.name} вже вимкнений.")



class Television(Device):
    def __init__(self, name, screen_size):
        
        super().__init__(name)
        self.screen_size = screen_size

    def change_channel(self, channel):
       
        if self.is_on:
            print(f"Канал на {self.name} змінено на {channel}.")
        else:
            print(f"Увімкніть {self.name}, щоб змінити канал.")



class Computer(Device):
    def __init__(self, name, processor):
        
        super().__init__(name)
        self.processor = processor

    def run_program(self, program_name):
        
        if self.is_on:
            print(f"Програма '{program_name}' запущена на {self.name}.")
        else:
            print(f"Увімкніть {self.name}, щоб запустити програму.")



class SmartWatch(Device):
    def __init__(self, name, brand):
        
        super().__init__(name)
        self.brand = brand

    def show_time(self):
       
        if self.is_on:
            print(f"{self.name} показує поточний час.")
        else:
            print(f"Увімкніть {self.name}, щоб побачити час.")



tv = Television("Телевізор Samsung", 55)
tv.turn_on()
tv.change_channel(7)
tv.turn_off()

pc = Computer("Ноутбук Lenovo", "Intel i7")
pc.turn_on()
pc.run_program("Word")
pc.turn_off()

watch = SmartWatch("Apple Watch", "Apple")
watch.turn_on()
watch.show_time()
watch.turn_off()
