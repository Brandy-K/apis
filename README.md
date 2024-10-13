## Description of files

###Main.py
Aquest és el punt d'entrada del fastapi on es defineixen tots els punts finals, incloent-hi l'addició, l'actualització i la recuperació de dades dels estudiants. Utilitza el model Pydantic per a la validació de dades i esquemes
###Alumnat.py
Això gestiona la connexió de la base de dades i el funcionament de l'aplicació.  Inclou funcions per llegir tots els registres de l'estudiant, llegir un estudiant per identificador, validar els identificadors de l'aula i afegir nous estudiants a la base de dades.
###alumne.py
Aquest fitxer conté funcions que defineixen com s'estructuren i processen les dades dels estudiants. Inclou esquemes Pydantic per validar les dades dels estudiants i convertir els registres de bases de dades en brut en un format més manejable.
###models.py
S'utilitza per definir estructures de dades addicionals utilitzades al llarg de l'aplicació. Conté el model "Alumne" utilitzat per validar les dades dels alumnes.
