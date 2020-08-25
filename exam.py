
from fraction import Fraction

one = [ "", "one ", "two ", "three ", "four ", 
        "five ", "six ", "seven ", "eight ", 
        "nine ", "ten ", "eleven ", "twelve ", 
        "thirteen ", "fourteen ", "fifteen ", 
        "sixteen ", "seventeen ", "eighteen ", 
        "nineteen "]; 
  
ten = [ "", "", "twenty ", "thirty ", "forty ", 
        "fifty ", "sixty ", "seventy ", "eighty ", 
        "ninety "]; 
  
# n is 1- or 2-digit number 
def numToWords(n, s): 
  
    str = ""; 
      
    # if n is more than 19, divide it 
    if (n > 19): 
        str += ten[n // 10] + one[n % 10]; 
    else: 
        str += one[n]; 
  
    # if n is non-zero 
    if (n): 
        str += s; 
  
    return str; 
  
# Function to print a given number in words 
def convertToWords(n, se): 
  
    # stores word representation of given  
    # number n 
    out = ""; 
  
    # handles digits at ten millions and  
    # hundred millions places (if any) 
    out += numToWords((n // 10000000),  
                            "crore ");

    if(n > 10000000 and n % 10000000):
        out += ",";
  
    # handles digits at hundred thousands  
    # and one millions places (if any) 
    out += numToWords(((n // 100000) % 100), 
                                   "lakh ");
    
    if(n > 100000 and n % 100000):
        out += ",";
  
  
    # handles digits at thousands and tens  
    # thousands places (if any) 
    out += numToWords(((n // 1000) % 100),  
                             "thousand ");
    
    if(n > 1000 and n % 1000):
        out += ",";
  
    out += numToWords(((n // 100) % 10),  
                            "hundred "); 
  
    if (n > 100 and n % 100):
        out += ", ";

    out += numToWords((n % 100), ""); 

    if(str(se)==""):
        return out
    return out+"and "+str(se); 
  
# Driver code 
  
num = input("enter yout currency:- ")

txt = str(num)
nw = txt.split(".")

n = int(nw[0])

x = ""
if(len(nw)>1):
    if(len(nw[1])!=""):
        se = 10**len(nw[1])
        s = nw[1]
        x = Fraction(s, se)
        

# convert given number in words
print(convertToWords(n, x))


