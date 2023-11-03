from PIL import Image, ImageDraw, ImageFont

def create_marketing_image(product_image, punchline_text, button_text, punchline_and_button_color):
    # Logo resmini yükle

    width, height = 600, 600


    logo_path = "/Users/furkangulenc/Desktop/addCreativeTask/assets/logo1.jpeg"

    logo = Image.open(logo_path)
    logo = logo.resize((200, 60))

    product_image = product_image.resize((250, 250))

    space_between_logo_and_product = 30
    space_between_product_and_punchline = 50
    space_between_punchline_and_button = 20

    """width = max(logo.width, product_image.width) + 80  # kenarlarda 20px boşluk için
    height = logo.height + product_image.height + space_between_logo_and_product + space_between_product_and_punchline + 100"""

    
    image = Image.new('RGB', (width, height),'white')
    image.paste(logo, ((width - logo.width) // 2, 10)) 
    image.paste(product_image, ((width - product_image.width) // 2, logo.height + space_between_logo_and_product))

    # Metin ve buton ekle
    draw = ImageDraw.Draw(image)
    font_size = 20  # İstediğiniz boyuta ayarlayın
    font = ImageFont.truetype("/Users/furkangulenc/Desktop/addCreativeTask/assets/Natural Precision.ttf", font_size)


    # Punchline metni
    text_width, text_height = draw.textsize(punchline_text, font=font)
    text_y = logo.height + space_between_logo_and_product + product_image.height + space_between_product_and_punchline
    #draw.text(((width - text_width) / 2, text_y), punchline_text, fill=punchline_and_button_color, font=font, align="center")
    draw.multiline_text(((width - 450) / 2, text_y), punchline_text, fill=punchline_and_button_color, font=font, align="center")
    #draw.textlength(punchline_text, font=font, embedded_color=punchline_and_button_color,features=["-kern"])

    # Buton
    font1 = ImageFont.load_default()
    button_y = text_y + text_height + space_between_punchline_and_button
    button_height = 40
    #draw.rectangle([((width - 200) / 2, button_y), ((width + 200) / 2, button_y + button_height)], outline=punchline_and_button_color, fill=punchline_and_button_color)
    draw.rounded_rectangle([(width - 200) // 2, button_y, (width + 200) // 2, button_y + button_height], radius=20, fill=punchline_and_button_color)
    button_text_width, button_text_height = draw.textsize(button_text, font=font1)
    draw.multiline_text(((width - button_text_width) / 2, button_y + (button_height - button_text_height) / 2), button_text, fill="white", font=font1, align="center", stroke_width=60)


    return image