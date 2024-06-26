[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=СОЗДАНИЕ+ПОЛЬЗОВАТЕЛЬСКИХ+ДАННЫХ)](https://github.com/komanch7/createusersdata)
---

### 🔥 Моя статистика:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/createusersdata/pulse)

- Информация представлена на нескольких языках:
    
    | [Английский](https://github.com/komanch7/createusersdata/blob/main/README.md) |
    [Украинский](https://github.com/komanch7/createusersdata/blob/main/docs/README_UA.md) |
    [Немецкий](https://github.com/komanch7/createusersdata/blob/main/docs/README_DE.md) |

# createusersdata
Данные пользователя. Выбор имени из списка имен, выбор фамилии из списка фамилий, расчет года на основе введенного возраста.

## Дорожная карта
- create_first_name - функция принимает три параметра. 1. имена - массив имен. 2. пол – два параметра (мужской, женский). 3. национальность — строковое значение в формате __iso2__.

- create_last_name - 1.names — массив имён. 2. nationality – строковое значение в формате __iso2__.

- get_year_ago - функция принимает один параметр (age). Месяц и день выдаются случайно.

---
## Технический стек

**Server:** Python 3.9^

---

## Клонировать этот репозиторий

```sh
$ gh repo clone komanch7/createusersdata gp-pro

$ cd gh-cli

  or

$ git clone https://github.com/komanch7/createusersdata gp-pro

$ cd gp-pro
```



### JSON для данных
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

fisrt_name = "first_names.json"

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

## 🚀 Обо мне
- Я новичок в разработке Python. Благодарю вас за понимание и поддержку.
---

## Лицензия
[MIT](https://github.com/komanch7/createusersdata/LICENSE)
