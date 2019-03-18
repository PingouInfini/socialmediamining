Facerecognition
==============

###### 1° Prérequis
  /!\ Activer l'environnement virtualisé facerecognition /!\
    
    
###### 2° Installation 

    pip install cmake
        
Dans Visual Studio Builder, 2ème onglet "Composants individuels",\
descendre dans la section "Compilers, build tools and runtimes" \
et cocher "Outils Visual C++ pour CMake" -> Installer

    pip install face-recognition
    
#### TESTS

##### 1) matching obama picture with google image results :"president"

- get 100 google images results for "president"
    
      pip install google-images-download
      googleimagesdownload -k president -l 100

- launch face recognition; search for obama
      
      face_reco.py