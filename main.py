from fastapi import FastAPI
from router import router
import uvicorn
main_router = FastAPI()
main_router.include_router(router)
if __name__ == "__main__":
    uvicorn.run(main_router,host="127.0.0.1",port=8000)
