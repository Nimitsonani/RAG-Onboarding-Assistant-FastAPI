from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.vectordb import query_db
from app.api import api_call
import markdown

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
def home(request: Request,
         ans:str = None):
    if ans:
        ans = markdown.markdown(ans)
    return templates.TemplateResponse(name='index.html',request=request,context={'ans':ans})

@app.post('/')
def post_home(query :str = Form(...)):
    vector_list = query_db(query)
    response_model = api_call(query,vector_list)
    return RedirectResponse(url=f'/?ans={response_model}',status_code=303)

