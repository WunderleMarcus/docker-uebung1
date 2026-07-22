# Docker-Übung: Von lokalem Container zu Docker Hub

Willkommen zu dieser praxisorientierten Docker-Übung! 

Dieses Repository enthält eine vollständige Schritt-für-Schritt-Anleitung, mit der du den grundlegenden Workflow von Docker erlernst. Ziel ist es, eine einfache Webanwendung zu containerisieren, das Docker-Image lokal zu erstellen, auf Docker Hub zu veröffentlichen und anschließend erneut aus Docker Hub bereitzustellen.

## Lernziele

Nach Abschluss der Übung kannst du:

* Docker Images erstellen (`docker build`)
* Docker Container starten und verwalten (`docker run`, `docker ps`, `docker stop`)
* Ein Dockerfile erstellen und verstehen
* Images versionieren und taggen (`docker tag`)
* Images auf Docker Hub veröffentlichen (`docker push`)
* Images aus Docker Hub herunterladen (`docker pull`)
* Den kompletten Lebenszyklus eines Docker-Images nachvollziehen

## Zielgruppe

Diese Übung richtet sich an:

* Auszubildende im Bereich Fachinformatik
* Studierende der Informatik
* IT-Administratoren und DevOps-Einsteiger
* Alle, die Docker praxisnah erlernen möchten

Es werden keine Docker-Vorkenntnisse vorausgesetzt. Grundlegende Kenntnisse im Umgang mit der Kommandozeile sind jedoch hilfreich.

## Inhalt des Repositories

```text
.
├── README.md              # Einführung und Informationen zum Projekt
├── Docker-Uebung.md       # Vollständige Übungsanleitung mit Musterlösungen
└── assets/                # Optional: Bilder oder weitere Materialien
```

## Voraussetzungen

Bevor du mit der Übung beginnst, solltest du Folgendes installiert haben:

* Docker Desktop (Windows/macOS) oder Docker Engine (Linux)
* Einen Docker-Hub-Account
* Ein Terminal oder eine PowerShell

Überprüfe deine Installation mit:

```bash
docker --version
docker info
```

## Ablauf der Übung

Während der Übung wirst du:

1. Eine einfache HTML-Webseite erstellen.
2. Ein Dockerfile erstellen.
3. Ein Docker-Image bauen.
4. Einen Container lokal starten.
5. Das Image auf Docker Hub veröffentlichen.
6. Den lokalen Container und das Image entfernen.
7. Das Image erneut aus Docker Hub herunterladen.
8. Den Container erneut starten.

Zum Abschluss folgen Bonusaufgaben, um den Umgang mit Versionen und mehreren Containern zu vertiefen.

## Verwendete Technologien

* Docker
* Docker Hub
* NGINX
* HTML

## Lizenz

Dieses Projekt dient ausschließlich Lern- und Ausbildungszwecken. Es kann frei verwendet, angepasst und erweitert werden.

---

Viel Erfolg beim Ausprobieren und Lernen! 
