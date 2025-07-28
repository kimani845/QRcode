
import qrcode

# Replace this with your website URL
url = "https://docs.google.com/forms/d/e/1FAIpQLSe0Y26rQcz53HGRZ6jMItd1sBG5yGLUGpPY_KsFyPnUIRpP-g/viewform?usp=dialog"

# Generate QR code
qr = qrcode.make(url)

# Convert to RGB for editing
qr=qr.convert("RGB")
# Set up canvas size (QR code size and space title)
qr_width, qr_height=qr.size
title_height= 50
canvas = Image.new("RGB", (qr_width, qr_height + title_height), "white")

# Paste the Qr code to canvas
camvas.paste(qr, (0, title_height))

# Draw the text 
draw = Image.Draw(canvas)
title_text = "📲 Scan Me to Visit"
font_size =24

try: 
    # Try use a TTF font if available
    font = ImageFont.truetype("arial.ttf", font_size)
except: 
    # Default font fallback
    font = ImageFont.load_default()

# Calculate the text postion
text_width, text_height = draw.textsize(title_text, font=font)
text_y = (qr_width - text_width) // 2
text_x = (title_height - text_height) // 2

# Draw the title text 
draw.text((text_x, text_y), title_text, fill="black", font=font)

# Save final image
qr.save("my_code_qr.png")
