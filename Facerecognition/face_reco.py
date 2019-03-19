import face_recognition
import glob, os, datetime, shutil


    #Le but de ce script est de filtrer les images du répertoire enrichi par google-images-download, et d'enregistrer les valides dans un nouveau répertoire

try:

    #Création d'un nouveau répertoire pour le stockage des futures images, avec date pour éviter les doublons
    candidat = "MAGLOIRE"
    current_time = datetime.datetime.now()
    stringified_time = "{}-{}_{}h{}".format(current_time.day, current_time.month, current_time.hour, current_time.minute)

    path = os.getcwd()
    new_dir = "{}/{}_{}".format(path, candidat, stringified_time)

    os.mkdir(new_dir)

    #Chemin de l'image de référence
    ref_image = face_recognition.load_image_file("jpp.jpg")

    list_of_unknown_image = []
    list_of_unknown_face_encoding = []

    ref_encoding = face_recognition.face_encodings(ref_image)[0]

    known_faces = [
        ref_encoding
    ]

    #Chemin du dossier à parcourir

    os.chdir("C:\Workspace\socialmediamining\Facerecognition\Jean-Pascal")

    at_least_one_true = False
    for file in glob.glob("*.jpg"):

        #La commande ci-dessous ajoute la personne, si elle n'est pas connue à une liste de personnes inconnues
        #list_of_unknown_face_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(file))[0])

        # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
        image = face_recognition.load_image_file(file)
        face_locations = face_recognition.face_locations(image)

        if (len(face_locations) > 0 ):

            results = face_recognition.compare_faces(known_faces, face_recognition.face_encodings(image)[0])

            if results[0] == True:
                shutil.copy2(file, new_dir)
                at_least_one_true = True

        else :
            print("No face was detected on this picture")

    if (at_least_one_true == True) :
        print("The candidate was observed at least on one picture")

        #print("Is the unknown face a picture of Obama? {}".format(results[1]))
        #print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.


except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()



