#### Member
```
Jedsadaporn Puttakosai 61102010139
Pattamas Wiratchanee 61102010156
Suwikan Wongwean 61102010166
```
#### install lib
```
pip install -r requirements.txt
```
#### start project
```
python app.py
```
### Feature
  - get food by name
  - get tdee
  - create food
  - edit food
  - delete food
### Path 
  #### GET
  ```
  localhost:5000/foods [ get food by param optional name ]
  ```
  #### POST
  ```
  localhost:5000/foods [ create food ]
  ```
  #### PUT
  ```
  localhost:5000/foods [ edit food ]
  ```
  #### DELETE
  ```
  localhost:5000/foods/delete/{Food} [ DELETE food ]
  ```
  #### GET TDEE,BMR
  ```
  localhost:5000/tdee [ GET BMR param :  age , weight , height, gender]
  localhost:5000/tdee [ GET TDEE param :  age , weight , height, gender, activity]
  ```
