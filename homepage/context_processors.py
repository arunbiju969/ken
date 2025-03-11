import qrcode
import base64
from io import BytesIO


def qr_code_context(request):
    """
    Context processor that adds QR code to all templates.
    """
    qr_data = "https://discord.gg/HFsHgtNpAy"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image to a bytes buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return {"qr_code": img_str}
