
# Fast-Food-Fast
FAST-FOOD-FAST is an e-commerce platfrom dealing in food delivery.

**Installation and setup**

Clone the repository from github:<br/>

```
git clone https://github.com/mulondo/Fast-Food-Fast.git

```
Create virtualenv and activate it:

Install pip

pip install virtualenv

virtualenv venv

activate the virtualenv<br/>

On windows:

```
mypthon\Scripts\activate 

```
On linux/os:

```
source/venv/acticate

```

Run the application

```
python run.py
```
Test the application by running

```

pytest or python -m unittest

```

**API End points**
 
|Resource URL|Methods   |Description|
|----------------|------------|-------------|
|`/api/v1/orders    ` |`GET,POST `|`Get all orders,Add an order` |
|`/api/v1/orders/<int:order_id>  `|`GET,PUT`|`Get a specific order, Update the status of a specific order `|
