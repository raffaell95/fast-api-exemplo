from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.jobs.write_notification import white_notification
from src.routers import RouterController


app = FastAPI()

RouterController(app).routers()




#CORS
origins = ['http:localhost:3000']
app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)


#Middlewares
@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('Interceptou Chegada..')
    response = await next(request)
    print('Interceptou a Volta..')
    return response


@app.post('/send-email/{email}')
def send_email(email: str, backgound: BackgroundTasks):
    backgound.add_task(white_notification, email, 'Ola tudo bem?')
    return {'status': 'Mensagem enviada'}
