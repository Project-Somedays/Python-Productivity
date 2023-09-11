from wifi_connect import connect_to_sparkhaus_wifi
import json
from datetime import datetime
from time import sleep_ms

def update_induction_register():
    print("Induction register updated")

def connect_to_flask_app():
    print("Connected to Flask App")
    
def get_equipment_name():
    print("Your name is Big Red!")
    
def start_equipment_session():
    print("Starting equipment session")

def light_LED(colour: str):
    print(f"Lighting {colour} LED")

def main():
    print("Connecting to wifi")
    connect_to_sparkhaus_wifi()
    
    print("Connecting to Flask App")
    connect_to_flask_app()
    
    print("Updating induction register")
    update_induction_register()
    
    print("Getting equipment name from server")
    get_equipment_name()
    
    print("Initialising RFID")
    rfid = PiicoDev_RFID()

    print("Loading json")
    with open("induction_register.json", "r") as fh:
        induction_register = json.load(fh)
    
    print("Waiting for an RFID Scan")
    while True:
        username = rfid.read_text()
        if username in induction_register.keys() and datetime.strptime(induction_register[username],"%d/%m/%Y") - datetime.today() > 365:
            start_equipment_session()
            light_LED("GREEN")
        else:
            light_LED("RED")

        sleep_ms(100)
        
        
    

if __name__ == '__main__':
    main()