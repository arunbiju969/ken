import qrcode
import base64
from io import BytesIO
from django.shortcuts import render


def index(request):
    # Define the data to encode in the QR code
    qr_data = "https://discord.gg/HFsHgtNpAy"

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a bytes buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    context = {"qr_code": img_str}
    return render(request, "homepage/index.html", context)


def sandbox(request):
    return render(request, "homepage/sandbox.html")
