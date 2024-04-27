import os
import logging
import time
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.configs.config import basicSettings
from app.middleware.exception import exception_message
from app.routers.v1.base import router_v1

def init_app():
    app = FastAPI(
        version=basicSettings.VERSION,
        title=basicSettings.TITLE
    )
    
    app.include_router(router_v1, prefix=basicSettings.BASE_PREFIX)
    
    # # Setting local Static files directory (offline)
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # static_dir = os.path.join(BASE_DIR, 'static')
    # app.mount('/static', StaticFiles(directory=static_dir), name="static")
    
    # origins = ["http://localhost"]
    origins = ["*"]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
  
    return app

APP = init_app()

# origins = ["*"]
    
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*']
# )

@APP.get("/")
async def root():
    return {"message": "Hello World"}


uvicorn_logger = logging.getLogger('uvicorn.error')
system_logger = logging.getLogger('custom.error')

@APP.middleware("http")
async def log_middleware(request: Request, call_next):
    
    # print(request.url.path)
    # print(request.client.host)
    
    start_time = time.time()
    
    try:
        response = await call_next(request)
    
    except Exception as e:
        system_logger.error(exception_message(e))
        response = JSONResponse(
            status_code=500,
            content={"message": "internal server error"}
        )
        
    finally:
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    
    
### Define Exception Handler
@APP.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    '''Define the response format while raising HTTPException'''
    if exc.status_code == 404:
        return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail})
    elif exc.status_code == 500:
        return JSONResponse(
        status_code=exc.status_code,
        content={"message": "internal server error"})
    else:
        return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail})

if __name__ == "__main__":

    expose_port = os.environ['FASTAPI_PORT']
    worker_count = os.environ['WORKER_COUNT']
    debug = os.getenv('DEBUG',False) == 'True'
    debug =True
    uvicorn.run(
      "main:APP",
      host="0.0.0.0",
      port=basicSettings.SERVICE_PORT,
      workers=basicSettings.WORKER_COUNT,
      reload=basicSettings.SERVICE_DEBUG,
    #   reload=True,
      root_path=basicSettings.BASE_PATH,
      log_level="info",
      log_config='./app/configs/log_conf.yml'
      )