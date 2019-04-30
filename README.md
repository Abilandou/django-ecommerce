BEFORE YOU CLONE TO RUN AND TEST PROJECT PLEASE DO THE FOLLOWING.
	- Install a virtual environment. Follow below link to create the virtual environment
		https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
	- Activate your virtual environment. 
	- In The activated virtual environment, install django 1.11.4
	- After installing the django 1.11.4
	- Clone this repo to that directory.
	- cd to the cloned directory.
	- run command below to start the python-django server
		python manage.py runserver
	- Open any browser and go to the following url.
		http://localhost:8000 
	- If the above url does not work, check your terminal for the url provided by the server for you to open.
	
	HAPPY CODING
	

########## 	SOME APPS AND A LITTLE EXPLANATION OF EACH ##########



### CHECKOUT PROCESS######

1. Cart -> Checkout view
	?
	-Login/Register or Enter an Email (as Guest)
	-Shipping Address
	-Billing Info
		- Billing Address
		- Credit Card / Payment

2. Billing App/Component
	- Billing Profile
		- User or Email (Guest Email)
		- Generate payment processor token (Stripe or Braintree)


3. Orders / Invoices Component
	- Connecting the Billing Profile
	- Shipping / Billing Address
	- Cart
	- Status -- Shipped? Cancelled?
	
	
