import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    import seaborn as sns
except ImportError:
    st.error("seaborn 라이브러리가 설치되지 않았습니다. 'pip install seaborn' 명령어로 설치해 주세요.")

# Load the CSV file
@st.cache_data
def load_data():
    file_path = 'age2411.csv'  # Replace with the uploaded file path
    data = pd.read_csv(file_path)
    return data

data = load_data()

# Title and description
st.title("인구 데이터 분석 및 시각화")
st.write("이 애플리케이션은 특정 지역의 인구 데이터를 분석하고 시각화합니다.")

# Display raw data
if st.checkbox("원본 데이터 보기"):
    st.subheader("원본 데이터")
    st.write(data.head())

# 지역 선택 기능
st.sidebar.header("필터 선택")
region_options = data['행정구역'].unique()
selected_region = st.sidebar.selectbox("지역을 선택하세요", region_options)

# 선택한 지역의 데이터 필터링
filtered_data = data[data['행정구역'] == selected_region]

# 인구 분포 시각화 (연령대별 인구수 막대 그래프)
st.subheader(f"{selected_region}의 인구 분포 시각화")

# 연령대별 컬럼만 선택 (2024년11월_계_0세 ~ 2024년11월_계_100세 이상)
age_columns = [col for col in data.columns if '2024년11월_계_' in col]
region_age_data = filtered_data[age_columns].sum()

# 연령대 추출 및 정리
age_labels = [col.replace('2024년11월_계_', '') for col in age_columns]
age_values = region_age_data.values

# 시각화 생성
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=age_labels, y=age_values, palette="viridis", ax=ax)
ax.set_xticklabels(age_labels, rotation=90)
ax.set_title(f"{selected_region}의 연령대별 인구 분포")
ax.set_xlabel("연령대")
ax.set_ylabel("인구수")

st.pyplot(fig)

# 특정 연령대의 인구수 확인 기능
st.sidebar.subheader("특정 연령대의 인구수 확인")
age_range = st.sidebar.slider("연령대 범위 선택", min_value=0, max_value=100, value=(0, 100))

# 연령대에 맞는 컬럼만 선택
age_start, age_end = age_range
age_columns_filtered = [f'2024년11월_계_{i}세' for i in range(age_start, age_end + 1)]

# 선택한 연령대의 인구수 합계 계산
if all(col in filtered_data.columns for col in age_columns_filtered):
    age_population_sum = filtered_data[age_columns_filtered].sum().sum()
    st.write(f"{selected_region}의 {age_start}세부터 {age_end}세까지의 인구수 합계: {age_population_sum}명")
else:
    st.write("선택한 연령대에 대한 데이터가 없습니다.")

# 다운로드 기능
st.sidebar.subheader("데이터 다운로드")
if st.sidebar.button("CSV로 다운로드"):
    filtered_csv = filtered_data.to_csv(index=False).encode('utf-8-sig')
    st.sidebar.download_button(
        label="CSV 다운로드",
        data=filtered_csv,
        file_name=f"{selected_region}_인구데이터.csv",
        mime="text/csv",
    )

st.write("**끝!** 애플리케이션을 이용해 다양한 지역의 인구 분포를 분석해 보세요!")
