# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)
            
        self.cabin = cabin
        self.fuel_tank = fuel_tank

    
class Wheel:
    def __init__(self, car = None, wheel_location = None, tpms=None):
        self.car = car
        self.wheel_location = wheel_location
        self.tpms = tpms

    def install_tire(self):
        print('remove old tube.')
         # TODO: Rewrite the following after moving tpms to the 'Wheel' class
        print('cleaned tpms: ', 
              self.car.tpms_di[self.wheel_location].get_serial_number, 
              '.')
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        # TODO: After making tpms an attribute of 'Wheel' class,
        #       rewrite the following.
        return self.tpms.get_pressure()
    
    def set_car(self, car):
        self.car = car
    
    def set_tpms(self, tpms):
        self.tpms = tpms


class Tpms:
    """Tire Pressure Monitoring System.
    """
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number
    
class Engine:
    def __init__(self):
        pass
    
class FuelTank:
    def __init__(self):
        pass
    
class Cabin:
    def __init__(self):
        pass    
    

engine = Engine()
wheels = [Wheel(None, 'front-right', Tpms(983408543)), 
          Wheel(None, 'front-left', Tpms(4343083)), 
          Wheel(None, 'back-right', Tpms(23654835)), 
          Wheel(None, 'back-left', Tpms(3498857))]

cabin  = Cabin()

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)


