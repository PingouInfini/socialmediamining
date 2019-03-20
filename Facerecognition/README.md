Facerecognition
==============

### 1° Prérequis
  /!\ Activer l'environnement virtualisé facerecognition /!\
    
    
### 2° Installation 

    pip install cmake
        
Dans Visual Studio Builder, 2ème onglet "Composants individuels",\
descendre dans la section "Compilers, build tools and runtimes" \
et cocher "Outils Visual C++ pour CMake" -> Installer

    pip install face-recognition
    
#### USAGE

- Compare l'image <ref_path_image> avec les images dans <source_dir>
- Copie les images qui matchs dans "<candidate_name>_{JJ_M_HHhMM}"
                       
      face_reco.py
    
    
    
#### TESTS

Le but de ce script est de parcourir un dossier d'images et de les comparer avec la photo \
d'un candidat fournie en entrée. Lorsque le candidat est identifié sur une de ces photos, 
la photo est sauvegardée dans un dossier nouvellement créé là où le script vient d'être lancé\
(attention, ce n'est pas dans le dossier du script)

Le fichier "parameters_face_reco.py" comprend trois paramètres nécessaires qu'il faut renseigner : 

-  *candidate_name* : il s'agit du nom du candidat, nécessaire pour nommer le dossier \
 des images filtrées
 
-  *source_dir* : il s'agit du chemin absolu vers le dossier source d'images à filtrer  

-  *ref_path_image* : il s'agit du chemin absolu vers l'image de référence servant de base pour \
la comparaison