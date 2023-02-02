# pyvhr_v2

Depuis le dossier racine, lancer : python -m main.py video_filename video_extension

Exemple : python -m main.py face mp4

Le fichier vidéo doit se situer dans le dossier sampleDataset

En premier lieu, pyVHR enregistre la vidéo avec le visage extrait, sous forme de .npz dans le dossier cropped.
Cette opération est longue (~5 minutes pour une durée de 10 secondes).

Ensuite, pyVHR est appliquée sur la vidéo enregistrée dans le dossier cropped, ce qui ne prend pas beaucoup de temps (5~10 secondes).
Une onglet s'ouvre sur le navigateur par défaut avec le graphe iPPG et le graphe est enregistré sous forme de .csv dans le dossier csv.

Pour comparer 2 graphes, lancer la commande python compare.py csv_filename1 csv_filename2 (sans les extensions).

Pour tout bugs, questions, proposition d'améliorations, il faut absolument m'envoyer un message sur discord ou par mail et je règlerai ça au plus vite. 

- gpoloudenny@gmail.com
- Ayzikin#9079
