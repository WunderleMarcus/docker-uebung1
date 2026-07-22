# Docker Übung 1

Dieses Repository enthält eine Docker-Übung sowie eine bereits fertig umgesetzte Beispielanwendung zum Thema **App Deployment mit Docker**.

## 📁 Repository-Struktur

```text
docker-uebung1/
│
├── app/
│   └── ...
│
├── uebung/
│   └── excercise1.md
│
├── .dockerignore
├── Dockerfile
└── README.md
```

## 📝 Die eigentliche Übung

Die eigentliche Aufgabenstellung befindet sich im Ordner:

```text
uebung/
```

Dort ist die Datei `excercise1.md` zu finden. Sie enthält die Aufgabe, die im Rahmen dieser Übung bearbeitet werden soll.

➡️ **Für die Bearbeitung der Übung sollte daher zuerst der Ordner `uebung` geöffnet und die Aufgabenstellung gelesen werden.**

## 🚀 Fertige Beispielaufgabe: App Deployment mit Docker

Der Ordner `app` sowie die Dateien im Hauptverzeichnis enthalten eine bereits fertig umgesetzte Beispielaufgabe zum Thema **Deployment einer Anwendung mit Docker**.

Dabei beziehen sich insbesondere folgende Dateien auf die Beispielanwendung:

* `app/` – enthält die Anwendung, die mit Docker bereitgestellt werden soll
* `Dockerfile` – beschreibt, wie das Docker-Image für die Anwendung erstellt wird
* `.dockerignore` – legt fest, welche Dateien beim Erstellen des Docker-Images nicht in den Build-Kontext übernommen werden

Diese Dateien dienen als Beispiel dafür, wie eine Anwendung containerisiert und anschließend mit Docker ausgeführt werden kann.

## 🐳 Docker-Anwendung starten

Um die Beispielanwendung zu bauen, kann im Hauptverzeichnis des Repositories ein Docker-Image erstellt werden:

```bash
docker build -t docker-uebung1 .
```

Anschließend kann ein Container aus dem Image gestartet werden:

```bash
docker run -p 8080:8080 docker-uebung1
```

Der genaue Port kann abhängig von der Anwendung im Ordner `app` angepasst werden.

## 🎯 Überblick

Zusammengefasst besteht das Repository aus zwei Bereichen:

### 1. Übung

```text
uebung/
```

Enthält die eigentliche Aufgabenstellung und dient zur Bearbeitung der Docker-Übung.

### 2. Fertige Beispielanwendung

```text
app/
Dockerfile
.dockerignore
```

Enthält eine bereits fertig umgesetzte Aufgabe zum **App Deployment mit Docker** und dient als Beispiel bzw. Referenz.

Dadurch können die Dateien im Repository sowohl zum Bearbeiten der Übung als auch zum Nachvollziehen eines vollständigen Docker-Deployments verwendet werden.
