# 🌸 **Iris Flower Classification** 🌸  
**A Machine Learning Web App using Streamlit**  

---

## 📌 **Project Overview**  

This project is a **machine learning web application** that predicts the species of an **Iris flower** based on its **sepal and petal dimensions**. The app is built using **Streamlit** and an **SVM (Support Vector Machine) model** trained on the **Iris dataset**.  

**Key Highlights:**
- **Developed and deployed a machine learning web application** using **Streamlit** to classify **Iris flower species** based on petal and sepal measurements.  
- **Trained and evaluated three models (Random Forest, KNN, SVM)**, selecting **SVM as the final model** after **hyperparameter tuning with GridSearchCV** for optimal performance.  
- **Integrated the best-performing model into a user-friendly web app**, handling real-time inputs and deploying on **Streamlit Cloud** for public access.  

### About Dataset 

The dataset consists of **four features** (attributes) measured from each iris flower:

1. Sepal Length (in centimeters) - The length of the sepal, which is the outer part of the flower that protects the bud.
2. Sepal Width (in centimeters) - The width of the sepal, measured at its broadest point.
3. Petal Length (in centimeters) - The length of the petal, which is the colorful leaf-like part of the flower.
4. Petal Width (in centimeters) - The width of the petal, measured at its widest point.

The dataset contains samples of three different **Iris Species**:

✔️ **Setosa**  
✔️ **Versicolor**  
✔️ **Virginica**  

Each species has 50 samples, resulting in a total of 150 samples.

### 🔥 **Key Features**  
✅ **Simple UI** with Streamlit  
✅ **Trained SVM Model** for accurate predictions  
✅ **Instant Predictions** based on user inputs  
✅ **Easy Deployment** on Streamlit Cloud  

---

## 🚀 **Live Demo**  

🔹 **[Try the Live App](https://iris-flower-classification-priyanshinegi01.streamlit.app/)**

🔹 **Demo Screenshot:**

  ![App Output (Screenshot)](https://github.com/user-attachments/assets/6080f824-9d30-4844-84a6-daee82387a59)


---

## 📂 **Project Structure**  

```
📂 Iris Flower Classification
│-- 📜 app.py              # Streamlit web application
│-- 📜 final_svm_model.pkl # Trained SVM model (saved using Joblib)
│-- 📜 requirements.txt    # Dependencies for deployment
│-- 📜 README.md           # Project documentation
│-- 📜 iris dataset.csv    # Dataset file
```

---

## 🔧 **Installation & Running Locally**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/priyanshi-negi/iris-flower-classification.git
cd iris-flower-classification
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Streamlit App**  
```bash
streamlit run app.py
```

---

## 🛠 **Technologies Used**  
🖥 **Programming Language**: Python  
📊 **Machine Learning**: Support Vector Machine (SVM)  
📦 **Libraries**:
- **NumPy & Pandas** (for data processing)  
- **Scikit-Learn** (for model training)  
- **Joblib** (for model saving)
- **Streamlit** (for UI)  

---

## 🎯 **Future Improvements**  
🔹 **Enhance UI** with better styling  
🔹 **Compare multiple ML models** for better accuracy  
🔹 **Deploy on multiple platforms** (Streamlit Cloud, Hugging Face)  
🔹 **Add Docker support** for easy deployment  

---

## ✨ **Author**  
👩‍💻 **Priyanshi Negi**  
📧 [LinkedIn](https://www.linkedin.com/in/priyanshinegi01)  

🚀 *If you like this project, feel free to ⭐ the repository!* 😊
