# Data-Booster 🚀

**Data-Booster** is an open-source Python library for simple and effective **data augmentation** in computer vision and NLP projects. Whether you're working on a prototype or a large-scale AI model, Data-Booster helps you generate diverse datasets and improve your model performance.

---

## 🌟 Features
- **Image Augmentation**: Rotate, crop, flip, adjust brightness, add noise, and more.
- **Text Augmentation**: Synonym replacement, word shuffling, paraphrasing, and more.
- **Framework Integration**: Compatible with TensorFlow, PyTorch, and Keras.
- **Custom Plugins**: Add your own augmentation techniques easily.
- **Scalable and Lightweight**: Works with both small and large datasets.

---

## 🛠 Installation

Install Data-Booster using pip:

```bash
pip install data-booster
```

---

## 🚀 Quick Start

### Example: Image Augmentation

```python
from data_booster.image_augmentor import ImageAugmentor

# Initialize the augmentor
augmentor = ImageAugmentor()

# Apply rotation to an image
augmented_image = augmentor.apply_rotation("input_image.jpg", angle=45)
augmented_image.save("output_image.jpg")
```

---

### Example: Text Augmentation

```python
from data_booster.text_augmentor import TextAugmentor

# Initialize the augmentor
augmentor = TextAugmentor()

# Replace words with synonyms
augmented_text = augmentor.synonym_replacement("This is a great example!")
print(augmented_text)
```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

We welcome contributions! Feel free to:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

---

## 📧 Contact

For any questions, feel free to open an issue or reach out directly!

