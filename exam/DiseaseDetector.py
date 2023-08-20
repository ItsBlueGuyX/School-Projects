disease_symptoms = {
    "Cold": ["runny nose", "sneezing", "cough", "fatigue"],
    "Flu": ["fever", "body aches", "cough", "headache"],    
    "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste or smell"],
    "Allergies": ["runny nose", "itchy eyes", "sneezing", "cough"],
    "Asthma": ["shortness of breath", "wheezing", "cough", "chest tightness"],
    "Diabetes": ["frequent urination", "excessive thirst", "weight loss", "fatigue"],
    "Hypertension": ["high blood pressure", "headache", "fatigue", "chest pain"],
    "Migraine": ["severe headache", "nausea", "sensitivity to light", "visual disturbances"],
    "Eye Flu": ["redness of the eyes", "itchy or watery eyes", "discharge from the eyes"],
    "Heart Disease": ["chest pain", "shortness of breath", "fatigue", "dizziness"],
    "Cancer": ["unexplained weight loss", "persistent fatigue", "changes in skin", "lumps or growths"],
    "Chickenpox": ["itchy rash", "fever", "headache", "loss of appetite"],
    "Influenza": ["high fever", "chills", "body aches", "sore throat"],
    "Fever": ["fever", "sweating", "chills", "body aches", "weakness"]
}

#Using manual dataset. As disease dataset found on kaggle unupdated and government doesn't provide one

def calculate_matching_score(user_symptoms, disease_symptoms):
    matched_count = sum(symptom in user_symptoms for symptom in disease_symptoms)
    return matched_count / len(disease_symptoms)

def main():
    print("Welcome to Disease Detector!")
    user_input = input("Enter your symptoms (comma-separated): ").lower()
    user_symptoms = user_input.split(", ")

    disease_predictions = {}
    for disease, symptoms in disease_symptoms.items():
        matching_score = calculate_matching_score(user_symptoms, symptoms)
        disease_predictions[disease] = matching_score

    print("\nDisease predictions:")
    for disease, score in disease_predictions.items():
        print(f"{disease}: {score:.2f}")

    most_likely_disease = max(disease_predictions, key=disease_predictions.get)
    print(f"\nMost likely disease: {most_likely_disease}")

if __name__ == "__main__":
    main()
