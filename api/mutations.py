### Resolver
# mutations.py
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import MaiorRomano

@convert_kwargs_to_snake_case
def search(obj, info, text):
    def romToInt(num12):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        num12 = num12.upper()
        while i < len(num12):
            if i+1<len(num12) and num12[i:i+2] in roman:
                num+=roman[num12[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[num12[i]]
                i+=1
        return num

#Check if input is in the right format
    if text.upper().find('A') != 0 or 'B' not in text.upper():
    	payload = {
    	    "aviso": ["Please inform 'A' as indication of first number and 'B' for second. Example: AXXBLX"]
    	}
    else:
        #In case of correctly informed, we start finding the numerals from string by finding their position
        posA = text.upper().find('A')
        posB = text.upper().find('B')
        num1 = text[posA+1:posB]
        num2 = text[posB+1:]
        value = max(romToInt(num1), romToInt(num2))
        if value == romToInt(num1): number = num1.upper()
        else: number = num2.upper()
        payload = {
            "number": number,
            "value": value
        }
    return payload
        
        
       