# L'utilisateur entre une date au format MM-DD-YYYY ou Mois Jour, Année
# Le programme renvoit la date au format YYYY-MM-DD

def main():
    d = input_date()
    print(d)

def input_date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            
            # Si le format est MM/DD/YYYY
            if "/" in date:
                month,day,year = date.split("/")
                month,day,year = int(month),int(day),int(year)
            
            # Si le format est Mois Jour, Année
            elif "," in date:
                month_day,year = date.split(",")
                month,day = month_day.split()
                # Si le mois est dans la liste, le transforme en nombre
                if month.capitalize() in months:
                    month = months.index(month.capitalize()) + 1
                month,day,year = int(month),int(day),int(year)

            # Si ce n'est aucun format, redemande une date    
            else:
                continue

        except ValueError:
            pass
        else:
            # La date doit exister
            if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                return f"{year:04}-{month:02}-{day:02}"

main()