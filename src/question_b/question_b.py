import question_b
from src.question_b.question_b import get_fahrenheit

def main ():
    print("Celsius\t\tFahrenheit")
    print("-------------------------")

for celsius in range(0, 21):  
    fahrenheit = get_fahrenheit(celsius)
    print(f"{celsius}\t\t{fahrenheit:.1f}")  
    #write functions here, don't add input('') statements here!
