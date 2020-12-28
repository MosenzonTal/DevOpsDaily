##   **Project Description**
**The purpose of this project is to demonstrate the DevOps daily routine to manage the entire application development lifecycle that is: Development, Testing, Deployment, and monitoring.**

<p align="center">
  <img src="https://imagizer.imageshack.com/img923/7820/gc3mv6.png" width="650" title="hover text">
</p>

**DevOpsDaily is a simple RESTful API application to provide access to a database of users and performing various actions on it.**

For simplicity, the database will be stored as a simple JSON file in the following format:<br>
*users.json*:
```json
{
    "duncan_long": {
        "id": "drekaner",
        "name": "Duncan Long",
        "favorite_color": "Blue"
    },
    "kelsea_head": {
        "id": "wagshark",
        "name": "Kelsea Head",
        "favorite_color": "Ping"
    },
    "phoenix_knox": {
        "id": "jikininer",
        "name": "Phoenix Knox",
        "favorite_color": "Green"
    },
    "adina_norton": {
        "id": "slimewagner",
        "name": "Adina Norton",
        "favorite_color": "Red"
    }
}

```

**The application exposes 3 endpoints:**

<p align="left">
  <img src="https://imagizer.imageshack.com/img924/2343/Bwsa9t.png" width="650" title="hover text">
</p>

*• users.json File is stored in JsonPlaceHolder, which will be used as the db server, receiving HTTP get requests from the application.<br>*
*• The application was built by using the simple Flask web Framework.*

### Containers

-------------------------- TO EDIT -----------------------------

### Unit Tests

In the tests stage we should write a simple unit-test for testing the functionality of the application.
The unit-test creates a **mock JSON** database file (users.json) with predefined data, and validate that the application returns the correct information.

For example, given the following input file:
```json
{
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    }
}
```

**(Test #1)** Accessing the /users URI should return:

```cpp
{
    "test_user": {
        "name": "Test User",
        "favorite_color": "Black"
    }
}

```
**(Test #2)** Accessing the /user/test_user URI should return:

```json
{
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    }
}
```

**(Test #3)** Accessing the /user/test_user123 URI should return **HTTP code 404 as the user does not exist in the database.**

• For this stage, I used **Pytest framework** to test the application functionality. <br>
• For testing with mock JSON database file object, I have used the: unittest.mock library, which allows replacing parts of the system under test with mock objects and making assertions about how they have been used.

###  CI
In the last stage, we have a working app that can also run inside a container, we should setup CI for it, so it won't break in the future.



<p align="center">
  <img src="https://www.lacework.com/wp-content/uploads/2020/08/up-and-running-with-lacework-and-jenkins.png" width="250" title="hover text">
    <img src="https://cdn.vox-cdn.com/thumbor/1yDRMoogTR55jiv_b-PVZLXWv8A=/0x0:792x613/1220x813/filters:focal(300x237:426x363):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/59850273/Docker_logo_011.0.png" width="250" title="hover text">
  <img src="https://www.almtoolbox.com/blog_he/wp-content/uploads/2017/09/Git-Logo-2Color-1.png" width="250" title="hover text">
    <img src="  https://www.macworld.co.uk/cmsdata/features/3635912/learn_python_mac_thumb800.jpg" width="250" title="hover text">
</p>







