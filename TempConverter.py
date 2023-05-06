# Programm zur Umrechnung in die drei Temperaturskalen C, K, F.
# Autor: Martin Dominiak
# Pythonversion: 3.11.1

# Übergabe Menüauswahl
def get_int(mAuswahl = 0):
   print("\n******* Terperaturwandler 0.2 *******\n")
   print("(1) Umrechnung von Celsius nach Kelvin")
   print("(2) Umrechnung von Celsius nach Fahrenheit")
   print("(3) Umrechnung von Kelvin nach Celsius")
   print("(4) Umrechnung von Kelvin nach Fahrenheit")
   print("(5) Umrechnung von Fahrenheit nach Celsius")
   print("(6) Umrechnung von Fahrenheit nach Kelvin")
   print("\n(7) Beenden\n")
   while True: # Endlosschliefe mit Rückgabewert
      try:
           if (mAuswahl > 7) or (mAuswahl == 0 ): # Überprüfung auf flasche nummerische Eingabe
              mAuswahl = int(input("Bitte Auswahl treffen: "))
           else:
                return mAuswahl
      except ValueError: # überprüfung auf falsche Eingabe
           print("Ungütlige Eingabe!\n") 

# Berechnung und Ausgabe der einzelnene Temperaturen
def Berechnung(auswahl):
    def CnachK(temp): # Funktion zur Berechnung Celsius nach Kelvin
      while True: # Endlosschleife mit Rückgabewert
         try:
            temp = float(input("Geben sie eine Temperatur in °C ein: ")) 
            if temp < -273.15: # Überprüfung Eingabe über abslout Null
               print("Temperatur unter dem absloutem Nullpunkt vom -273,15 °C.\nEINGABE WIEDERHOLEN:\n ")
            else:                return (temp, temp + 273.15) # Rückgabe in Celsius und Kelvin
         except ValueError: # Überprüfung auf falsche Eingabe
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")
# Analog 5 weitere Umrechnungen:
    def CnachF(temp): # Fuktion zur Berechnung Celsius nach Fahrenheit
      while True:
         try:
            temp = float(input("Geben sie eine Temperatur in °C ein: "))
            if temp < -273.15:
               print("Temperatur unter dem absloutem Nullpunkt vom -273,15 °C.\nEINGABE WIEDERHOLEN:\n ")
            else:
                return (temp, temp * (9/5) + 32)
         except ValueError:
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")

    def KnachC(temp): # Funktion zur Berechnung Kelvin nach Celsius
      while True:
         try:
            temp = float(input("Geben sie eine Temperatur in °K ein: "))
            if temp < 0:
               print("Temperatur unter dem absloutem Nullpunkt vom 0°K.\nEINGABE WIEDERHOLEN:\n ")
            else:
                return (temp, temp - 273.15)
         except ValueError:
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")

    def KnachF(temp): # Funktion zur Berechnung Kelvin nach Fahrenheit
      while True:
         try:
            temp = float(input("Geben sie eine Temperatur in °K ein: "))
            if temp < 0:
               print("Temperatur unter dem absloutem Nullpunkt vom 0°K.\nEINGABE WIEDERHOLEN:\n ")
            else:
                return (temp, (temp - 273.15) * (9/5) + 32)
         except ValueError:
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")

    def FnachC(temp): # Funktion zur Berechnung Fahrenheit nach Celsius
      while True:
         try:
            temp = float(input("Geben sie eine Temperatur in °F ein: "))
            if temp < -459.67:
               print("Temperatur unter dem absloutem Nullpunkt vom -459.67°F.\nEINGABE WIEDERHOLEN:\n ")
            else:
                return (temp, (temp - 32) * 5/9)
         except ValueError:
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")

    def FnachK(temp): # Funktion zur Berechnung Fahrenheit nach Kelvin
      while True:
         try:
            temp = float(input("Geben sie eine Temperatur in °F ein: "))
            if temp < -459.67:
               print("Temperatur unter dem absloutem Nullpunkt -459.67°F.\nEINGABE WIEDERHOLEN:\n ")
            else:
                return (temp, (temp - 32) * 5/9 + 273.15)
         except ValueError:
             print("Ungültige Eingabe. Bitte nochmals probieren:\n")

   # Ausgabe der errechneten Werte
    if int(auswahl) == 1: # Menüauswahl
      tempSwitch = CnachK(temp = 0) # Übergabe der Liste mit der original - und umgerechneten Temperatur
      print(tempSwitch [0], "°C = ", "{:.2F}".format(tempSwitch [1]),'°K\n', sep = "") # Ausgabe beider Temperaturen
    elif int(auswahl) == 2:
       tempSwitch = CnachF(temp = 0)
       print(tempSwitch [0], "°C = ", "{:.2F}".format(tempSwitch [1]),'°F\n', sep = "")
    elif int(auswahl) == 3:
      tempSwitch = KnachC(temp = 0)
      print(tempSwitch [0], "°K = ", "{:.2F}".format(tempSwitch [1]),'°C\n', sep = "")    
    elif int(auswahl) == 4:
      tempSwitch = KnachF(temp = 0)
      print(tempSwitch [0], "°K = ", "{:.2F}".format(tempSwitch [1]),'°F\n', sep = "") 
    elif int(auswahl) == 5:
      tempSwitch = FnachC(temp = 0)
      print(tempSwitch [0], "°F = ", "{:.2F}".format(tempSwitch [1]),'°C\n', sep = "") 
    elif int(auswahl) == 6:
      tempSwitch = FnachK(temp = 0)
      print(tempSwitch [0], "°F = ", "{:.2F}".format(tempSwitch [1]),'°K\n', sep = "") 
      
# Main Fuktion zum steuern des Programmflusses.
def main(auswahl = 0):
   while (auswahl != 7):
         auswahl = get_int()
         Berechnung(auswahl)
   print("Beehren Sie uns bald wieder.\n")

main()