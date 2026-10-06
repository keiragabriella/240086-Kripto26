from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    message = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        message += chr(int(byte, 2))
    return message

def encode_image(image_path, secret_message, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    pixels = encoded.load()

    binary_secret_msg = text_to_binary(secret_message) + '1111111111111110'
    data_index = 0
    msg_len = len(binary_secret_msg)

    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for i in range(3): 
                if data_index < msg_len:
                    pixel[i] = pixel[i] & ~1 | int(binary_secret_msg[data_index])
                    data_index += 1
            pixels[x, y] = tuple(pixel)
            if data_index >= msg_len:
                encoded.save(output_path)
                print("Pesan rahasia berhasil disisipkan pada stego-object!")
                return

def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()

    binary_secret_msg = ""
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for i in range(3):
                binary_secret_msg += str(pixel[i] & 1)

    delimiter = '1111111111111110'
    delimiter_index = binary_secret_msg.find(delimiter)
    if delimiter_index != -1:
        binary_secret_msg = binary_secret_msg[:delimiter_index]
        return binary_to_text(binary_secret_msg)
    else:
        return "Pesan tidak ditemukan."

if __name__ == '__main__':
    print("--- Proses Encode ---")
    encode_image("cover.png", "Halo, ini pesan rahasia dari tugas kripto!", "stego.png")
    
    print("\n--- Proses Decode ---")
    pesan_ditemukan = decode_image("stego.png")
    print("Pesan yang diekstrak:", pesan_ditemukan)