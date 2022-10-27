class Request:
    def __init__(self):
        from fastapi import FastAPI
        self.app = FastAPI()