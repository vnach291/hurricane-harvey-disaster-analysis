from flask import Flask, request, jsonify
from PIL import Image
import torch
from transformers import SwinForImageClassification, SwinConfig, AutoImageProcessor
import io

app = Flask(__name__)

# load model
model_path = 'best_swin_model.pth'
config = SwinConfig.from_pretrained('microsoft/swin-tiny-patch4-window7-224', num_labels=2)
model = SwinForImageClassification.from_pretrained('microsoft/swin-tiny-patch4-window7-224', config=config, ignore_mismatched_sizes=True)
model.load_state_dict(torch.load(model_path, map_location='cpu'))
model.eval()

# load processor
processor = AutoImageProcessor.from_pretrained('microsoft/swin-tiny-patch4-window7-224')

@app.route('/summary', methods=['GET'])
def summary():
    return jsonify({'model': 'Best Swin Transformer Model', 'input_shape': '(224, 224, 3)', 'classes': ['no_damage', 'damage']})

@app.route('/inference', methods=['POST'])
def inference():
    file = request.files['image']
    img = Image.open(io.BytesIO(file.read())).resize((224, 224))  # resize to match my model input
    inputs = processor(img, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        pred = outputs.logits.argmax(dim=1).item()
    label = 'damage' if pred == 1 else 'no_damage'
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)