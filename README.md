# Authentication Proyect

#### Ivan Raitman

Aplicación realizada para IDM Challenge 2020

- Application URL: `ec2-18-230-151-229.sa-east-1.compute.amazonaws.com:8081`
  
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


# Run this project

If you want to run this code locally, you should run the following commands:

* Being inside the project folder, build the container:

      docker build -t meli_app .

* After that, you are able to run the code

      docker run -it --publish 8081:8081  meli_app
 
It is important to have the local_settings file to run this code correctly.

