from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.routers import breeds

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs")


app.include_router(breeds.router)
