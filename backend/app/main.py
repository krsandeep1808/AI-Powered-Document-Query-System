from fastapi import FastAPI
from app.api.endpoints import router
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of the FastAPI class
app = FastAPI()

# Define the list of allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "https://muku-chat-pdf.netlify.app"
]

# Add the CORSMiddleware to the FastAPI app instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from the specified origins
    allow_credentials=True,  # Allow credentials (cookies, headers) to be sent with requests
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the router in the FastAPI app instance
app.include_router(router)