import streamlit as st
import pandas as pd
 
import joblib

model = joblib.load('model.pkl')
st.title("GVHD prediction")

st.image('bloodstemcell.jpg', use_column_width=True)  # Replace "path_to_your_image.jpg" with the actual path to your image
st.header("User Input")

# Define input fields for the variables you provided
st.subheader("User Input Variables")

# Define input fields in the main content area
ABOmatch = st.radio("ABOmatch (Compatibility of donor and recipient according to ABO blood group - Matched: 1, Mismatched: 0)", [1, 0])
Gendermatch = st.radio("Gendermatch (Compatibility of donor and recipient according to gender - Female to Male: 1, Other: 0)", [1, 0])
HLAmatch = st.selectbox("HLAmatch (Compatibility of antigens of the main histocompatibility complex of the donor and the recipient according to ALL international BFM SCT 2008 criteria)", [0, 1, 2, 3])
HLAmismatch = st.radio("HLAmismatch (HLA matched: 0, HLA mismatched: 1)", [0, 1])
Recipientgender = st.radio("Recipientgender (Male - 1, Female - 0)", [1, 0])
Stemcellsource = st.radio("Stemcellsource (Peripheral blood - 1, Bone marrow - 0)", [1, 0])
Riskgroup = st.radio("Riskgroup (High risk: 1, Low risk: 0)", [1, 0])
DonorABO = st.selectbox("DonorABO (ABO blood group of the donor of hematopoietic stem cells)", [0, 1, -1, 2])
RecipientABO = st.selectbox("RecipientABO (ABO blood group of the recipient of hematopoietic stem cells)", [0, 1, -1, 2])
RecipientRh = st.radio("RecipientRh (Presence of the Rh factor on recipient's red blood cells - '+': 1, '-': 0)", [1, 0])
CMVstatus = st.selectbox("CMVstatus (Serological compatibility of donor and recipient according to cytomegalovirus)", [0, 3])
DonorCMV = st.radio("DonorCMV (Presence of cytomegalovirus infection in the donor of hematopoietic stem cells prior to transplantation - Present: 1, Absent: 0)", [1, 0])
RecipientCMV = st.radio("RecipientCMV (Presence of cytomegalovirus infection in the donor of hematopoietic stem cells prior to transplantation - Presence: 1, Absence: 0)", [1, 0])
Diseasegroup = st.radio("Diseasegroup (Type of disease - Malignant: 1, Nonmalignant: 0)", [1, 0])
Relapse = st.radio("Relapse (Reoccurrence of the disease - No: 0, Yes: 1)", [0, 1])
Antigen = st.selectbox("Antigen (In how many antigens there is a difference between the donor and the recipient)", [-1, 0, 1, 2, 3])
Allele = st.selectbox("Allele (In how many alleles there is a difference between the donor and the recipient)", [-1, 0, 1, 2, 3])


# Define a function to preprocess user input
def preprocess_user_input(user_input):
    # Create a copy of the user input
    user_input_encoded = user_input.copy()

    # Make sure that categorical columns are of 'category' dtype
    user_input_encoded[categorical_columns] = user_input_encoded[categorical_columns].astype('category')

    # Apply the encoder to the categorical columns


    # Scale the data
    user_input_scaled = user_input_encoded

    return user_input_scaled


# Prediction based on user input
if st.button("Predict"):
    # Prepare user input as a DataFrame
    user_input = pd.DataFrame({
        'ABOmatch': [ABOmatch],
        'Gendermatch': [Gendermatch],
        'HLAmatch': [HLAmatch],
        'HLAmismatch': [HLAmismatch],
        'Recipientgender': [Recipientgender],
        'Stemcellsource': [Stemcellsource],
        'Riskgroup': [Riskgroup],
        'DonorABO': [DonorABO],
        'RecipientABO': [RecipientABO],
        'RecipientRh': [RecipientRh],
        'CMVstatus': [CMVstatus],
        'DonorCMV': [DonorCMV],
        'RecipientCMV': [RecipientCMV],
        'Diseasegroup': [Diseasegroup],
        'Relapse': [Relapse],
        'Antigen': [Antigen],
        'Allele': [Allele],
    })
    categorical_columns = [
    'Recipientgender', 'Stemcellsource','Gendermatch',
    'DonorABO', 'RecipientABO', 'RecipientRh', 'ABOmatch', 'CMVstatus',
    'DonorCMV', 'RecipientCMV','Riskgroup',
    'Diseasegroup', 'HLAmatch', 'HLAmismatch', 'Antigen', 'Allele',
    'Relapse'
]
    user_input[categorical_columns] = user_input[categorical_columns].astype('category')

    # Preprocess user input data
    user_input_scaled = preprocess_user_input(user_input)

    # Make a prediction using your loaded SVM model
    prediction = model.predict(user_input_scaled)

    st.subheader("Prediction")
    st.write("The predicted class for GVHD is:", prediction[0])
    if prediction[0] == 1:
     st.write("The patient is at high risk to develop GVHD.")
    else:
     st.write("The patient is at low risk to develop GVHD.")

#


# Add any additional visualizations, explanations, or details about the model as needed


