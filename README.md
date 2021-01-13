# Authentication Proyect

#### Ivan Raitman
  
# API Authentication

To authenticate in the application you will have to log in with username and password and use the token that you will receive in response if your credentials are valid
      
    {"Authorization":"Bearer {token}"}

The token is the username encoded with JWT 

## Create auth user

Ask to an application admin to create a new user in the application. To make this, this admin will create you an user with the endpoint:

- **Requires token**

**Note:** password must have minimum eight characters, at least one uppercase letter, one lowercase letter and one number:

- **URL:**
    `/user`

- **Method**
    `POST`

- **Params example** 
  
        {
            userame:test,
            password:Testing123
        }
  
- **Response:**
    **Code:** 201 <br />
        **Content:**
        
        None

## Login
Login to authenticate and receive the token that will later be used for the other endpoints

* **URL:**

      /login/
    
* **Method:**

  `POST`


* **JSON params**
           
        {
            "username":"test"
            "password":"test123"
        }

* **Response example:**
  
    **Code:** 200 <br />
    **Content:** 
    
        {
            "token":"token.jwt.example.response"
        }


