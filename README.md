##   **Project Description**
**The purpose of this project is to demonstrate the DevOps daily routine to manage the entire application development lifecycle, that is: Development, Testing, Deployment, and monitoring.**

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
for setting up the CI I have used the following guidelines:

1.	 Installed and Set up the project in **Jenkins** +**configured** required **Jenkins** Plugins to run **Python Unit Test**.
2.	Clone the application source code from a GitHub repository.
3.	**Verify the result** - run the unit-test and made sure all the tests pass.
4.	BONUS: Automatically execute the CI on every new pull request.

For Seting up the project in Jenkins I used "Build a free-style software project" and added a build step "Execute Windows batch command", with the following configuration:

```bash
echo '#### create Python3 Virtual Environment ####'
source scl_source enable rh-python36

VIRTUAL_ENV_NAME='virtual-environment'
py -m venv $VIRTUAL_ENV_NAME

echo '#### Avtivate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install requirments ####'
py -m pip install -r requirements.txt
py -m pip install --upgrade pip

echo '#### Run Tests ####'
py -m pytest --junitxml=test.xml

```
**Configuring GitHub
<p align="center">
      <img src="https://imagizer.imageshack.com/img922/1069/IEp5JG.png" width="500" title="hover text">
</p>

**running all unit-tests from *test_application.py* and getting Success.
<p align="center">
      <img src="https://imagizer.imageshack.com/img923/9517/wwDJUW.png" width="700" title="hover text">
</p>

**running all unit-tests from *test_application.py* and getting failure by looking for a user which is exist in the fake database (mock JSON)(Test #3).

<p align="center">
      <img src="https://imagizer.imageshack.com/img922/872/hLsJ5T.png" width="700" title="hover text">
</p>


<p align="center">
      <img src="https://www.macworld.co.uk/cmsdata/features/3635912/learn_python_mac_thumb800.jpg" width="200" title="hover text">
        <img src="https://img.techentice.com/media/2020/06/docker.png" width="175" title="hover text">
    <img src="https://www.almtoolbox.com/blog_he/wp-content/uploads/2017/09/Git-Logo-2Color-1.png" width="215" title="hover text">
    <img src="https://www.lacework.com/wp-content/uploads/2020/08/up-and-running-with-lacework-and-jenkins.png" width="200" title="hover text">
</p>







