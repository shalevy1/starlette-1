# A simple starlette server.

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='static/html')


async def homepage(request):
    return templates.TemplateResponse('home.html', {'request': request})


async def posts(request):
    return JSONResponse({'page': 'posts'})


async def projects(request):
    return JSONResponse({'page': 'projects'})


async def about(request):
    return JSONResponse({'page': 'about'})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/posts', posts),
    Route('/projects', projects),
    Route('/about', about),
    Mount('/static', app=StaticFiles(directory='static'), name="static")
])