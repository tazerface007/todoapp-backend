import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class MyCustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # --- 1. Logic BEFORE the route handler ---
        request.state.start_time = time.time()
        
        # --- 2. Process the request ---
        response = await call_next(request)
        
        # --- 3. Logic AFTER the route handler ---
        duration = time.time() - request.state.start_time
        response.headers["X-Response-Time"] = str(duration)
        print('Middleware fired')
        
        return response
