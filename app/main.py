"""

Main file

"""

# Importing packages and modules
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from sources.routers import analysis, dashboard

# File information
__author__ = "Leonardo Godói"
__date__ = "2022-02-05"

# Project information
title = "VAI - Vibration Analysis Interface"
description = "FastAPI backend"

# Setting routes
router = APIRouter()
router.include_router(analysis.router)
router.include_router(dashboard.router)

# Instantiating the application
app = FastAPI(
    title=title,
    description=description
)

# Including routes
app.include_router(router)

# Setting the static files directory
app.mount("/static", StaticFiles(directory="sources/templates/static"), name="static")

# Running the application
if __name__ == "__main__":
    uvicorn.run("main:app", debug=True)
