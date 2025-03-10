# 📌 databooster

**databooster** is a Python package designed for AI developers to automatically analyze and augment datasets when data is scarce. It supports both **image** and **text** augmentation techniques, making it an essential tool for machine learning projects requiring data balancing.

---

## 🚀 Features
- **Automatic Data Analysis**: Checks dataset distribution and identifies class imbalances.
- **Image Augmentation**:
  - Rotation (90°, 180°, 270°)
  - Horizontal & Vertical Flipping
  - Brightness Adjustment
- **Text Augmentation**:
  - Synonym Replacement
  - Random Word Deletion
- **Easy Integration**: Simple API for applying augmentations automatically.

---

## 📦 Installation
```bash
pip install databooster  # (Future release)
```
For now, clone the repository:
```bash
git clone https://github.com/your-username/databooster.git
cd databooster
```

---

## 🛠 Usage

### **1. Import and Initialize**
```python
from databooster import databooster

# Create an instance for image augmentation
augmentor = databooster(dataset_path="path/to/images", mode="image")
```

### **2. Check Dataset Balance**
```python
balance = augmentor.check_data_balance()
print(balance)  # Output: {'class1': 120, 'class2': 80, 'class3': 50}
```

### **3. Apply Augmentation**
#### **For Images**
```python
augmentor.auto_augment()  # Applies augmentation and saves images in the same directory
```

#### **For Text**
```python
augmentor_text = databooster(dataset_path="path/to/text", mode="text")
augmentor_text.auto_augment()
```

---

## 📁 Project Structure
```
databooster/
│── databooster.py  # Main package module
│── utils.py  # Data analysis utilities
│── image_augment.py  # Image augmentation methods
│── text_augment.py  # Text augmentation methods
│── __init__.py
```

---

## 🎯 Roadmap
- [ ] Add advanced augmentation techniques
- [ ] Implement custom augmentation strategies
- [ ] Publish on PyPI
- [ ] Integrate with TensorFlow & PyTorch

---

## 🤝 Contributing
We welcome contributions! Feel free to fork the repository and submit a pull request.

---

## 📜 License
MIT License © 2025 Your Name

---

## 🌟 Show Your Support
If you like **databooster**, consider starring ⭐ the repository!