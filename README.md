# Network Intrusion Detection

A mini project to classify network traffic as **normal** or **potential threat** using a machine learning model trained on the UNSW-NB15 dataset.

## 🔍 Project Overview

This web application allows users to upload a `.csv` file containing network traffic records. 
The app processes the input, performs categorical encoding, and uses a pre-trained `RandomForestClassifier` to predict whether the packets represent normal traffic or a potential intrusion.

### Features
- Upload and classify network traffic via CSV
- Preprocessing includes encoding and feature alignment
- Outputs count of normal vs. threat traffic
- Built with Flask, pandas, scikit-learn

## 🧠 Model Info
- Model: `RandomForestClassifier`
- Training Data: UNSW-NB15 (open-source dataset for intrusion detection)
    - https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
- Features Used: 42 selected features from the dataset
- Labels: Binary classification (0 = Normal, 1 = Threat)

## ⚙️ How to Run

1. Clone this repo:
    ```bash
    git clone https://github.com/hemadri-labs/network-intrusion-detector.git
    cd network-intrusion-detector
    ```

2. Install requirements:
    ```bash
    pip install -r setup.txt
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

## 📁 Project Structure

── UNSW_NB15_training-set.csv  ← must be downloaded

── UNSW_NB15_testing-set.csv   ← must be downloaded

## ✅ Example CSV Format

The uploaded CSV should match the training features. 
Extra columns are ignored; missing ones are defaulted to zero.
Testing Set: UNSW_NB15_testing-set.csv

## Acknowledgments
This project was developed as a learning exercise in network intrusion detection using machine learning. 
I used guidance from 🤖 ChatGPT to help me structure the Flask app, data preprocessing steps, model integration, clarify concepts, and debug issues.

Learnings:
- End-to-end ML model deployment
- Handling categorical encodings
- Building user-friendly web interfaces with Flask

---
