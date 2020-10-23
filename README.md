# [Session-Hijack-101](https://www.youtube.com/watch?v=AhYOtVVSKfo)

#### Woking (On Target Machine) | Ideally you only need two files --> requirements.txt and api_exploit.py
- Install requirements
    - `pip install -r requirements.txt`
- Execute api_exploit.py

#### Now session id is logged on your api endpoint


## Important Talk
```txt
You can use your creativity here to get it executed using only a bash or bat script, or attach it in your python project that
downloads this files along with its requirements and execute it. This is left to the hacker on how he may exploit this with his/her
creative payload
```
```txt
I did it for Moodle, but you can do it for any website making use of session id and poor security too. This is a targeted poc as per
my project requirement.
```

## Mitigation
- Allow only 1 active session to create alert if session id is stolen, just like whatsapp
- IP Logging to detect possible hijack and prevent by invalidating the detected session
- Inactivity leads to session timeout
- Educating students to follow security guidelines such as logging out and not simply closing the window


- Link for viewing the session: [here](https://sessionhijack.herokuapp.com/moodle)

# Part 2
- Analyzing the leaks and User Behaviour

## How to run the web app?
- `pip install requirements.txt`
- `uvicorn server:app --reload`
- All Done!

## Screen-Shots of Web App (I am not using dropdown, because sometimes people are too lazy to drop it...)

![image](https://user-images.githubusercontent.com/41824020/96888692-847de500-14a3-11eb-9c98-827eed0742c8.png)

![image](https://user-images.githubusercontent.com/41824020/96888772-98294b80-14a3-11eb-9fab-12ee2fbcaa3c.png)

![image](https://user-images.githubusercontent.com/41824020/96888833-a8d9c180-14a3-11eb-88a6-ac00166b7754.png)

![image](https://user-images.githubusercontent.com/41824020/96888975-c7d85380-14a3-11eb-8272-7ee60f7e684c.png)

![image](https://user-images.githubusercontent.com/41824020/96889081-e0486e00-14a3-11eb-9933-9c99e4423306.png)

![image](https://user-images.githubusercontent.com/41824020/96889374-29002700-14a4-11eb-9063-0f6e9bc4dfa8.png)

![image](https://user-images.githubusercontent.com/41824020/96889520-4c2ad680-14a4-11eb-9cba-58c69fb978c4.png)

-------------------------------------------------------------------------------------------------------------
