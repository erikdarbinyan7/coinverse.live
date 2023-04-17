import uvicorn
from config.settings import app, DEBUG

if __name__ == "__main__":
    uvicorn.run(
        app='config.settings:app',
        host="0.0.0.0",
        port=8000,
        log_level="debug" if DEBUG else 'info',
        reload=True,
        workers=10,
)
