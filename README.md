# Ignacio-django-DLP

## Run Django Project

you download this code from [here](https://github.com/luckystar91121/Ignacio-django-DLP.git) and run project after install django and slackclient and pyee and slackeventapi
```git bash
# install django framework
pip install django

# install slackclient for event hook
pip install slackclient

# install pyee 
pip install pyee

# make db migrations

python manage.py makemigrations
...
python manage.py migrate
...

# run django server with host 0.0.0.0 and port 8000
python manage.py runserver 0.0.0.0:8000
```

## Run Ngrok Server

you download ngrok.exe file from [here](https://ngrok.com/download) and run ngrok server

```git bash
> ngrok http 8000

ngrok by @inconshreveable                                                        (Ctrl+C to quit)
Session Status                online
Account                       luckystar91121@gmail.com (Plan: Free)
Version                       2.3.40
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://b5a9-188-43-136-34.ngrok.io -> http://localhost:8000        
Forwarding                    https://b5a9-188-43-136-34.ngrok.io -> http://localhost:8000       

Connections                   ttl     opn     rt1     rt5     p50     p90     
                              33      0       0.00    0.00    49.33   300.65

```

## Make bot and get Bot Token and Verification Token from Slack

You add your slack app and make bot and get Bot Token and Verification Token from [here](https://api.slack.com/apps)

## Verify Request URL with ngrok url and Set Permission of Bot 

You select [Event Subscription Tag](https://api.slack.com/apps) and register and verify Request URL with ngrok.

### Request URL
```
[ngrok URL]/slack_events/event/hook/
```

### Permission
```
- message:channel
- message:im
```

## Check Result with Django Admin

```
[ngrok URL]/admin
```

you see __Regular_experssions__ and __Detected_messages__.

