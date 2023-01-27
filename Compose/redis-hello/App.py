import redis
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
host = redis.Redis(host="172.26.80.1", port=6379, decode_responses=True)

if host.exists("counter") == False:
    host.set("counter", 0)

@app.get("/", response_class=HTMLResponse)
async def root():
    contador = host.get("counter")
    host.incr("counter")
    
    return """
       <html>
        <head>
            <title>Contador do Lucas</title>
        </head>
        <body>
            <h2>Você já entrou nesse site {} vezes.</h2>
        </body>
    </html>
    """.format(contador)
    
     

