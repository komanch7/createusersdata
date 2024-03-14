[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=CREATE+USERS+DATA)](https://github.com/komanch7/createusersdata)
---

### 🔥 My Stats:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/createusersdata/pulse)

- Information is presented in several languages:
    
    | [German](https://github.com/komanch7/createusersdata/blob/main/docs/README_DE.md) |
    [Russian](https://github.com/komanch7/createusersdata/blob/main/docs/README_RU.md) |
    [Ukrainian](https://github.com/komanch7/createusersdata/blob/main/docs/README_UA.md) |


# createusersdata
User data. Selecting a name from a list of names, selecting a last name from a list of surnames, calculates the year based on the entered age

## Roadmap
- create_first_name - the function takes three parameters. 1. names - an array of names. 2. gender - two parameters (male, female). 3. nationality - string value in __iso2__ format

- create_last_name - 1. names - an array of names. 2. nationality - string value in __iso2__ format

- get_year_ago - the function takes one parameter (age). Month and day are given randomly.

---
## Tech Stack

**Server:** Python 3.9^

---

# Clone this repository

```sh
$ gh repo clone komanch7/createusersdata cud-pro

$ cd cud-cli

  or

$ git clone https://github.com/komanch7/createusersdata cud-pro

$ cd cud-pro
```



### JSON for data
```json
{"male", "female"}
```
```json
{
  "male": {
    "en": [
      "Name first",
      "..."
    ]
  },
  "female": {
    "en": [
      "Name first",
      "..."
    ]
  }
}
```

### Codespaces
_Python Code..._
```python
# all imports
import create_first_name
import create_last_name
import get_year_ago
```
## Function number 1
```python
# get list

first_name = "first_names.json"

# takes three parameters
#  1. list with named
#  2. string with gender
#  3. string with Name nationality (optional)

res_first_name = first_name_selection(fisrt_name, gender='male', nationality='us')
print(res_first_name)
```
- program response
```python
>> William
```
### Function number 2
```python
# get list

last_name = "last_names.json"

# takes three parameters
#  1. list with named
#  2. string with Name nationality (optional), default parameter = 'en'

res_last_name = last_name_selection(last_name, nationality='en')

print(res_last_name)
```
- program response
```python
>> Berger
```
### Function number 3
```python
# takes one parameter
#  1. integer with age

age = 18
year_ago = get_year_ago(age)
print(year_ago.strftime('%Y'))
```
- program response
```python
>> 2005
```

## 🚀 About Me
- I'm a beginner in Python development. Thank you for your understanding and support.
---

## License
[MIT](https://github.com/komanch7/createusersdata/LICENSE)
