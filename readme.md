# Industrial Copper Modelling

<p align="center">
  <img src="https://github.com/user-attachments/assets/6cb09a1c-2905-4475-acd6-646663959ac5" alt="Project WorkFlow" width="790" height="700">
 </p>

**Introduction**

The "Industrial Copper Modeling" project is designed to boost your data analysis and machine learning skills. In the copper industry, handling complex sales and pricing data can be challenging. Our solution uses advanced machine learning techniques to solve these problems. It includes regression models for accurate pricing predictions and classification models for better customer targeting. Through this project, you'll learn about data preprocessing, feature engineering, and web application development using Streamlit, equipping you with the skills to tackle real-world manufacturing issues.

**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Contributing
6. License
7. Contact

**Key Technologies and Skills**
- Python
- Pandas
- Streamlit
- Plotly
- GridSearch CV
- SkLearn
- Pickle
- 
**Installation**

To run this project, you need to install the following packages:

```python
pip install pandas
pip install streamlit
pip install plotly
pip install scikit-learn
pip install xgboost
pip install matplotlib
pip install seaborn
```
**Usage**

To use this project, follow these steps:

1. Clone the repository: ```git clone https://github.com/gopinathvenkatesan01/IndustrialCopperModelling```
3. Run the Streamlit app: ```streamlit run app.py```
4. Access the app in your browser at ```http://localhost:8501```

**Features**

**Data Preprocessing**
- **Data Understanding :** Before embarking on modeling, it's essential to thoroughly comprehend your dataset. Begin by categorizing the variables, distinguishing between continuous and categorical ones, and examining their distributions. Within our dataset, it's important to address potential issues such as 'Material_Ref' values starting with '00000,' which should be converted to null to enhance data integrity.
- **Handling Null Values:** In our dataset, addressing missing values is critical. Depending on the nature of the data and the specific feature, we may opt for imputation methods such as mean, median, or mode to handle these null values effectively.
- **Encoding and Data Type Conversion:** When preparing categorical features for modeling, we utilize ordinal encoding. This method converts categorical values into numerical representations that reflect their inherent order and relationship with the target variable. Additionally, it's crucial to ensure that all data types are appropriately converted to meet the modeling requirements.
- **Skewness - Feature Scaling:** Skewness is a common challenge in datasets. Identifying skewness in the data is essential, and appropriate data transformations must be applied to mitigate it. One widely-used method is the log transformation, which is particularly effective in addressing high skewness in continuous variables. This transformation helps achieve a more balanced and normally-distributed dataset, which is often a prerequisite for many machine learning algorithms.
- **Outliers Handling:** Outliers have the potential to greatly influence model accuracy. To address outliers in our dataset, we employ the Interquartile Range (IQR) method. This approach entails identifying data points that lie outside the boundaries defined by the IQR and subsequently adjusting them to values that better align with the majority of the data. By applying this technique, we aim to enhance the robustness and reliability of our model predictions.
- **Wrong Date Handling:** When encountering cases where delivery dates precede item dates in our dataset, we address this issue by calculating the time difference between them. This difference is then utilized to train a Random Forest Regressor model, allowing us to predict the corrected delivery date accurately. By implementing this approach, we ensure that our dataset maintains both integrity and accuracy, facilitating more reliable predictions in our analyses.


**Classification**
- **Success and Failure Classification**
- **Handled Imbalance Data**
- **Algorithm Selection**
- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**
- **Model Accuracy and Metrics**
- **Model Persistence**
  
**Regression**

- **Handled Imbalance Data**
- **Algorithm Selection**
- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**
- **Model Accuracy and Metrics**
- **Model Persistence**

**Contributing**

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

**License**

This project is licensed under the MIT License. Please review the LICENSE file for more details.

**Contact**

📧 Email: gopinathvenakatesan01@gmail.com

🌐 LinkedIn: [linkedin.com/in/gopinath-venkatesan-9707022a7](https://www.linkedin.com/in/gopinath-venkatesan-9707022a7/)

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
