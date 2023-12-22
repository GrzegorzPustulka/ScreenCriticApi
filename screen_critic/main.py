import uvicorn
from fastapi import FastAPI

from screen_critic.api.routes.user import router as user_router

app = FastAPI()
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
