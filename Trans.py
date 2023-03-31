from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from googletrans import Translator
from pydantic import BaseModel

app = FastAPI()
translator = Translator()

class TranslationRequest(BaseModel):
    text: str
    dest: str

@app.post("/translate")
async def translate_text(translation_request: TranslationRequest):
    translation = translator.translate(translation_request.text, dest=translation_request.dest)
    result = {"result": translation.text}
    return JSONResponse(content=jsonable_encoder(result))