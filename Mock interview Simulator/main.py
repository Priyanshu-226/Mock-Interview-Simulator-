from fastapi import FastAPI
from routers import roles, resume, intro, stt, scoring

app = FastAPI(title="Mock Interview Simulator")

app.include_router(roles.router, prefix="/roles")
app.include_router(resume.router, prefix="/resume")
app.include_router(intro.router, prefix="/intro")
app.include_router(stt.router, prefix="/stt")
app.include_router(scoring.router, prefix="/scoring")