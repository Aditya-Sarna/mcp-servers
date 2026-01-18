
ACCOUNTS = {
     1001: {
        "user_id":1,
        "type": "savings",
        "balance": 125000,
        "currency": "INR",
        "status": "active"
    },
    1002: {
        "user_id": 2,
        "type": "credit",
        "balance": -32000,
        "credit_limit": 100000,
        "status": "active"
    },
    1003:{
        "user_id":3,
        "type":"savings",
        "balance":75000,
        "currency":"INR",
        "status":"inactive"
    },
    1004:{
        "user_id":4,
        "type":"credit",
        "balance":-15000,
        "credit_limit":50000,
        "status":"active"
    },
    1005:{
        "user_id":5,
        "type":"savings",
        "balance":200000,
        "currency":"INR",
        "status":"active"
    }   ,
    1006:{
        "user_id":6,
        "type":"credit",
        "balance":-45000,
        "credit_limit":120000,
        "status":"inactive"
    }
    


}
print(ACCOUNTS[1003]["balance"])