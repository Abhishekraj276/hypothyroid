import pickle
import streamlit as st
import numpy as np

# Load the trained model
with open('hypothyroid_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# --- Streamlit UI ---
st.set_page_config(page_title="Hypothyroid Prediction", page_icon="🩺", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
        }
        .title {
            font-size: 35px;
            text-align: center;
            font-weight: bold;
            color: #007bff;
        }
        .subheader {
            font-size: 18px;
            text-align: center;
            color: #666;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            padding: 8px 20px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<p class="title">🔬 AI-based Hypothyroid Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Enter the details below to check for hypothyroid risk.</p>', unsafe_allow_html=True)
st.markdown("---")

# Create layout for user inputs
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("🔢 Age", min_value=1, max_value=100, value=30)
    TSH = st.number_input("📊 TSH Level", value=5.08)
    FTI = st.number_input("📉 FTI", value=110.46)
    TT4 = st.number_input("📈 TT4", value=108.32)
    T3 = st.number_input("🧪 T3", value=2.01)
    TSH_measured = st.selectbox("🩸 TSH Measured?", [0, 1])
    on_thyroxine = st.selectbox("💊 On Thyroxine?", [0, 1])

with col2:
    T3_measured = st.selectbox("🧬 T3 Measured?", [0, 1])
    sick = st.selectbox("🤒 Sick?", [0, 1])
    T4U = st.number_input("📏 T4U", value=0.99)
    TT4_measured = st.selectbox("📋 TT4 Measured?", [0, 1])
    on_antithyroid_medication = st.selectbox("💉 On Antithyroid Medication?", [0, 1])
    goitre = st.selectbox("🦠 Goitre?", [0, 1])
    thyroid_surgery = st.selectbox("🔪 Thyroid Surgery?", [0, 1])

with col3:
    query_hypothyroid = st.selectbox("❓ Query Hypothyroid?", [0, 1])
    pregnant = st.selectbox("🤰 Pregnant?", [0, 1])
    lithium = st.selectbox("🧴 Lithium?", [0, 1])
    psych = st.selectbox("🧠 Psychological Issues?", [0, 1])
    T4U_measured = st.selectbox("📏 T4U Measured?", [0, 1])
    hypopituitary = st.selectbox("🩺 Hypopituitary?", [0, 1])

# Prediction button
if st.button("🔍 Predict Now"):
    input_data = np.array([age, TSH, FTI, TT4, T3, TSH_measured, on_thyroxine, T3_measured, sick, T4U,
                           TT4_measured, on_antithyroid_medication, goitre, thyroid_surgery, query_hypothyroid,
                           pregnant, lithium, psych, T4U_measured, hypopituitary]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == "N":
        st.success("✅ No Hypothyroid (Negative) - Your thyroid function is normal.")
    else:
        st.error("⚠️ Hypothyroid Positive - Please consult a doctor.")

        # Detailed explanation for Hypothyroidism
        st.markdown(
            """
            ### ℹ️ **What is Hypothyroidism?**
            Hypothyroidism occurs when the thyroid gland does not produce enough hormones, leading to slow metabolism.

            ### 🔍 **Possible Symptoms:**
            - Fatigue & Weakness  
            - Weight Gain  
            - Cold Sensitivity  
            - Dry Skin & Hair Loss  
            - Depression & Mood Changes  
            - Slow Heart Rate  

            ### 🏥 **What You Should Do?**
            - Consult an **Endocrinologist**  
            - Get a **TSH & T4 Blood Test**  
            - Follow a **Healthy Diet** with iodine & selenium  
            - Consider **Medication (Levothyroxine)**
            """,
            unsafe_allow_html=True
        )
