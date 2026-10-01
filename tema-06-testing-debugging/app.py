"""Punto de entrada del Tema 06 - Testing y Debugging.

Este archivo representa la base para probar endpoints con FastAPI.
"""
from fastapi import FastAPI

app = FastAPI(title="Tema 06 - Testing y Debugging")

@app.get("/")
async def root():
    return {"mensaje": "API del tema 06 funcionando"}
