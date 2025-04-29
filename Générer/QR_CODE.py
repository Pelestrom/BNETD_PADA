import qrcode  # type: ignore

# URL avec niveau de zoom
url = f"http://192.168.137.240:8000/00217P7937/"

# Création de l'objet QRCode
qr = qrcode.QRCode(
    version=1,  # Version du code QR (1 à 40, 1 étant la plus petite)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur (L, M, Q, H)
    box_size=10,  # Taille de chaque pixel dans le code QR
    border=4,  # Marge autour du code QR
)

# Ajout de l'URL au code QR
qr.add_data(url)
qr.make(fit=True)

# Création d'une image du code QR (vous devez avoir installé la bibliothèque Pillow)
img = qr.make_image(fill_color="MidnightBlue", back_color="white")

# Enregistrement de l'image du code QR dans un fichier
img.save("test2_desk.png")
