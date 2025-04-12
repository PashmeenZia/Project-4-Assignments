import qrcode
import cv2

def generate_qr(text, filename="qrcode.png"):
    """Generate a QR code from the given text and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

def decode_qr(image_path):
    """Decode the QR code from an image and return the data."""
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    data, _, _ = detector.detectAndDecode(img)
    if data:
        print("Decoded Data:", data)
    else:
        print("No QR Code found in the image.")

# Example Usage
if __name__ == "__main__":
    print("1. Generate QR Code")
    print("2. Decode QR Code")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        text = input("Enter text to encode in QR: ")
        generate_qr(text)
    elif choice == "2":
        image_path = input("Enter QR image file path: ")
        decode_qr(image_path)
    else:
        print("Invalid choice! Please enter 1 or 2.")