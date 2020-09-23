# Session-Hijack-101

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