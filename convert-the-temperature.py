class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        Fahrenheit = ((9/5) * celsius) + 32
        Kelvin = celsius + 273.15
        return [Kelvin, Fahrenheit]
        
