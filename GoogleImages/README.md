Google Images
=============

###### 1° Prérequis
    /!\ activer l'env virtualisé GoogleImages /!\
    pip install google-images-download
###### 2° API
https://github.com/hardikvasa/google-images-download#arguments

###### 3° EXEMPLES
- googleimagesdownload --keywords "Obiwan Kenobi" --limit 10

- googleimagesdownload -k "Jar Jar Binks" -l 5 -e -o myOutputDirectory \
            Les images sont stockées dans "myOutPutDirectory" \
            Le Json généré par -e est stocké dans le répertoire logs