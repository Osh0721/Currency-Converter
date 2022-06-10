def USD_conv(value,currency):

    if(currency=="AUD"):

     return value*1.39

    elif(currency=="LKR"):

        return value *361.20

    elif (currency == "YEN"):

        return value * 130.84

    elif (currency == "EURO"):

        return value * 0.93

    elif (currency == " Pound"):

        return value * 0.80

    elif (currency == " Riyal"):

        return value * 3.75
    elif (currency == "Yuan"):

        return value *3.75

    elif (currency == "INR"):

        return value * 77.61


def AUD_conv(value, currency):
    if (currency == "USD"):

        return value * 0.72

    elif (currency == "LKR"):

        return value * 260.33

    elif (currency == "YEN"):

        return value * 94.65

    elif (currency == "EURO"):

        return value * 0.67

    elif (currency == " Pound"):

        return value * 0.58

    elif (currency == " Riyal"):

        return value * 2.70
    elif (currency == "Yuan"):

        return value * 4.80

    elif (currency == "INR"):

        return value * 55.94

def YEN_conv(value, currency):
    if (currency == "USD"):

        return value * 0.0076

    elif (currency == "LKR"):

        return value * 2.76

    elif (currency == "AUD"):

        return value * 0.011

    elif (currency == "EURO"):

        return value * 0.0071

    elif (currency == " Pound"):

        return value * 0.0061

    elif (currency == " Riyal"):

        return value *0.029
    elif (currency == "Yuan"):

        return value * 0.051

    elif (currency == "INR"):

        return value * 0.59


def LKR_conv(value, currency):
    if (currency == "USD"):

        return value *0.0028

    elif (currency == "YEN"):

        return value *0.36

    elif (currency == "AUD"):

        return value *0.0038

    elif (currency == "EURO"):

        return value *0.0026

    elif (currency == " Pound"):

        return value *0.0022

    elif (currency == " Riyal"):

        return value *0.010
    elif (currency == "Yuan"):

        return value *0.018

    elif (currency == "INR"):

        return value *0.22

def EURO_conv(value, currency):
    if (currency == "USD"):

        return value *1.07

    elif (currency == "YEN"):

        return value *140.30

    elif (currency == "AUD"):

        return value *1.49

    elif (currency == "LKR"):

        return value *387.21

    elif (currency == " Pound"):

        return value *0.86

    elif (currency == " Riyal"):

        return value *4.02

    elif (currency == "Yuan"):

        return value *7.14

    elif (currency == "INR"):

        return value *83.20

def Pound_conv(value, currency):
    if (currency == "USD"):

        return value *1.25

    elif (currency == "YEN"):

        return value *163.41

    elif (currency == "AUD"):

        return value *1.73

    elif (currency == "LKR"):

        return value *451.09

    elif (currency == "EURO"):

        return value *1.16

    elif (currency == "Riyal"):

        return value *4.68

    elif (currency == "Yuan"):

        return value *8.32

    elif (currency == "INR"):

        return value *96.93


def Yuan_conv(value, currency):
    if (currency == "USD"):

        return value *0.15

    elif (currency == "YEN"):

        return value *19.65

    elif (currency == "AUD"):

        return value *0.21

    elif (currency == "LKR"):

        return value *54.23

    elif (currency == "EURO"):

        return value *0.14

    elif (currency == "Pound"):

        return value *0.12

    elif (currency == "Riyal"):

        return value *0.56

    elif (currency == "INR"):

        return value *11.65

def Riyal_conv(value, currency):
        if (currency == "USD"):

            return value * 0.27

        elif (currency == "YEN"):

            return value * 34.89

        elif (currency == "AUD"):

            return value * 0.37

        elif (currency == "LKR"):

            return value * 96.30

        elif (currency == "EURO"):

            return value * 0.25

        elif (currency == "Pound"):

            return value * 0.21

        elif (currency == "Yuan"):

            return value * 1.78

        elif (currency == "INR"):

            return value * 20.69


def INR_conv(value, currency):
    if (currency == "USD"):

        return value *0.013

    elif (currency == "YEN"):

        return value *1.69

    elif (currency == "AUD"):

        return value *0.018

    elif (currency == "LKR"):

        return value *4.65

    elif (currency == "EURO"):

        return value *0.012

    elif (currency == "Pound"):

        return value *0.010

    elif (currency == "Yuan"):

        return value *0.086

    elif (currency == "Riyal"):

        return value *0.048



print("Welcome to the Currency converter".upper())



while True:
    currency = input( "Which currency you want to convert?".upper() + "\nUSD\nAUD\nYEN\nLKR\nEURO\nPound\nYuan\nRiyal\nINR")
    Value = int(input("Enter the value to convert?".upper()))
    Converter_Currency = input("To Which currency you want to convert?".upper() + "\nUSD\nAUD\nYEN\nLKR\nEURO\nPound\nYuan\nRiyal\nINR")

    if(currency=="USD"):
        print(USD_conv(Value,Converter_Currency))
        break
    elif(currency=="AUD"):
        print( AUD_conv(Value,Converter_Currency))
        break
    elif(currency=="YEN"):
        print( YEN_conv(Value,Converter_Currency))
        break
    elif(currency=="LKR"):
        print( LKR_conv(Value,Converter_Currency))
        break
    elif (currency == "EURO"):
        print( EURO_conv(Value, Converter_Currency))
        break
    elif(currency=="Pound"):
        print( Pound_conv(Value,Converter_Currency))
        break
    elif (currency == "Yuan"):
        print(Yuan_conv(Value, Converter_Currency))
        break
    elif(currency=="Riyal"):
        print( Riyal_conv(Value,Converter_Currency))
        break
    elif(currency=="INR"):
        print( INR_conv(Value,Converter_Currency))
        break

    else:
        print("Sorry there is no such a currency".upper())
        continue
