# Identify NYC Subway travel time Destination from two Origin pairs with time restrictions

Data and Inspiration: https://project.wnyc.org/transit-time/

### Dependencies

	pip install ipython
	pip install pandas
	pip install jupyter

### Project Outline

```
download project files
    * https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip
    * https://project.wnyc.org/transit-time/data/transit-time-json-files.zip

unzip project files

create function to read json file 
    return dictionary

create function to select time threshold, value from key value pair
    return selected keys and values

find origin-destinations that share same destination and valid time value
    create empty dictionary
    loop through one o-d set 
        loop through other o-d set
            if match destination 
                generate dicationary item 
    return matches dictionary 


read json
select by time threshold 
find matches 
return matches
```