from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.database import listeners  # noqa: F401
from app.database.engine import init_db
from app.routers import admin, ai, auth, request, user
from app.utils.logger import app_logger, error_logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_body = await request.body()
        app_logger.info(
            f"📥 Request: {request.method} {request.url} | "
            f"Body: {request_body.decode('utf-8')}"
        )

        response = await call_next(request)

        response_body = [chunk async for chunk in response.body_iterator]
        response_body_str = b"".join(response_body).decode("utf-8")

        app_logger.info(f"📤 Response: {response.status_code} | Body: {response_body_str}")

        return Response(
            content=response_body_str,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )


class ExceptionLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            error_logger.error(f"🔥 ERROR: {request.method} {request.url} | {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "https://your-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
app.add_middleware(ExceptionLoggingMiddleware)

app.include_router(user.router)
app.include_router(request.router)
app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(ai.router)
