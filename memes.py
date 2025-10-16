import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import io
import random

def run():
    st.header("🔥 Creative Sports Meme Generator (Offline)")

    uploaded = st.file_uploader("Upload a player image", type=["jpg", "jpeg", "png"])

    if st.button("Generate Meme") and uploaded:
        # Enhance image contrast & brightness
        image = Image.open(uploaded).convert("RGB")
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.3)
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.1)

        draw = ImageDraw.Draw(image)

        # Fun captions with emojis
        captions = [
            "When you realize it's not your day 😅",
            "POV: You just missed the goal 🤦",
            "Epic save incoming! 🧤🔥",
            "Did someone say 'six'? 😎🏏",
            "Coach: 'Focus!' Me: 🤔😴",
            "When VAR ruins your perfect play 😭",
            "Celebration mode ON! 🎉🎊",
            "Goal? Nope. Just another save 😬"
        ]

        # Pick 1-3 captions randomly
        selected_captions = random.sample(captions, k=random.randint(1, 3))

        # Try to use a TTF font, fallback to default
        try:
            font_path = "arial.ttf"
            fonts = [ImageFont.truetype(font_path, max(20, image.width // 15)) for _ in selected_captions]
        except:
            fonts = [ImageFont.load_default() for _ in selected_captions]

        # Function to draw text with outline and background
        def draw_text(draw_obj, position, text, font, fill="yellow", outline="black"):
            x, y = position
            bbox = draw_obj.textbbox((0,0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Draw semi-transparent box
            box_margin = 5
            draw_obj.rectangle(
                [x-box_margin, y-box_margin, x+text_width+box_margin, y+text_height+box_margin],
                fill=(0,0,0,150)
            )

            # Draw outline
            for dx in [-2, -1, 0, 1, 2]:
                for dy in [-2, -1, 0, 1, 2]:
                    draw_obj.text((x+dx, y+dy), text, font=font, fill=outline)
            # Draw main text
            draw_obj.text((x, y), text, font=font, fill=fill)

        # Calculate vertical positions to avoid overlap
        num_captions = len(selected_captions)
        spacing = image.height // (num_captions + 1)
        positions_y = [(i+1)*spacing - 20 for i in range(num_captions)]

        for i, caption in enumerate(selected_captions):
            bbox = draw.textbbox((0,0), caption, font=fonts[i])
            text_width = bbox[2] - bbox[0]
            x = (image.width - text_width) // 2
            y = positions_y[i]
            draw_text(draw, (x, y), caption, fonts[i], fill=random.choice(["yellow","white","lime","cyan","orange"]))

        # Display image
        st.image(image, caption="🔥 Generated Creative Meme", use_container_width=True)

        # Download
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.download_button("Download Meme", data=buf.getvalue(), file_name="creative_meme.png", mime="image/png")
