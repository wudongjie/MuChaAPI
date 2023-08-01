from fastapi import FastAPI
import uvicorn
from midjourney import mj_api
from chatgpt import gpt_api

app = FastAPI(title="Muchi API",
              description="Autogenerating images for your article.",
              version="1.0.0")

app.include_router(mj_api, prefix="/midjourney", tags={"Mucha Midjourney API"})
app.include_router(gpt_api, prefix="/chatgpt", tags={"Mucha ChatGPT API"})
if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000,
                reload=True, workers=1)
