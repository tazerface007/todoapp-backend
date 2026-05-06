from starlette.responses import Response
from starlette.types import ASGIApp, Scope, Receive, Send

class HighPerformanceMiddleware:
    def __init__(self, app: ASGIApp, exclude_paths: set[str]):
        self.app = app
        self.exclude_paths = exclude_paths

    
    async def __call__(self, scope: Scope, receive: Receive, send: Send):

        if scope["type"]!="http":
            return await self.app(scope, receive, send)
        
        path:str = scope['path']
        
        if path == "/.well-known/appspecific/com.chrome.devtools.json":
        # Returning a 204 No Content drops the request without triggering app logic
            response = Response(status_code=204)
            return await response(scope, receive, send)

        if path!="/" and path.endswith("/"):
            path = path.rstrip("/")

        if path in self.exclude_paths:
            return await self.app(scope, receive, send)
        
        print(f'Applying high speed logic to : {scope['path']}')

        await self.app(scope, receive, send)