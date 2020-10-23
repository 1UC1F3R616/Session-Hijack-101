
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
# f = open('mass_dump.txt', 'r') # user mass dump goes here
# f_read = f.read()
# f.close()

Education = set()
Entertainment = set()
Malicious = set()
Shopping_and_Self = set()
Social_Networking = set()
Travel_and_Tourism = set()
Others = set()

categories = [Education, Entertainment, Malicious, Shopping_and_Self, Social_Networking, Social_Networking, Travel_and_Tourism, Others]

education = open('./clean_categories/education_read', 'r')
education_read = education.readlines()
education.close()

entertainment = open('./clean_categories/entertainment_read', 'r')
entertainment_read = entertainment.readlines()
entertainment.close()

malicious = open('./clean_categories/malicious_read', 'r')
malicious_read = malicious.readlines()
malicious.close()

others = open('./clean_categories/others_read', 'r')
others_read = others.readlines()
others.close()

shopping = open('./clean_categories/shopping_read', 'r')
shopping_read = shopping.readlines()
shopping.close()

social = open('./clean_categories/social_read', 'r')
social_read = social.readlines()
social.close()

tandt = open('./clean_categories/tandt_read', 'r')
tandt_read = tandt.readlines()
tandt.close()

cjs = str(cj)

for website in education_read:
    # print(website)
    if website.strip() in cjs:
        Education.add(website)
for website in entertainment_read:
    if website.strip() in cjs:
        Entertainment.add(website)
for website in malicious_read:
    if website.strip() in cjs:
        Malicious.add(website)
for website in shopping_read:
    if website.strip() in cjs:
        Shopping_and_Self.add(website)
for website in social_read:
    if website.strip() in cjs:
        Social_Networking.add(website)
for website in tandt_read:
    if website.strip() in cjs:
        Travel_and_Tourism.add(website)
for website in others_read:
    if website.strip() in cjs:
        Others.add(website)

Education = list(Education)
Entertainment = list(Entertainment)
Malicious = list(Malicious)
Shopping_and_Self = list(Shopping_and_Self)
Social_Networking = list(Social_Networking)
Travel_and_Tourism = list(Travel_and_Tourism)
Others = list(Others)
############################################## utils #########################################

@app.get('/')
@app.get("/home")
@app.get("/index")
async def home(request: Request):
    result = {'Education': len(Education), 'Entertainment': len(Entertainment), 'Malicious': len(Malicious), 'Shopping_and_Self': len(Shopping_and_Self), 'Social_Networking': len(Social_Networking), 'Travel_and_Tourism': len(Travel_and_Tourism), 'Others': len(Others), 
    'tokens': len(tokens), 'sessions': len(sessions)
    }
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

@app.get("/websites")
async def websites(request: Request):
    result = {'Education': Education, 'Entertainment': Entertainment, 'Malicious': Malicious, 'Shopping_and_Self': Shopping_and_Self, 'Social_Networking': Social_Networking, 'Travel_and_Tourism': Travel_and_Tourism, 'Others': Others}
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

