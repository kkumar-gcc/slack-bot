# main.py

import uvicorn
from fastapi import FastAPI
from app.api.routes import router
from fastapi import Request
from app.bots.slack_bot import app_handler
from app.bots.slack_bot import app as slack_app

api = FastAPI()

# Mount the API router
api.include_router(router)


@router.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


# Run the FastAPI server
if __name__ == "__main__":
    # Start the FastAPI server
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
