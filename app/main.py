"""

Main file

"""

# Importing packages and modules
import uvicorn
from fastapi import FastAPI, APIRouter
from sources.routers import analysis

# File information
__author__ = "Leonardo Godói"
__date__ = "2022-02-05"

# Project information
title = "VAI - Vibration Analysis Interface"
description = "FastAPI backend"

# Setting routes
router = APIRouter()
router.include_router(analysis.router)

# Instantiating the application
app = FastAPI(
    title=title,
    description=description
)

# Including routes
app.include_router(router)

# Running the application
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
