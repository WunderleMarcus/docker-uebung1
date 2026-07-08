# Docker-Übung: Von der lokalen Webanwendung zu Docker Hub

## Lernziele

Nach dieser Übung kannst du:

- Docker Images erstellen
- Docker Container starten
- Container verwalten
- Images zu Docker Hub hochladen
- Images von Docker Hub herunterladen
- Container aus Docker Hub starten

---

# Voraussetzungen

Installiert sind:

- Docker Desktop oder Docker Engine
- Docker Hub Account
- Terminal oder PowerShell

Prüfen:

```bash
docker --version
docker info
```

---

# Aufgabe 1 – Projekt erstellen

Erstelle einen neuen Ordner.

```text
docker-webapp
```

Wechsle anschließend in diesen Ordner.

## Erstelle die Datei

`index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Meine Docker Übung</title>
</head>
<body>
    <h1>Hallo Docker!</h1>
    <p>Dieses Image wurde lokal erstellt.</p>
</body>
</html>
```

---

# Musterlösung

Ordner erstellen:

```bash
mkdir docker-webapp
cd docker-webapp
```

Datei erstellen:

```bash
touch index.html
```

Unter Windows kann die Datei auch mit dem Editor erstellt werden.

---

# Aufgabe 2 – Dockerfile erstellen

Erstelle eine Datei mit dem Namen

```text
Dockerfile
```

### Anforderungen

- Verwende einen Webserver
- Kopiere die HTML-Datei
- Öffne Port 80

---

# Musterlösung

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

## Erklärung

### FROM

Verwendet das offizielle nginx-Image.

```dockerfile
FROM nginx:alpine
```

Die Alpine-Version ist besonders klein.

---

### COPY

Kopiert die HTML-Datei in den Standardordner von nginx.

```dockerfile
COPY index.html /usr/share/nginx/html/index.html
```

---

### EXPOSE

Dokumentiert, dass der Container Port 80 verwendet.

```dockerfile
EXPOSE 80
```

---

# Aufgabe 3 – Image bauen

Baue nun dein Docker Image.

Das Image soll heißen:

```text
docker-webapp
```

---

# Musterlösung

```bash
docker build -t docker-webapp .
```

## Erklärung

| Parameter | Bedeutung |
|-----------|-----------|
| docker build | Erstellt ein Image |
| -t | Vergibt einen Namen |
| . | Aktuelles Verzeichnis verwenden |

Kontrolle:

```bash
docker images
```

Beispiel:

```
REPOSITORY       TAG       IMAGE ID
docker-webapp    latest    8a1fd91f
```

---

# Aufgabe 4 – Container starten

Starte das Image.

Vorgaben:

- Name: webapp
- Hintergrundmodus
- Port 8080 → 80

---

# Musterlösung

```bash
docker run -d \
--name webapp \
-p 8080:80 \
docker-webapp
```

Unter Windows:

```bash
docker run -d --name webapp -p 8080:80 docker-webapp
```

## Erklärung

| Option | Bedeutung |
|---------|-----------|
| -d | Hintergrundmodus |
| --name | Containername |
| -p | Portweiterleitung |

Browser:

```
http://localhost:8080
```

---

# Aufgabe 5 – Container untersuchen

Finde heraus:

- Welche Container laufen?
- Welche Images existieren?
- Welche Logs besitzt der Container?
- Welche Ports nutzt er?

---

# Musterlösung

Container anzeigen

```bash
docker ps
```

Alle Container

```bash
docker ps -a
```

Images

```bash
docker images
```

Logs

```bash
docker logs webapp
```

Containerinformationen

```bash
docker inspect webapp
```

---

# Aufgabe 6 – Docker Hub Login

Melde dich bei Docker Hub an.

---

# Musterlösung

```bash
docker login
```

Danach erscheint:

```
Username:
Password:
```

Nach erfolgreichem Login:

```
Login Succeeded
```

---

# Aufgabe 7 – Image taggen

Docker Hub erwartet folgendes Format:

```
BENUTZERNAME/IMAGE:TAG
```

Beispiel:

```
maxmustermann/docker-webapp:v1
```

---

# Musterlösung

```bash
docker tag docker-webapp BENUTZERNAME/docker-webapp:v1
```

Kontrolle:

```bash
docker images
```

Jetzt existieren zwei Tags für dasselbe Image.

---

# Aufgabe 8 – Image hochladen

Lade dein Image hoch.

---

# Musterlösung

```bash
docker push BENUTZERNAME/docker-webapp:v1
```

Nach einigen Sekunden erscheint:

```
latest: digest: ...
```

Kontrolle auf Docker Hub:

Das Repository sollte nun sichtbar sein.

---

# Aufgabe 9 – Container löschen

Stoppe den Container.

