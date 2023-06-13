from sqlalchemy.orm import Session

from . import models, schemas

def create_dvd(db: Session, dvd: schemas.Dvd):
    db_dvd = models.DVD(dvdtitle=dvd.dvdtitle, dvdgenre=dvd.dvdgenre, dvditems=dvd.dvditems)
    db.add(db_dvd) #eisagei to dvd ston pinaka tis vasis
    db.commit() #efarmozei tin eisagwgi
    db.refresh(db_dvd) #enimerwtnei tin vasi
    return db_dvd

def get_dvd_by_title(db: Session, title: str):
    return db.query(models.DVD).filter(models.DVD.dvdtitle == title).first()


def get_dvd(db: Session, dbdvd_id: int):
    return db.query(models.DVD).filter(models.DVD.id == dbdvd_id).first()

def get_all_dvds(db: Session):
    return db.query(models.DVD).all()

def delete_dvd(db: Session, dbdvd_id: int):
    done = db.query(models.DVD).filter(models.DVD.id== dbdvd_id).delete()
    db.commit() #efarmogi twn allagwn meta to delete
    return done #epistrofi apotelesmatos

def update_dvd(db: Session, dbdvd_id: int, dbdvd: schemas.Dvd):
    dvd = db.query(models.DVD).filter(models.DVD.id == dbdvd_id).first()
    if not dvd: #ean den vrethei to dvd
        return "No Dvd found"
    
    if dbdvd.dvdgenre:
        dvd.dvdgenre = dbdvd.dvdgenre
    if dbdvd.dvditems:
        dvd.dvditems = dbdvd.dvditems
    db.commit()

    return "Dvd info changed!"
    
