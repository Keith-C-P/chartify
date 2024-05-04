import math

class PieChart:
    def __init__(self, *, radius: int = 15,
                 data: dict[str, float] = 0,
                 reverse: bool = None,
                 keys: tuple[str] = ('#', '*', '!', '&', ';', '%', ':', '@', '.', 
                                     '$', ',', '?', '>', '<', '+', '-', '=', '^', 
                                     '~', '`', '|', '\\', '/'), 
                 gamerMode: bool = False) -> None:
        '''
        Create a pie chart.
        radius: int
         radius of the pie chart
        data: dict
         data to be represented in the pie chart
        order: int 
         order of the pie chart (-1 : descending, 0 : no order, 1 : ascending)
        keys: tuple
          keys to represent the data
        '''
        try:
            assert isinstance(data, dict), "Data must be a dictionary"
            assert isinstance(reverse, bool) or reverse == None, "reverse must be a boolean or None"
            assert isinstance(keys, tuple), "Keys must be a tuple"
            assert isinstance(radius, int), "Radius must be an integer"
            assert isinstance(gamerMode, bool), "gamerMode must be a boolean"
            assert all(isinstance(key, str) for key in data.keys()), "Keys must be strings"
            assert all(isinstance(key, (int,float)) for key in data.values()), "Values must be integers or floats"
            assert len(data) > 0, "Values must have at least one value"
            assert radius > 0, "Radius must be greater than 0"
            assert len(keys) >= len(data), "Not enough keys for the data provided"

        except AssertionError as e:
            print(e)
            exit()
        
        else:
            self.keys: tuple[str] = keys
            self.radius: int = radius
            self.raw_data: dict[str, float] = data
            self.gamerMode: bool = gamerMode
            
            if reverse == False:
                self.raw_data = {k: v for k, v in sorted(self.raw_data.items(), key=lambda item: item[1], reverse=False)}
            elif reverse == True:
                self.raw_data = {k: v for k, v in sorted(self.raw_data.items(), key=lambda item: item[1], reverse=True)}
                
            dum: list[float] = [self.raw_data[i]/sum(self.raw_data.values()) for i in data] # convert to percentages
            dum = [sum(dum[:i+1]) for i in range(len(dum))] # cumulative sum
            
            self.color: list[str] = []
            if gamerMode:
                self.color = [self.__huetoRGB(i/len(dum)) for i in range(len(dum))]
                self.color = [self.__huetoRGB(0)] + self.color



            self.percentages: dict[str, float] = {list(data.keys())[i]: dum[i] for i in range(len(dum))}


    def __calc_percentage(self, x: int, y: int) -> float:
        '''
        Calculate percentage that the pixel corresponds to.
        x: int
         x coordinate
        y: int
         y coordinate
        '''
        if x == 0 and y < 0: # 270 degrees
            return 0.5

        m = y/x if x != 0 else math.inf
        p = .5 * (.5 - (math.atan(m)/math.pi))
        if x < 0:
            p = 0.5 + p
        return p
    
    def __huetoRGB(self, p: float) -> str:
        '''
        Convert hue to RGB.
        p: float
         percentage
        '''
        q = 1 - p
        r, g, b = 0, 0, 0
        if p < 1/6:
            r = 1
            g = p * 6
        elif p < 1/3:
            r = q * 6
            g = 1
        elif p < 1/2:
            g = 1
            b = (p - 1/3) * 6
        elif p < 2/3:
            g = q * 6
            b = 1
        elif p < 5/6:
            r = (p - 2/3) * 6
            b = 1
        else:
            r = 1
            b = q * 6

        return (f"\u001b[38;2;{int(r * 255)};{int(g * 255)};{int(b * 255)}m")

    def __color_pixel(self, x: int, y: int) -> None: 
        '''
        Color the pixel based on the percentage it corresponds to.
        x: int 
         x coordinate
        y: int 
         y coordinate
        '''
        values = [0] + list(self.percentages.values())
        p = self.__calc_percentage(x, y)
        for i in range(1, len(values)):
            if p >= values[i - 1] and p < values[i]:
                return f"{self.color[i - 1]}{self.keys[i - 1] * 2}\u001b[0m" if self.gamerMode else f"{self.keys[i - 1] * 2}"
        return ('  ')
    
    def __legend(self) -> str:
        '''
        Create the legend for the pie chart.
        '''
        legend = "Legend:\n" if not self.gamerMode else ''.join([f"{self.__huetoRGB( j / len( list( 'RGB Gamer Legend:' ) ) )}{i}\u001b[0m" for j,i in enumerate(list('RGB Gamer Legend:'))]) + "\n" # for rgb gamerMode legend
        lKey = max([len(key) for key in self.raw_data])

        i = 0
        for k, v in self.raw_data.items():
            legend += f"[{self.keys[i]}] {k} {' ' * (lKey - len(k))}- {v}\n" if not self.gamerMode else f"{self.color[i]}[{self.keys[i]}] {k} {' ' * (lKey - len(k))}- {v}\u001b[0m\n"
            i += 1
        return legend

    
    def __str__(self) -> str:
        '''
        Create the pie chart with legend.
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
        chart += self.__legend()

        return chart
    
    def __repr__(self) -> str: # Return the string representation of the object
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
    # print("\u001b[38;2;{r};{g};{b}m Hello, world! \u001b[0m")
    print(a)

# TODO
# - add random to graph keys
# - add new graphs
# - add order customization
# - add color customization
