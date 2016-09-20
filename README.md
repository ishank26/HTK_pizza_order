#HTK Food Order
A speech recognition application for food ordering via dialog based interface.

###Grammar used
* **Pizza**: CHEESE | CAPSICUM | TOMATO
* **Side orders**: CUPCAKE | PASTA
* **Size**: REGULAR | LARGE
* **Number**: ONE | TWO | THREE
* **Yes**: YES | YEAH
* **No**: NO | THATS ALL | NO THATS ALL

#####Run file: order.py
###Application flow
```
++++ Welcome and pizza order audio stating choices of pizzas and sizes
  |---- Please speak pizza order 
  |   |--- {Number-Size-Pizza} # any order combination allowed
  |   |--- IF voice recognised >> Proceed to side order
  |      |--- IF NOT voice recognised >> Please speak pizza order
  |   
++++ Play audio stating side order choices
  |---- Please speak side order 
  |   |--- {Number-Size orders} # any order combination allowed
  |      |--- IF voice recognised >> Proceed to confirmation
  |      |--- IF NOT voice recognised >> Please speak side order
  |
+++++ Confirm order
  |--- Print order
  |--- Yes 
  |--- No >> Please speak pizza order
```

###Requirements
* Julius
* Python
* HTK
