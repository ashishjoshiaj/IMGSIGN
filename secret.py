from stegano import lsb

#Define the input image and the output image paths.
input_image_path = "<Input Image Path>"
output_image_path = "<Output Image path>"

#The secret message you want to hide
secret_message = "Hello world"

#Hide the message in the image using LSB steganography
stego_image = lsb.hide(input_image_path, secret_message)
stego_image.save(output_image_path)
print(f"Secret message embedded and saved as {output_image_path}")

#To extract the hidden message:
revealed_message = lsb.reveal(output_image_path)
print("Revealed message:", revealed_message)
