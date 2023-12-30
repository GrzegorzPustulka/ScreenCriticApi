import uvicorn
from fastapi import FastAPI

from screen_critic.api.routes.auth import router as auth_router
from screen_critic.api.routes.movie import router as movie_router
from screen_critic.api.routes.movie_list import router as movie_list_router
from screen_critic.api.routes.user import router as user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(movie_list_router)
app.include_router(auth_router)
app.include_router(movie_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
