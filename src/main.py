from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import sys
sys.path.append("..")

from src.movies import utils, models, schemas
from src.database import SessionLocal, engine

#dimiourgia olwn twn pinakwn
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello" : "World"}


@app.post("/dvd/create", response_model=schemas.Dvd)
async def create_dvd(dvd: schemas.DvdBase, db: Session = Depends(get_db)):
    if dvd.dvditems <= 0: #ean den exoun dwthei temaxia sto dvd
        raise HTTPException(status_code=400, detail="Wrong number of pieces")
    dbdvd = utils.get_dvd_by_title(db, title=dvd.dvdtitle) #anazitisi tainias me ton titlo
    if dbdvd: #elegxos ean uparxei idi i tainia
        raise HTTPException(status_code=400, detail="Title movie already exists")
    return utils.create_dvd(db=db, dvd=dvd)


@app.get("/dvd/" , response_model=list[schemas.Dvd])
async def get_dvd(dvdid: int | None = None, title: str | None = None, db: Session = Depends(get_db)):
    if title and not dvdid: #ean exei dwsei titlo
        dbdvd = utils.get_dvd_by_title(db, title=title) #anazitisi tainias me ton titlo
        if not dbdvd or dbdvd is None: #elegxos ean uparxei idi i tainia
            raise HTTPException(status_code=400, detail="Title movie not exists")
    elif not title and dvdid:
        dbdvd = utils.get_dvd(db, dbdvd_id=dvdid) #anazitisi me to id tis tainias
        if not dbdvd or dbdvd is None: 
            raise HTTPException(status_code=400, detail="Id of movie not exists")
    elif title and dvdid:
        dbdvd = utils.get_dvd_by_title(db, title=title) #anazitisi tainias me ton titlo
        if not dbdvd or dbdvd is None: #elegxos ean uparxei idi i tainia
            raise HTTPException(status_code=400, detail="Title movie not exists")
        if (dvdid == dbdvd.id):
            return dbdvd
        else:
            raise HTTPException(status_code=400, detail="No movie with such id and title")
    elif not title and not dvdid:
        print ("hoooo")
        return( utils.get_all_dvds(db=db)) #epistrofi olwn twn dvd apo tin vasi
    
    return [dbdvd] #epistrofi tou dvd se morfi pinaka
      
      
@app.delete("/dvd/remove/{dvd_id}")
async def delete_dvd(dvd_id: int, db: Session = Depends(get_db)):
    response = utils.delete_dvd(db=db, dbdvd_id=dvd_id)
    if response == 0:
        return HTTPException(status_code=400, detail="Id of movie not exists")
    else:
        return "Success"

@app.patch("/dvd/update/{dvd_id}") #sunartisi gia allagi twn stoixeiwn tou dvd
def update_hero(dvd_id: int, dvd: schemas.DvdBase, db: Session = Depends(get_db)):
    return utils.update_dvd(db=db, dbdvd_id=dvd_id, dbdvd=dvd)


