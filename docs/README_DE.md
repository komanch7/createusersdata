[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=BENUTZER+DATEN+ERSTELLEN)](https://github.com/komanch7/createusersdata)
---

### 🔥 Meine Statistiken :
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/createusersdata/pulse)

- Die Informationen werden in mehreren Sprachen präsentiert:
    
    | [Englisch](https://github.com/komanch7/createusersdata/blob/main/README.md) |
    [Russisch](https://github.com/komanch7/createusersdata/blob/main/docs/README_RU.md) |
    [Ukrainisch](https://github.com/komanch7/createusersdata/blob/main/docs/README_UA.md) |

# createusersdata
Benutzerdaten. Wenn Sie einen Namen aus einer Namensliste auswählen oder einen Nachnamen aus einer Liste mit Nachnamen auswählen, wird das Jahr basierend auf dem eingegebenen Alter berechnet.

## Roadmap
- create_first_name – die Funktion benötigt drei Parameter. 1. Namen – ein Array von Namen. 2. Geschlecht – zwei Parameter (männlich, weiblich). 3. Nationalität – Zeichenfolgenwert im __iso2__ -Format

- create_last_name - 1. Namen – ein Array von Namen. 2. Nationalität – Zeichenfolgenwert im __iso2__-Format

- get_year_ago - Die Funktion benötigt einen Parameter (Alter). Monat und Tag werden zufällig vergeben.

---
## Tech-Stack

**Server:** Python 3.9^

---

## Klonen Sie dieses Repository

```sh
$ gh repo clone komanch7/createusersdata gp-pro

$ cd gh-cli

  oder

$ git clone https://github.com/komanch7/createusersdata gp-pro

$ cd gp-pro
```



### JSON für Daten
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

## 🚀 Über mich
- Ich bin ein Anfänger in der Python-Entwicklung. Vielen Dank für Ihr Verständnis und Ihre Unterstützung.
---

## Lizenz
[MIT](https://github.com/komanch7/createusersdata/LICENSE)