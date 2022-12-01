import os

import uvicorn

from app import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run('app:create_app', host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True, factory=True)
