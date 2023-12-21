[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=СТВОРЕННЯ+КОРИСТУВАЛЬНИХ+ДАНИХ)](https://github.com/komanch7/createusersdata)
---

### 🔥 Моя статистика:
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/createusersdata/pulse)
    
- Інформація представлена ​​кількома мовами:
    
    | [Англійська](https://github.com/komanch7/createusersdata/blob/main/README.md) |
    [Німецька](https://github.com/komanch7/createusersdata/blob/main/docs/README_DE.md) |
    [Російська](https://github.com/komanch7/createusersdata/blob/main/docs/README_RU.md) |

# createusersdata
Данные пользователя. Выбор имени из списка имен, выбор фамилии из списка фамилий, расчет года на основе введенного возраста.

## Дорожная карта
- create_first_name - функция принимает три параметра. 1. имена - массив имен. 2. пол – два параметра (мужской, женский). 3. национальность — строковое значение в формате __iso2__.

- create_last_name - 1.names - масив імен. 2. nationality – рядкове значення форматі __iso2__.

- get_year_ago - функція приймає один параметр (age)

---
## Технічний стек

**Server:** Python 3.9^

---

## Клонувати цей репозиторій

```sh
$ gh repo clone komanch7/createusersdata gp-pro

$ cd gh-cli

  or

$ git clone https://github.com/komanch7/createusersdata gp-pro

$ cd gp-pro
```



### JSON для данних
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
# 
res_first_name = first_name_selection(fisrt_name, gender='male', nationality='us')
print(res_first_name)
```
- program response
```python
>> William
```
### Function number 2
```python
res_last_name = last_name_selection(last_name, nationality='en')

print(res_last_name)
```
- program response
```python
>> Berger
```
### Function number 3
```python
age = 18
year_ago = get_year_ago(age)
print(year_ago.strftime('%Y-%m-%d'))
```
- program response
```python
>> 2005-11-14
```

## 🚀 Про мене
- Я новачок у розробці Python. Дякую вам за розуміння та підтримку.
---

## Ліцензія
[MIT](https://github.com/komanch7/createusersdata/LICENSE)
