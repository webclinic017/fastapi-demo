from fastapi import Request, Response,status
from fastapi.routing import APIRoute
from typing import Callable
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import time
import sys
import traceback
from app.config.config import fs_config

class FSRoute(APIRoute):
    '''
    自定义路由
    '''
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                env = fs_config.get("env")
                if env and env.get('TIME'):
                    #记录时间
                    before = time.time()
                    response: Response = await original_route_handler(request)
                    duration = time.time() - before
                    response.headers["X-Response-Time"] = str(duration)
                    return response
                else:
                    return await original_route_handler(request)
            except Exception as exc: #except StarletteHTTPException as exc
                body = await request.body()
                exc_type, exc_instance, exc_traceback = sys.exc_info()
                formatted_tbtext = traceback.format_tb(exc_traceback.tb_next)
                error = '\n[Exception]:{0}-{1}'.format(formatted_tbtext, exc_instance)
                request.app.logger.error(error)
                detail = '[Exception]:{0}'.format(exc_instance)
                return JSONResponse(
                    status_code=status.HTTP_417_EXPECTATION_FAILED,
                    content=jsonable_encoder({
                        "status": -1,
                        "msg": detail,
                    }),
                )


        return custom_route_handler

