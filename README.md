

## enviroment
- python -m venv venv
- venv\scripts\activate  (windows)
- if (linux)  . venv\bin\activate

## Install:
- pip install django
- pip install djangorestframework

## Set up project
- django-admin startproject vendor .
- django-admin startapp vendorapp

## migration
- python manage.py makemigrations
- python manage.py migrate

## Superuser
- python manage.py createsuperuser


## here now token is excluded for easy checking

## Running the server
- python manage.py runserver

## migrate models


## vendor  model:

- http://127.0.0.1:8000/api/vendors/  (list) and can add there beacause it is restframework
- http://127.0.0.1:8000/api/vendors/{vendor_id}  (get by id) and same for put method  retrive and put and for delete method


## Retrieve a vendor's performance:

-  http://127.0.0.1:8000/api/vendors/1/performance/
- On-Time Delivery Rate: The average percentage of purchase orders delivered before the delivery date compared to the total number of purchase orders completed.
- Quality Rating Average: The average rating given to the vendor across all completed purchase orders.
- Average Response Time: The average time taken by the vendor to acknowledge a purchase order, calculated as the difference between the issue date and acknowledgment date for each purchase order, then averaged across all purchase orders.
- Fulfillment Rate: The percentage of successfully fulfilled purchase orders (completed without issues) compared to the total number of purchase orders issued to the vendor.

## Update recalculation of  average_response_time:
- http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/
- here this endpoint is used to acknowledge the purchase_order with given po_id and trigger the recalculation of average_reponse_time.

