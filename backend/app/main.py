from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI()

# Configure CORS middleware
origins = [
    "http://localhost:3000",  # Add your frontend's origin here
    # "https://your-production-domain.com",  # Uncomment and add if needed for production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows the specified origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routes under the `/api` prefix
app.include_router(api_router, prefix="/api")

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI!"}
