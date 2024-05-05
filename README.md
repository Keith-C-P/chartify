
# Chartify

A Python Library that provides tools to print Charts in the terminal
 


## Usage/Examples

1 - Clone the repo into your working directory

2 - import it with `from chartify import PieChart`

### Example

```python
from chartify import PieChart

data = {'': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
pie = PieChart(data = data)
print(pie)

```

This should give an output like this

```
                              !!                            
                    !!!!!!!!!!!!!!!!!!!!!!                  
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              
            &&!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**          
          &&&&&&!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!******        
        &&&&&&&&!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!********      
      &&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!!!!!************    
      &&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!**************    
    &&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!!!!!****************  
    &&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!!!!!******************  
  &&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!!!!!**********************
  &&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!************************
  &&&&&&&&&&&&&&&&&&&&&&&&!!!!!!!!!!************************
  &&&&&&&&&&&&&&&&&&&&&&&&&&!!!!!!**************************
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&!!****************************
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##****************************
  &&&&&&&&&&&&&&&&&&&&&&;;;;;;########**********************
  &&&&&&&&&&&&&&&&;;;;;;;;;;;;##############****************
  &&&&&&&&&&;;;;;;;;;;;;;;;;;;####################**********
  &&&&;;;;;;;;;;;;;;;;;;;;;;;;##########################****
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


Legend:
[#] a - 1
[*] b - 1
[!] c - 1
[&] d - 1
[;] e - 1
```
