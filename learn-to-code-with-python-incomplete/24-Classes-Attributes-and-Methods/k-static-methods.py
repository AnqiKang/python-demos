# static methods are used for utility operations that affect neither the class nor its objects
class WeatherForecast():
    def __init__(self, temps):
        self.temps = temps

    @staticmethod
    def convert(fahr):
        calculation = (5/9) * (fahr - 32)
        return round(calculation, 2)

    def in_celsius(self):
        return [self.convert(temp) for temp in self.temps]


wf = WeatherForecast([100, 90, 80, 70, 60])
print(wf.in_celsius())

print(WeatherForecast.convert(100))
