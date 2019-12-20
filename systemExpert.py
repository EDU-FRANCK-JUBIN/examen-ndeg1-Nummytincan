from pyDatalog import pyDatalog
import easygui as eg
pyDatalog.clear()

msg = "Entrer vos informations personnells"
titre = "Intervention"
fieldNames = ["Name","lieux accident","Nombre de victime","Etat des victimes","obstacle"]
fieldValues = []
fieldValues = eg.multenterbox(msg,titre, fieldNames)


while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" est requis\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = eg.multenterbox(errmsg, titre, fieldNames, fieldValues)
print("Réponse :", fieldValues)