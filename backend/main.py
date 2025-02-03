from fastapi import FastAPI
from routes.voice_call import voice_call_router
from routes.heygen_call import heygen_call_router

app = FastAPI()

# Include routes for AI Voice Calls and HeyGen Avatar
app.include_router(voice_call_router, prefix="/voice", tags=["Voice Calls"])
app.include_router(heygen_call_router, prefix="/avatar", tags=["HeyGen Avatar Calls"])

@app.get("/")
def read_root():
    return {"message": "AI Voice Agent Backend is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)