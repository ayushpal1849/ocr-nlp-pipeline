import pytesseract
from ultralytics import YOLO
from utils.preprocessing import preprocess_image
from utils.nlp_parser import extract_key_info
import cv2

class OCREngine:
    def __init__(self):
        # Load a pre-trained YOLO model (using standard 'yolov8n.pt' for demo)
        # In a real project, you would load your custom trained model here
        self.model = YOLO("yolov8n.pt") 
        
        # Set path to Tesseract (Update this path if on Windows)
        # Example for Windows: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' ""

    def process_document(self, image_path):
        """
        Runs the full pipeline: Preprocessing -> Detection -> OCR -> NLP
        """
        
        # Step 1: Object Detection (Simulated for Demo)
        # We run YOLO to detect objects, though for full document extraction
        # we often use the whole image or specific cropped regions.
        results = self.model(image_path)
        
        # (In a real scenario, you would crop the image based on 'results' boxes here)
        
        # Step 2: Preprocessing
        processed_img = preprocess_image(image_path)
        
        # Step 3: OCR (Text Extraction)
        # passing the processed image to Tesseract
        raw_text = pytesseract.image_to_string(processed_img)
        
        # Step 4: NLP Parsing
        structured_data = extract_key_info(raw_text)
        
        return structured_data