from typing import Literal

class FuelStation:

    allowed_fuel_type = Literal["diesel","petrol","electric"]

    def __init__(self, diesel: int, petrol: int, electric: int):
        self.diesel = diesel
        self.petrol = petrol
        self.electric = electric

        self.max_spot = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }


    def fuel_vehicle(self,fuel_type: allowed_fuel_type) -> bool:
        if fuel_type == 'diesel':
            if self.diesel > 0:
                self.diesel-= 1
                return True
            else:
                return False
            
        elif fuel_type == 'petrol':
            if self.petrol > 0:
                self.petrol-= 1
                return True
            else:
                return False
            
        elif fuel_type == 'electric':
            if self.electric > 0:
                self.electric-= 1
                return True
            else:
                return False
        
        else:
            return False
            
            
    def open_fuel_slot(self,fuel_type: allowed_fuel_type) -> bool:
        if fuel_type == 'diesel':
            if self.diesel == self.max_spot.get('diesel'):
                return False
            else:
                self.diesel += 1
                return True
            
        elif fuel_type == 'petrol':
            if self.petrol == self.max_spot.get('petrol'):
                return False
            else:
                self.petrol += 1
                return True
            
        elif fuel_type == 'electric':
            if self.electric == self.max_spot.get('electric'):
                return False
            else:
                self.electric += 1
                return True
            
        else:
            return False
            

if __name__ == "__main__":
    fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
    print(fuel_station.fuel_vehicle("diesel")) 
    print(fuel_station.fuel_vehicle("petrol"))
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.fuel_vehicle("electric")) 
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.open_fuel_slot("diesel")) 
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.open_fuel_slot("electric"))
    print(fuel_station.open_fuel_slot("electric"))

