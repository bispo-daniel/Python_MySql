#-----------------FRONT-END-------------------
#Instalar o GUI
import PySimpleGUI as sg

def bandOrAlbum():
    list = ['Banda', 'Album', 'Sair']
    myGui = [
        [sg.Text("O que deseja manipular?")],
        [sg.Combo(list, default_value='Selecionar', s=(15, 22), enable_events=True, readonly=True,
                  k='-COMBO-')]
    ]

    res = sg.Window(title="Spotify", layout=[[myGui]], element_justification='c', margins=(50, 140)).read()
    print(res[1]['-COMBO-'])
    return res[1]['-COMBO-']


def init():
    listinha = ['Criar', 'Listar', 'Atualizar', 'Deletar', 'Sair']

    myGui = [
        [sg.Text("O que deseja fazer?")],
        [sg.Combo(listinha, default_value='Selecionar', s=(15, 22), enable_events=True, readonly=True,
                  k='-COMBO-')]
    ]

    res = sg.Window(title="Spotify", layout=[[myGui]], element_justification='c', margins=(50, 140)).read()
    return res[1]['-COMBO-']

def createBand():
    myGui = [
        [sg.Text("Digite o nome da banda: ")],
        [sg.Input(s=30)],
        [sg.Text("Digite o ano de fundação da banda: ")],
        [sg.Input(s=4)],
        [sg.Button('Criar', s=12)]
    ]

    #Criando uma Janela com os parâmetros
    txt = sg.Window(title="Criar banda", layout=[[myGui]], element_justification='c', margins=(15, 22)).read()

    #Dicionário dentro de uma Tupla
    bandName = txt[1][0]
    bandBirth = txt[1][1]

    return [bandName, bandBirth]

def success():
    txt = sg.Window(title="Criar banda", layout=[[sg.Text("Success!")]], element_justification='c', margins=(15, 22)).read()

    return txt

def createAlbum():
    myGui = [
        [sg.Text("Digite o nome do album: ")],
        [sg.Input(s=30)],
        [sg.Text("Digite o ano de lançamento do album: ")],
        [sg.Input(s=4)],
        [sg.Text("Digite o id da banda do album: ")],
        [sg.Input(s=4)],
        [sg.Button('Criar', s=12)]
    ]

    #Criando uma Janela com os parâmetros
    txt = sg.Window(title="Criar banda", layout=[[myGui]], element_justification='c', margins=(15, 22)).read()

    #Dicionário dentro de uma Tupla
    albumName = txt[1][0]
    albumBirth = txt[1][1]
    albumBand = txt[1][2]
    return [albumName, albumBirth, albumBand]

def read(readValues):
    myGui = [
        [sg.Text([readValues])]
    ]

    sg.Window(title="Lista", layout=[[myGui]], element_justification='c', margins=(15, 22)).read()


def updateBand():
    updateList = ['band_name', 'band_birth']

    myGui = [
        [sg.Text("Alterar qual banda? Selecione-a por seu ID...")],
        [sg.Input(s=15)],
        [sg.Combo(updateList, default_value='Selecionar', s=(15, 22), enable_events=True, readonly=True,
                  k='-COMBO-')],
        [sg.Text("Digite o novo valor: ")],
        [sg.Input(s=15)],
        [sg.Button('Atualizar', s=12)]
    ]

    #Criando uma Janela com os parâmetros
    txt = sg.Window(title="Alterar banda", layout=[[myGui]], element_justification='c', margins=(15, 22)).read()

    #Dicionário dentro de uma Tupla
    idBand = txt[1][0]
    column = txt[1]['-COMBO-']
    newVal = txt[1][1]

    return [newVal, idBand], column


def updateAlbum():
    updateList = ['album_name', 'album_birth', 'band_id_FK']

    myGui = [
        [sg.Text("Alterar qual album? Selecione-o por seu ID...")],
        [sg.Input(s=15)],
        [sg.Combo(updateList, default_value='Selecionar', s=(15, 22), enable_events=True, readonly=True,
                  k='-COMBO-')],
        [sg.Text("Digite o novo valor: ")],
        [sg.Input(s=15)],
        [sg.Button('Atualizar', s=12)]
    ]

    #Criando uma Janela com os parâmetros
    txt = sg.Window(title="Alterar album", layout=[[myGui]], element_justification='c', margins=(15, 22)).read()

    #Dicionário dentro de uma Tupla
    idAlbum = txt[1][0]
    column = txt[1]['-COMBO-']
    newVal = txt[1][1]

    return [newVal, idAlbum], column

def delete():
    myLayout = [
        [sg.Text("Digite o id da banda para remove-la: ")],
        [sg.Input(s=4)],
        [sg.Button('Deletar', s=22)]
    ]

    lovelyRita = sg.Window(title="Deletar banda", layout=[[myLayout]], element_justification='c', margins=(15, 22)).read()
    print(lovelyRita[1][0])
    return lovelyRita[1][0]
