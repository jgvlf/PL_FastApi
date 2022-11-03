from fastapi import HTTPException, status
from fastapi import Response
from fastapi import FastAPI
from modules.models.Languages import Languages

languagess = {
  1: {
    "nome": "Rust",
    },
 2: {
    "nome": "Elixir",
    },
}

app = FastAPI()
@app.get('/')
async def raiz():
    return {"msg":"Aprendiz de DS"}

@app.get('/languages')
async def get_languagess():
    return languagess

@app.get('/languages/{languages_id}')
async def get_languages(languages_id : int):
    try:
        languages = languagess[languages_id]
        languages.update({"id":languages_id})
        return languages
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Linguagem não Encontrada.')

@app.post('/languages', status_code=status.HTTP_201_CREATED)
async def post_languagess(languages: Languages):
    if languages.id not in languagess:
        languages.id = len(languagess)+1
        languagess[languages.id] = languages
        return languages
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe uma linguagem com o ID {languages.id}")

@app.put('/languagess/{languages_id}')
async def put_languages(languages_id: int, languages: Languages):
    if languages_id in languagess:
        languagess[languages_id] = languages
        return languages
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa Linguagem Não Existe.")

@app.delete('/languagess/{languages_id}')
async def delete_languages(languages_id: int):
    if languages_id in languagess:
        del languagess[languages_id]
        return Response(status_code = status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code = status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa Linguagem Não Existe.")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)