import qrcode
import base64
from io import BytesIO
from .models import Announcement, SocialMediaLink, SiteSettings


def qr_code_context(request):
    """
    Context processor that adds QR code, announcements, and social media links to all templates.
    """
    # Fetch site settings
    site_settings = SiteSettings.objects.first()
    qr_data = (
        site_settings.qr_data if site_settings else "https://discord.gg/HFsHgtNpAy"
    )
    instagram_reel_permalink = (
        site_settings.instagram_reel_permalink
        if site_settings
        else "https://www.instagram.com/reel/DGBNoMounZo/?utm_source=ig_embed&utm_campaign=loading"
    )

    # Generate QR code
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

    # Fetch announcements
    announcements = Announcement.objects.all()

    # Fetch social media links
    social_media_links = SocialMediaLink.objects.all()

    return {
        "qr_code": img_str,
        "announcements": announcements,
        "social_media_links": social_media_links,
        "instagram_reel_permalink": instagram_reel_permalink,
    }
