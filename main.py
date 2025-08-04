from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

SCORONCO_API = "https://graphql.scorenco.com/v1/graphql"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "content-type": "application/json",
    "x-hasura-role": "anonymous",
    "x-hasura-locale": "fr-FR",
    "Origin": "https://scorenco.com",
    "Referer": "https://scorenco.com/"
}

@app.post("/")
async def proxy(request: Request):
    try:
        body = await request.body()
        response = requests.post(SCORONCO_API, headers=HEADERS, data=body, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}