Lösche anschließend den Container.

---

# Musterlösung

Container stoppen

```bash
docker stop webapp
```

Container löschen

```bash
docker rm webapp
```

Kontrolle

```bash
docker ps -a
```

Der Container sollte verschwunden sein.

---

# Aufgabe 10 – Image löschen

Lösche das lokale Image.

---

# Musterlösung

```bash
docker rmi docker-webapp
```

Anschließend:

```bash
docker rmi BENUTZERNAME/docker-webapp:v1
```

Kontrolle

```bash
docker images
```

Das Image sollte nicht mehr erscheinen.

---

# Aufgabe 11 – Image herunterladen

Lade dein Image erneut aus Docker Hub.

---

# Musterlösung

```bash
docker pull BENUTZERNAME/docker-webapp:v1
```

Kontrolle

```bash
docker images
```

Das Image ist wieder vorhanden.

---

# Aufgabe 12 – Container erneut starten

Starte den Container erneut.

Name:

```
webapp2
```

Port:

```
8080 → 80
```

---

# Musterlösung

```bash
docker run -d \
--name webapp2 \
-p 8080:80 \
BENUTZERNAME/docker-webapp:v1
```

Unter Windows:

```bash
docker run -d --name webapp2 -p 8080:80 BENUTZERNAME/docker-webapp:v1
```

Browser öffnen:

```
http://localhost:8080
```

Die Webseite sollte wieder angezeigt werden.

---

# Bonusaufgabe 1 – Version 2 erstellen

Ändere die HTML-Datei.

```html
<h1>Hallo Docker!</h1>
<p>Version 2</p>
```

---

## Musterlösung

Image neu bauen

```bash
docker build -t docker-webapp .
```

Tag vergeben

```bash
docker tag docker-webapp BENUTZERNAME/docker-webapp:v2
```

Push

```bash
docker push BENUTZERNAME/docker-webapp:v2
```

---

# Bonusaufgabe 2 – Zwei Versionen gleichzeitig starten

Starte Version 1 auf Port 8081.

---

## Musterlösung

```bash
docker run -d \
--name webapp-v1 \
-p 8081:80 \
BENUTZERNAME/docker-webapp:v1
```

Version 2 auf Port 8082

```bash
docker run -d \
--name webapp-v2 \
-p 8082:80 \
BENUTZERNAME/docker-webapp:v2
```

Browser:

```
http://localhost:8081
```

```
http://localhost:8082
```

Jetzt laufen beide Versionen parallel.

---

# Bonusaufgabe 3 – Container entfernen

Stoppe alle laufenden Container.

---

## Musterlösung

```bash
docker stop webapp-v1
docker stop webapp-v2
```

Container löschen

```bash
docker rm webapp-v1
docker rm webapp-v2
```

---

# Zusammenfassung der wichtigsten Docker-Befehle

| Befehl | Beschreibung |
|----------|--------------|
| docker build | Image erstellen |
| docker run | Container starten |
| docker ps | Laufende Container anzeigen |
| docker ps -a | Alle Container anzeigen |
| docker images | Images anzeigen |
| docker stop | Container stoppen |
| docker start | Container starten |
| docker restart | Container neu starten |
| docker rm | Container löschen |
| docker rmi | Image löschen |
| docker logs | Logs anzeigen |
| docker inspect | Detailinformationen |
| docker login | Anmeldung Docker Hub |
| docker tag | Image umbenennen |
| docker push | Image hochladen |
| docker pull | Image herunterladen |

---

# Wissensfragen

## Frage 1

Was ist der Unterschied zwischen einem Image und einem Container?

**Lösung**

Ein Image ist eine Vorlage. Ein Container ist eine laufende Instanz eines Images.

---

## Frage 2

Welcher Befehl erstellt ein Image?

**Lösung**

```bash
docker build
```

---

## Frage 3

Welcher Befehl lädt ein Image von Docker Hub?

**Lösung**

```bash
docker pull
```

---

## Frage 4

Welcher Befehl lädt ein Image zu Docker Hub hoch?

**Lösung**

```bash
docker push
```

---

## Frage 5

Wie lautet das allgemeine Format eines Docker-Hub-Tags?

**Lösung**

```
BENUTZERNAME/IMAGE:TAG
```

---

# Fazit

Du hast erfolgreich gelernt,

- eine Webanwendung zu containerisieren,
- ein Docker Image zu erstellen,
- einen Container lokal auszuführen,
- das Image auf Docker Hub hochzuladen,
- das lokale Image zu löschen,
- das Image erneut herunterzuladen und
- den Container aus Docker Hub erneut zu starten.

Damit hast du den vollständigen Lebenszyklus eines Docker-Images kennengelernt – von der Entwicklung bis zur Bereitstellung.
