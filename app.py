import streamlit as st
import pickle
import numpy as np

# Load the trained KNN model
model_path = 'dudoanbankchurn.pkl'
clf = pickle.load(open(model_path, 'rb'))

# Title of the application
st.title('Dự đoán khách hàng rời bỏ ngân hàng')

# Sidebar for user input
st.sidebar.title('Nhập các thuộc tính khách hàng')

# Number inputs for the features




NumOfProducts = st.sidebar.number_input('số lượng sản phẩm', min_value=0, step=1)
credit_score = st.sidebar.number_input('Điểm tín dụng', min_value=0, max_value=900, value=300, step=1)
age = st.sidebar.number_input('Tuổi', min_value=18, max_value=100, step=1)
balance = st.sidebar.number_input('Số dư tài khoản', min_value=0.0, value=570000.0, step=1000.0, format="%.2f")
estimated_salary = st.sidebar.number_input('Lương ước tính', min_value=0.0, value=12000000.0, step=1000.0, format="%.2f")

# Make predictions
input_data = np.array([[age,credit_score,balance,NumOfProducts,estimated_salary]])
prediction = clf.predict(input_data)

# Display prediction
st.write('## Kết quả dự đoán:')
st.write('Khách hàng sẽ rời bỏ ngân hàng' if prediction[0] == 1 else 'Khách hàng sẽ không rời bỏ ngân hàng')
