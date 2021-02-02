from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8091)
    #或者命令行，reload是程序改动自动重启服务
    #uvicorn main:app --host '0.0.0.0' --port 8091 --reload