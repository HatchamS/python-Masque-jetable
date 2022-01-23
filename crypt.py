import os
from random import randint
import sys


def key(rang):
    for _ in range(rang):
        yield randint(1, 255)


def main():
    sys.stdout.write("Veuillez donner le nom du fichier à chiffrer" + "\n")
    file_to_crypt = sys.stdin.readline().replace("\n", "")
    try:
        binary_file_to_crypt = open(file_to_crypt, "rb")
    except:
        sys.stdout.write("Impossible de trouver le fichier spécifier en entrée" + "\n")
    else:
        sys.stdout.write("Veuillez donner le nom du fichier de sortie chiffré" + "\n")
        file_to_crypt_out = sys.stdin.readline().replace("\n", "")
        with open(file_to_crypt_out, "wb") as binary_file_to_crypt_out:
            with open("masque_jetable.txt", "wb") as secret_key:
                taille_fichier_to_crypt = os.stat(file_to_crypt).st_size

                for random_octet in key(taille_fichier_to_crypt):
                    octet_to_encrypt = ord(binary_file_to_crypt.read(1))
                    secret_key.write(bytes(str(random_octet) + " ", 'utf-8'))
                    binary_file_to_crypt_out.write(bytes([random_octet ^ octet_to_encrypt]))

                binary_file_to_crypt.close()
        sys.stdout.write("Programme terminé" + "\n")


main()
