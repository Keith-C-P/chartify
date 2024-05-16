
# Chartify

A Python Library that provides tools to print Charts in the terminal

# Usage/Examples

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
<details>
<summary> PieChart </summary>

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
</details>

# Features

<details>

<summary> Keyword Arguments </summary>

### data: `dict[str, int]`
Enter the data of the piechart

- Default value: `None`
- Allowed Options: `dict[str, int]`
- Optional: `NO`

### radius: `int`
Change the radius of the chart

- Default value: `15`
- Allowed Options: `int`
- Optional: `YES`

### keys: `tuple[str]`
List of keys that the chart will use instead of default
(if the chart needs more keys than default provide your own keys)

- Default value: ```('#', '*', '!', '&', ';', '%', ':', '@', '.', '$', ',', '?', '>', '<', '+', '-', '=', '^', '~', '`', '|', '\', '/')```
- Allowed Options: `tuple[str]`
- Optional: `YES`

### gamerMode: `bool`
Print the chart in multicolor to make it more readeable 

- Default value: `False`
- Allowed Options: `True, False`
- Optional: `YES`

### ascending: `bool`, `None`
Order your data by value 
1. Ascending -> `True`
2. Descending -> `False`
3. Input order -> `None`

- Default value: `None`
- Allowed Options: `True`, `False`, `None`
- Optional: `YES`
<\details>