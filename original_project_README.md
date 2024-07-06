TicTacToe WebApp

Unser Github Repository ist hier zu finden: https://github.com/Leyiztokvan/tictactoe Mithilfe von HTML, CSS, JavaScript und vor allem Python entstand eine Web-Applikation, die es ermöglicht, online gegen einen reinforcement-learning-Algorithmus TicTacToe zu spielen. Die von überall erreichbare Webseite ist in einem schlichten und doch eleganten Retro-Look gehalten, mit den ikonischen Farben Schwarz und Grün, eine Kombination, die vor allem durch den Kultfilm Matrix bekannt wurde. Durch das minimalistische Design kommt nie Verwirrung auf, es wurde sich nur auf das Nötigste konzentriert, um das User-Erlebnis so unkompliziert wie möglich zu machen. Doch dies ist nicht nur ein simples TicTacToe. Nutzer/innen wird es möglich sein, mit ihrem Spiel and einem Wettbewerb teilzunehmen. Die Spielverläufe sowie persönliche Informationen werden mit einem raffinierten System in einer Datenbank abgespeichert, um neben dem Spassfaktor noch ein sinnvolles Ziel zu haben. Die WebApplikation ist nämlich nicht nur zm Zeitvertreib erstellt worden, sondern auch, um den Algorithmus ausgiebig zu testen. Spielen dient also nicht nur der eigenen Unterhaltung, sondern auch der Wissenschaft.

Bedienung Die Bedienung dieser genialen Applikation ist denkbar einfach. Man wird begrüsst von (muss noch hinzugefügt werden, sobald die Website fertig ist)

Endprodukt Leider ist es uns aufgrund der Zeit und des Schwierigkeitsgrads des Auftrags nicht ganz gelungen, das Programm zum laufen zu bringen. Die einzelnen Bestandteile des Programms funktionieren zwar soweit, jedoch war das Zusammenspiel der verschiedenen Programme, vor allem zwischen den Programmiersprachen, schwieriger und zeitintensiver als gedacht. So funktioniert die Website mit Unterseiten in ihrem Grundgerüst schon, zwischen den verschiedenen Websiten wechseln funktioniert auch, die Websiten wurden mithilfe von CSS schon optisch angepasst, das TicTacToe läuft auch (das ist zugegebenermassen nicht unsere Arbeit), doch wird auch während dem Spielen der Spielverlauf aufgezeichnet und in einer Liste abgespeichert, die später mit den restlichen Nutzerinformationen in die Datenbank eingeschleust werden kann, deren Tabellenerstellung mit Fremdschlüssel auch funktioniert. Zusätzlich funktioniert auch das Senden der Email mit selbst angepasstem Text. Zusammengefasst kann man sagen, das die einzelnen Grundsteine schon funktionieren, und man diese noch richtig zusammenfügen und die Kommunikation zwischen ihnen ermöglichen müsste.

Anmerkung zum Speicherort von App.py: Uns ist bewusst, dass app.py zum back-end gehören würde, jedoch kam es so zu Schwierigkeiten. Unsere Debug-Versuche gelangen aus unerklärlichen gründen nur, wenn app.py im front-end gespeichert ist.

Zu installierende Module: - flask - flask_sqlalchemy - sqlalchemy - psycopg2 - email - smtplib - numpy - pickle - socket - itertools - tkinter

Credits Leo Amstutz Pascal Böhlen Osman Ibrahim Reto Berger (TicTacToe-Programm)