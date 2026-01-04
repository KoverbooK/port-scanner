# port-scanner
##### A python script wich allows to find available ports

## Description

  Ce projet est un scanner de ports développé en Python. Il permet de :

* Scanner une plage de ports sur un hôte donné (adresse IP ou nom de domaine).

* Gérer le nombres de threads pour améliorer la vitesse de scan.

* Afficher les bannières des ports ouverts.

Les bannières peuvent être des informations de service (comme HTTP, FTP, etc.) envoyées par un serveur lorsque l'on envoie une requête

## Fonctionnalités

* Scan des ports : Vous pouvez spécifier un intervalle de ports à scanner avec ```--ports``` (par défaut, de 1 à 1024).

* Banner grabbing : Lorsque l'option ```--banners``` est activée, le programme essaie de récupérer la bannière de service pour chaque port ouvert.

* Multithreading : Il est possible de configurer le nombre maximum de threads à utiliser via l'option ```--max-threads```

## Installation
```bash
git clone https://github.com/KoverbooK/port-scanner.git
cd port-scanner
```

## Exemples 
Avec l'host "example.com".
* Scanner un seul port (exemple : port 80) :
```bash
python3 scanPort.py example.com --ports 80 80
```
* Scanner plusieurs ports entre 1 et 1024, avec récupération des bannières :
```bash
  python3 scanPort.py example.com --ports 1 1024 --banners
```
* Scanner plusieurs ports avec un nombre réduit de threads :
```bash
python3 scanPort.py example.com --ports 1 1024 --max-threads 50
```

## Limitations

* Le programme peut rencontrer des limitations selon le réseau et les ports scannés. Par exemple, certains ports peuvent ne pas répondre ou avoir une réponse trop lente.

* Le banner grabbing n'est pas toujours possible, car certains services ne renvoient pas de bannières, ou renvoient des erreurs.
