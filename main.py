import pandas as pd
from fastapi import FastAPI, HTTPException, Header

df = pd.read_csv('players.csv')

prog = FastAPI()

API_KEY = "apikeyftdssub02"

@prog.get("/")
def homepage () :
    return {"message" : "Welcome to players API"}

@prog.get("/players")
def getAllPlayers(api_key : str = Header(None)) :
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Wrong API KEY")
    else :
        return df.to_dict(orient="records")
    
@prog.get("/players/state/{state}")
def getPlayerbystate (state : str, api_key :str = Header(None)):
    print(api_key)
    print(state)
    if api_key is None or api_key != API_KEY:
        raise HTTPException (status_code=401, detail="Wrong API KEY")
    else :
        player_by_state = df[df['state'] == state]
        return player_by_state.to_dict(orient='recordS')

@prog.get("/players/position/{position}")
def getPlayerbystate (position : str, api_key :str = Header(None)):
    print(api_key)
    print(position)
    if api_key is None or api_key != API_KEY:
        raise HTTPException (status_code=401, detail="Wrong API KEY")
    else :
        player_by_state = df[df['position'] == state]
        return player_by_state.to_dict(orient='recordS')
    