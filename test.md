# http://localhost:8000/models/orm_createcustomersdata/
# http://localhost:8000/models/orm_updatecustomernamebyid/1/eee
# http://localhost:8000/models/orm_deleterecordbyid/1
# http://localhost:8000/models/orm_deleteallrecords/
# http://localhost:8000/models/orm_getallrecords/
# http://localhost:8000/models/orm_getrecordbyid/1
# http://127.0.0.1:8000/webservices_db/get_customer_details
# http://127.0.0.1:8000/webservices_db/insert_customer_details
```
# With postman apply the following
1. Method = POST 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "customer_id": 4
    ,"customer_name":"D"
    ,"application_date":"2022-01-02"
    ,"customer_creditscore":333
    ,"customer_req_loanamount":1234.45
}
```
# http://127.0.0.1:8000/webservices_db/update_customer_details/4
```
# With postman apply the following
1. Method = PUT 
2. Content = Body>Raw
3. type = JSON

content
--------
{
     "customer_id": 4
    ,"customer_name":"HHHHHHH"
    ,"application_date":"2021-08-20"
}

```


# http://127.0.0.1:8000/webservices_db/delete_customer_details/4
```
# With postman apply the following
1. Method = DELETE 
No Content To Pass
```
