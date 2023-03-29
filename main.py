import sys

import gui
import mysql.connector

#Criar conexão com o BD
myDb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database='spotify'
)
myCursor = myDb.cursor()

def create(bandOrAlbum):
    if bandOrAlbum == 'band':
        sql = "INSERT INTO {} ({}_name, {}_birth) VALUES (%s, %s)".format(bandOrAlbum, bandOrAlbum, bandOrAlbum)
        valLista = gui.createBand()
        valuesTuple = (valLista[0], valLista[1])
        myCursor.execute(sql, valuesTuple)
    elif bandOrAlbum == 'album':
        sql = "INSERT INTO {} ({}_name, {}_birth, band_id_FK) VALUES (%s, %s, %s)".format(bandOrAlbum, bandOrAlbum, bandOrAlbum)
        valList = gui.createAlbum()
        valuesTuple = (valList[0], valList[1], valList[2])
        myCursor.execute(sql, valuesTuple)

    myDb.commit()
    gui.success()
    init()

def read(bandOrAlbum):
    sql = "SELECT * FROM {}".format(bandOrAlbum)
    myCursor.execute(sql)
    rows = myCursor.fetchall()

    resList = []
    for x in rows:
        resList.append(x)

    gui.read(resList)
    init()

def update(bandOrAlbum):
    if bandOrAlbum == "band":
        valList = gui.updateBand()
        updateTuple = (valList[0][0], valList[0][1])

        sqlUpdate = "UPDATE band SET {} = %s WHERE band_id = %s".format(valList[1])
        myCursor.execute(sqlUpdate, updateTuple)

    elif bandOrAlbum == "album":
        valList = gui.updateAlbum()
        updateTuple = (valList[0][0], valList[0][1])

        sqlUpdate = "UPDATE album SET {} = %s WHERE album_id = %s".format(valList[1])
        myCursor.execute(sqlUpdate, updateTuple)


    myDb.commit()
    print(myCursor.rowcount, "Record(s) affected")
    init()

def delete(bandOrAlbum):
    id = gui.delete()
    idVal = [id]

    print(idVal)

    sql = "DELETE FROM {} WHERE {}_id = %s".format(bandOrAlbum, bandOrAlbum)
    myCursor.execute(sql, idVal)
    myDb.commit()
    print(myCursor.rowcount, "Record(s) deleted")
    init()

def chooseBandOrAlbum(option):
    if option == 'Banda':
        return 'band'
    elif option == 'Album':
        return 'album'
    elif option == 'Sair':
        sys.exit()

def choose(op):
    if op == 'Criar':
        create(save)
    elif op == 'Listar':
        read(save)
    elif op == 'Atualizar':
        update(save)
    elif op == 'Deletar':
        delete(save)
    elif op == 'Sair':
        sys.exit(0)

#Mágica da tela inicial
def init():
    bandOrAlbum = gui.bandOrAlbum()
    global save
    save = chooseBandOrAlbum(bandOrAlbum)

    operation = gui.init()
    choose(operation)

init()