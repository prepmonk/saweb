from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://0.0.0.0:5055",
    "http://127.0.0.1:5055",
    "http://localhost:5055",
    "*",
]


def add_app_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
