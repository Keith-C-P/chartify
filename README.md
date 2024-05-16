
# Chartify

A Python Library that provides tools to print Charts in the terminal

## Usage/Examples

1 - Clone the repo into your working directory

2 - import it with `from chartify import PieChart`

### Example

```python
from chartify import PieChart

data = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
pie = PieChart(data = data)
print(pie)

```

This should give an output like this

```
                              &&                              
                    &&&&&&&&&&&&&&&&&&&&&&                    
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                
            &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!            
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!          
        &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!        
      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!      
      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!      
    ;;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!    
    ;;;;;;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!    
  ;;;;;;;;;;;;&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!  
  ;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!!!  
  ;;;;;;;;;;;;;;;;;;&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!!!  
  ;;;;;;;;;;;;;;;;;;;;;;&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!!!!!  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;&&&&!!!!!!!!!!!!!!!!!!**********  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;##******************************
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;########**********************  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;##############****************  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;####################**********  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;##########################****  
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;##############################  
    ;;;;;;;;;;;;;;;;;;;;;;;;;;############################    
    ;;;;;;;;;;;;;;;;;;;;;;;;;;############################    
      ;;;;;;;;;;;;;;;;;;;;;;;;##########################      
      ;;;;;;;;;;;;;;;;;;;;;;;;##########################      
        ;;;;;;;;;;;;;;;;;;;;;;########################        
          ;;;;;;;;;;;;;;;;;;;;######################          
            ;;;;;;;;;;;;;;;;;;####################            
                ;;;;;;;;;;;;;;################                
                    ;;;;;;;;;;############                    
                              ##                              


RGB Gamer Legend:
[#] a - 3
[*] b - 1
[!] c - 2
[&] d - 4
[;] e - 5

```

## Features

data: dict[] - enter the data of the piechart 

radius: int (optional) - change the radius of the chart (default = 15)

keys: tuple() =  (optional) - list of keys that the chart will use instead of default (defalt = <a tuple of ascii charecters> )

(if the chart needs more keys than default provide your own keys)

gamerMode: bool (optional) - print the chart in multicolor to make it more readeable 

ascending: bool/None (optional) - order your dictionary data in ascending (True) or descending (False) (default = None (no ordering)) 