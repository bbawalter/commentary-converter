# commentary-converter
finds references to surahs and verses of a certain format in texts and adds tags to it 


# Automatisierte Tagsetzung in Texten #
 
Dies ist ein Programm, das Suren- und Versverweise in Texten anhand ihres Aufbaus erkennt und automatisch die benötigten Tags ergänzt.
 
### Akzeptierte Formate: ###
    
Suren
ein für Menschen gut lesbares “Sure 3” ist (im Moment) für das Programm nicht erkennbar. Um einen Verweis als einen solchen zu Kennzeichnen, sollte er dem folgenden Schema folgen:
 
    Q[Leerzeichen][Sure]
    Q[Leerzeichen][Sure]:[Vers]
    Q[Leerzeichen][Sure]:[Vers]-[Vers]
 
z.B.:

		Q 1           nicht     Q1
		Q 1:2         nicht     Q 1 :2 oder Q 1: 2
		Q 23:2-3      nicht     Q 23 :2-3   Q 23: 2 - 3

Aufzählung mehrer Verweise – Das Programm erkennt nur einzelne Verweise. Daher müssen auch Aufzählungen als einzelne Verweise erkennbar sein. 

		Q 1, Q 2, Q 3				nicht     Q 1, 2, 3
		Q 23:2-3, Q 32:3, Q 42:3-4		nicht     Q 23:2-3, 32:3, 42:3-4
 
### f und ff ###
Hier ist es wichtig, dass kein Leerzeichen zwischen dem [Vers] und [f] / [ff] ist. Die Buchstaben würden sonst nicht als zum Vers zugehörig erkannt werden. 

	 Q[Leerzeichen][Sure]:[Vers]f    - dieser und der folgende Vers
	 Q[Leerzeichen][Sure]:[Vers]ff   - dieser und die 3 folgenden Verse
 
z.B.  

	 Q 23:2f    	nicht     Q 23:2 f
	 Q 23:2ff    	nicht     Q 23:2 ff 

Wichtig: sollte eine exakte Angabe gewünscht sein, die genauer als “dieser und die 3 folgenden Verse” ist, muss es im Text spezifiziert werden
z.B.     

		Q 23:2ff       ersetzen durch     Q 23:2-4
		Q 23:2ff       ersetzen durch      Q 23:2-5
	
Dann würden wirklich nur die relevanten Verse gezeigt.       

### Versverweise ###
auch hier ist auf die richtigen Schlüsselzeichen zu achten. Während sich “Verspaar 2 und 3” für einen Menschen gut liest, ist das für das Programm nicht zu erfassen und müsste durch “Verse 2-3” oder “V 2-3” oder “V. 2-3” ersetzt werden. 
 
	V[Leerzeichen][Vers]
	V.[Leerzeichen][Vers]
	V[Leerzeichen][Vers]-[Vers]
	V.[Leerzeichen][Vers]-[Vers]
	Vers[Leerzeichen][Vers]
	Verse[Leerzeichen][Vers]-[Vers]

###### analog f und ff ###### 
es funktioniert wenn es direkt folgt:  V 2f  nicht  V 2 f 
Aufzählungen: V 2, V 3, V 4 statt V 2, 3, 4
z.B.

	V 2        	nicht     V2
	V. 2        ...
	V 1-2
	V. 1-2      nicht     V. 1- 2
	Vers 1
	Verse 1-2
	V 2f        nicht     V 2 f
	V 2ff
 
### TUK ###
Verweise auf TUK, die einer der folgenden Formen entsprechen, werden ohne Probleme erkannt und mit den entsprechenden Tags versehen.

	TUK 2
	TUK, 234        (mit Komma)
	TUK Nummer 123    (mit Nummer)
	TUK Nr. 123        (mit Nr.)
 
Die Ausgabe nach Durchlaufen des Programms ist einheitlich “TUK xyz”
