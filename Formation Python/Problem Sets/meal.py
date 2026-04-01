# L'utilisateur entre une heure sous la forme #:## ou ##:##. Le programme lui dit s'il est l'heure de manger
def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Convertir le str en float
def convert(time):
    # Séparer les heures et les minutes
    hour,minute = time.split(":")
    # Convertir les heures et minutes en float et convertir les minutes en heures
    hour , minute = float(hour) , float(minute) / 60
    return hour + minute

main()