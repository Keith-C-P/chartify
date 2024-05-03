import math

class PieChart:
    def __init__(self, *, radius: int = 15, data: dict[str, float] = 0, order: int = 1, keys: tuple[str] = ('#', '*', '!', '&', ';', '%', ':', '@', '.', '$', ',', '?', '>', '<', '+', '-', '=', '^', '~', '`', '|', '\\', '/') ) -> None: # (dunder method)
        '''
        radius: int - the radius of the circle
        percentages: tuple - the percentages of the catagories
        catagories: tuple - the catagories of the pie chart (has default value of an empty tuple)
        keys: tuple - the keys for the catagories (has default keys)
        '''
        try:
            assert isinstance(data, dict), "Values must be a dictionary"
            assert len(data) > 0, "Values must have at least one value"
            assert radius > 0, "Radius must be greater than 0"

        except AssertionError as e:
            print(e)
            exit()
        
        else:
            self.keys: tuple[str] = keys
            self.radius: int = radius
            self.raw_data: dict[str, float] = data
            
            dum: list[float] = [data[i]/sum(data.values()) for i in data] # convert to percentages
            dum = [sum(dum[:i+1]) for i in range(len(dum))] # cumulative sum
            
            self.percentages: dict[str, float] = {list(data.keys())[i]: dum[i] for i in range(len(dum))}


    def __calc_percentage(self, x: int, y: int) -> float: #  ('__' means private method)
        '''
        Calculate percentage that the pixel corresponds to.
        x: int - x coordinate
        y: int - y coordinate
        '''
        if x == 0 and y < 0: # 270 degrees
            return 0.5

        m = y/x if x != 0 else math.inf
        p = .5 * (.5 - (math.atan(m)/math.pi))
        if x < 0:
            p = 0.5 + p
        return p

    def __color_pixel(self, x: int, y: int) -> None: # ('__' means private method)
        '''
        Color the pixel based on the percentage it corresponds to.
        x: int - x coordinate
        y: int - y coordinate
        '''
        values = [0] + list(self.percentages.values())
        p = self.__calc_percentage(x, y)
        for i in range(1, len(values)):
            if p >= values[i - 1] and p < values[i]:
                return (f"{self.keys[i-1] * 2}")
        return ('  ')
    
    def __str__(self) -> str: # Create the pie chart (dunder method)
        '''
        Create the pie chart.
        '''
        chart = ""
        for y in range(-self.radius, self.radius):
            for x in range(-self.radius, self.radius):
                if x ** 2 + y ** 2 <= self.radius ** 2:
                    chart += self.__color_pixel(x, y)
                else:
                    chart += "  "
            chart += "\n"

        chart += '\n\n'
        chart += "Legend:\n"
        total = sum(self.raw_data.values())
        print(total)

        for k, v in self.raw_data.items():
            chart += f"{k} : {v} || {v/total:.0f}%\n"


        # something : <value> || <percent>


        return chart
    
    def __repr__(self) -> str: # Return the string representation of the object (dunder method)
        return (f"Radius: {self.radius}, Percentages: {self.raw_percentages}, Catagories: {self.catagories}")
    
class BarChart:
    def __init__():
        pass

class LineGraph:
    def __init__():
        pass


if __name__ == "__main__":
    d = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
    a = PieChart( data = d )
    print(a)

# TODO
# - add random to graph keys
# - add new graphs
# - add key input
# - change to raw value input
# - change to support dictionary or list input by default