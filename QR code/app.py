import streamlit as st
import qrcode
from PIL import Image
import cv2

# Function to generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Function to decode QR code
def decode_qr_code(image):
    if image is None:
        st.error("Failed to read the uploaded image.")
        return None

    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return data

# Streamlit UI
def main():
    st.title("QR Code Encoder/Decoder")
    st.sidebar.title("Encoder")

    # Encoder
    encode_data = st.sidebar.text_input("Enter data to encode:")
    if st.sidebar.button("Generate QR Code"):
        if encode_data:
            qr_img = generate_qr_code(encode_data)
            st.image(qr_img, caption="QR Code", use_column_width=True)
        else:
            st.warning("Please enter data to encode.")

    # Decoder
    st.subheader("Decoder")
    uploaded_file = st.file_uploader("Upload an image containing QR code:", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        decoded_data = decode_qr_code(cv2.cvtColor(cv2.imread(uploaded_file.name), cv2.COLOR_BGR2RGB))
        if decoded_data:
            st.success("QR Code Decoded Successfully!")
            st.write("Decoded Data:", decoded_data)
        else:
            st.warning("No QR Code detected in the image.")

if __name__ == "__main__":
    main()
