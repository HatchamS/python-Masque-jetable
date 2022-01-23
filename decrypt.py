import sys


def main():
    sys.stdout.write("Veuillez donner le nom du fichier à déchiffrer" + "\n")
    file_to_encrypt = sys.stdin.readline().replace("\n", "")
    try:
        binary_file_to_encrypt = open(file_to_encrypt, "rb")
        secret_key = open("masque_jetable.txt", "rb")
    except:
        sys.stdout.write("Impossible de trouver le fichier à déchiffrer ou le masque jetable" + "\n")
    else:
        sys.stdout.write("Veuillez donner le nom de sortie du fichier déchiffré" + "\n")
        fichier_decrypt = sys.stdin.readline().replace("\n", "")
        with open(fichier_decrypt, "wb") as fichier_decrypt_binary:
            liste_octet = tuple(map(int, secret_key.readline().split()))
            for octet in liste_octet:
                octet_to_decrypt = ord(binary_file_to_encrypt.read(1))
                fichier_decrypt_binary.write(bytes([octet_to_decrypt ^ octet]))

            binary_file_to_encrypt.close()
        sys.stdout.write("Programme terminé" + "\n")


main()
