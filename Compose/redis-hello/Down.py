import redis
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
host = redis.Redis(host="172.26.80.1", port=6379, decode_responses=True)

if host.exists("counter") == False:
    host.set("counter", 0)

@app.get("/", response_class=HTMLResponse)
async def root():
    host.decr("counter")
    contador = host.get("counter")
    return """
       <html>
        <head>
            <title>Contador do Lucas - Site de decréscimo</title>
        </head>
        <body>
            <h2>Você entrou no site que reduz o contador no redis, logo a contagem agora é de {} vezes.</h2>
        </body>
    </html>
    """.format(contador)
    
     

