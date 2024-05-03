import math

class PieChart:
    def __init__(self, *, radius: int, percentages: tuple, catagories: tuple = (), keys: tuple[str] = ('#', '*', '!', '&', ';', '%', ':', '@', '.', '$', ',', '?', '>', '<', '+', '-', '=', '^', '~', '`', '|', '\\', '/') ) -> None: # Initialize the PieChart object (dunder method) (catagories is optional ie a default value of an empty list)
        try:
            assert len(catagories) <= len(percentages)
            assert sum(percentages) <= 1
            assert len(percentages) > 0
            assert radius > 0

        except AssertionError:
            if len(catagories) > len(percentages):
                print("The number of percentages must be less than or equal to the number of catagories")
            if sum(percentages) > 1:
                print("The sum of the percentages must be less than or equal to 1")
            if len(percentages) == 0:
                print("There must be at least one percentage")
            if radius <= 0:
                print("The radius must be greater than 0")
            exit()
        
        else:
            self.keys: tuple[str] = keys
            self.radius: int = radius
            self.catagories: list[str] = list(catagories) # Save the catagories list
            self.raw_percentages: list[float] = list(percentages) # Save the raw percentages for the catagories list
            self.percentages = [0]

            if sum(self.raw_percentages) < 1: # Add a placeholder for the missing percentage
                self.raw_percentages.append(1 - sum(self.raw_percentages)) 

            for i in range(len(percentages)): # Calculate the percentages
                self.percentages.append(round(self.percentages[i] + percentages[i], ndigits=2))

            if (self.percentages[-1] != 1): # Check if the percentages add up to 1 (just in case)
                self.percentages.append(1)

            if len(self.catagories) < len(self.percentages) - 1: # Placeholder for missing catagories
                for i in range(len(self.catagories), len(self.percentages) - 2):
                    self.catagories.append("<<Placeholder>>")
                # print(self.percentages)

    def __calc_percentage(self, x: int, y: int) -> float: # Calculate percentage that the pixel corresponds to ('__' means private method)
        if x == 0 and y < 0: # 270 degrees
            return 0.5

        m = y/x if x != 0 else math.inf
        p = .5 * (.5 - (math.atan(m)/math.pi))
        if x < 0:
            p = 0.5 + p
        return p

    def __color_pixel(self, x: int, y: int, val: list) -> None: # Assign a color to the pixel ('__' means private method)
        p = self.__calc_percentage(x, y)
        for i in range(1,len(val)):
            if p >= val[i - 1] and p < val[i]:
                return (f"{self.keys[i-1] * 2}")
        return ('  ')
    
    def __str__(self) -> str: # Create the pie chart (dunder method)
        chart = ""
        for x in range(-self.radius, self.radius + 1): # execute for every pixel in the circle
            for y in range(-self.radius, self.radius + 1):
                if x ** 2 + y ** 2 <= self.radius ** 2: # circle equation
                    chart += self.__color_pixel(x, y, self.percentages)
                else:
                    chart += '  '
            chart += '\n'
        
        if self.catagories:
            chart += '\n\n'
            for i in range(len(self.catagories)):
                chart += f"[{self.keys[i]}] {self.catagories[i]} : {self.raw_percentages[i] * 100 :.0f}%\n"
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
    a = PieChart( radius = 20, percentages = [.2,.2,.2,.2,.2] )
    print(a)

# TODO
# - add random to graph keys
# - add new graphs
# - add key input
# - change to raw value input
# - change to support dictionary or list input by default