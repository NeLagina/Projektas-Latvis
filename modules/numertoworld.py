

def numertoworld(numerinput):
    units = ["", "Vienas", "Du", "Trys", "Keturi", "Penki", "Šeši", "Septyni", "Aštuoni", "Devyni"]
    tens = ["", "Dešimt", "Dvidešimt", "Trisdešimt", "Keturiasdešimt", "Penkiasdešimt", "Šešiasdešimt", "Septyniasdešimt", "Aštuoniasdešimt", "Devyniasdešimt"]
    hundreds = ["", "Šimtas", "Dviejų šimtų", "Trejų šimtų", "Keturių šimtų", "Penkių šimtų", "Šešių šimtų", "Septynių šimtų", "Aštuonių šimtų", "Devynių šimtų"]
    
    # Separate the integer and decimal parts
    

# Remove the Euro symbol
    
    number = str(numerinput).replace('€', '')
    parts = number.split('.')
    
    if len(parts) == 1: 
        integer_part = int(parts[0])
        decimal_part = 0
    elif len(parts) == 2: 
        integer_part = int(parts[0])
        decimal_part = int(parts[1])
    else:
        raise ValueError("Invalid number format")

 
    euras = "eurai" if integer_part % 10 in [1, 2, 3] else "eura" if integer_part % 10 == 4 else "euru"


    integer_text = ""
    decimal_text = ""
    if integer_part >= 5:
        if integer_part == 0:
            decimal_text = numertoworld(decimal_part) + " centų"
        elif integer_part < 10:
            integer_text = units[integer_part] + " " + euras
        elif integer_part < 100:
            integer_text = tens[integer_part // 10] + " " + units[integer_part % 10] + " " + euras
        else:
            integer_text = (
                hundreds[integer_part // 100]
                + " "
                + numertoworld(integer_part % 100)
                + " "
                + euras
            )
        
        if decimal_part > 0:
            decimal_text = numertoworld(decimal_part) + " centų"

        return f"{integer_text} ir {decimal_text}" if decimal_part > 0 else integer_text