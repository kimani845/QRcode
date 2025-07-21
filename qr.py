import qrcode

# # Replace this with your website URL
# qr=qrcode.make(url)
# url = "https://www.lishailabs.com"
# # url = "https://preview--lish-ai-visitor-scribe.lovable.app/"
# # Generate QR code
# qr = qrcode.make(url)

# # Save as image
# qr.save("my_website_qr.png")
# # qr.save("lovable.png")

import qrcode

# Replace this with your website URL
url = "https://preview--lish-ai-visitor-scribe.lovable.app"

# Generate QR code
qr = qrcode.make(url)

# Save as image
qr.save("my_code_qr.png")
