from flask import Flask, request, render_template, redirect
import pandas as pd
import joblib
import pickle
import os

app = Flask(__name__)

# Load model and required files
model = joblib.load("network_intrusion_model.pkl")
encoders = joblib.load("label_encoders.pkl")
feature_names = pickle.load(open("feature_names.pkl", "rb"))

def diagnostic_check(original_df, processed_df, preds, encoders):
    print("=== Diagnostic Check ===")
    # Show shape info
    print(f"Original data shape: {original_df.shape}")
    print(f"Processed data shape: {processed_df.shape}")
    
    # Check for -1 in categorical columns indicating unknown encoding
    for col, encoder in encoders.items():
        if col in processed_df.columns:
            unknown_count = (processed_df[col] == -1).sum()
            print(f"Unknown encodings in '{col}': {unknown_count}")
    
    # Sample 5 random rows to compare original input and prediction
    sample_indices = processed_df.sample(5, random_state=42).index
    for idx in sample_indices:
        print(f"\nRow index: {idx}")
        print("Original input:")
        print(original_df.loc[idx])
        print("Processed input:")
        print(processed_df.loc[idx])
        print(f"Predicted label: {preds[idx]}")
        # If you have true label column (e.g., 'label' or 'attack_cat'), print it:
        if 'label' in original_df.columns:
            print(f"Actual label: {original_df.loc[idx]['label']}")
        if 'attack_cat' in original_df.columns:
            print(f"Actual attack category: {original_df.loc[idx]['attack_cat']}")

def preprocess(df):
    df = df.copy()
    # Drop columns not in feature_names
    df = df[[col for col in df.columns if col in feature_names]]

    # Add missing columns with default value 0
    for col in feature_names:
        if col not in df:
            df[col] = 0
    
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = df[col].map(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)

    # Reorder columns to match training order
    df = df[feature_names]
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file)
            processed = preprocess(df)
            preds = model.predict(processed)
            diagnostic_check(df, processed, preds, encoders)
            normal = sum(preds == 0)
            threats = sum(preds == 1)
            result = {
                "total": len(preds),
                "normal": int(normal),
                "threat": int(threats),
            }

    return render_template("upload.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

