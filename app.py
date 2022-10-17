import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Kunal Patil", page_icon=":computer:", layout="wide")
#---- Load lottiefiles function----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS to hide the streamlit menu
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_vnikrcia.json")
lottie_coding2 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_qp1q7mct.json")

# ---- HEADER SECTION ----

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi, I am Kunal :wave:")
        st.title("Data Scientist")
        st.subheader("**Machine Learning & Data Analytics**")
        st.write("In todays era every industry is dependent on data to make firm business decisions, with my skills in data science and analytics. I am ready to work with large volumes of data, apply statistical/ML techniques to help make data informed decisions.")
        st.write("**TECHNICAL STACK**:")
        st.write("""
                  **Data Science/Machine Learning**
                  - Python, Data Visualization, Supervised Learning Algos,
                    Unsupervised Learning Algos, EDA, Feature Engineering,
                    statistics.
                    """)
        st.write("""
                   **Python packages and Frameworks**
                    - Scikit-Learn, Numpy, Pandas, Matplotlib, Seaborn, Streamlit, Jupyter Notebook, Google Colab
                      """)
        st.write("""
                   **Programming Languages**
                    - Python, C/C++, SQL
                      """)
        st.write("""
                   **Other Tools**
                    - Git/Github, Google Sheets
                      """)
        st.write("""
                    **Cloud Deployment**
                    - Heroku
                    """)
        st.write("**EMAIL**:kunalpatil104@gmail.com")
        st.markdown(":link:[**Github**](https://github.com/Kunnalpatil)")
        st.markdown(":person_with_blond_hair:[**Linkedin**](https://www.linkedin.com/in/kunalpatil104)")
     
    with right_column:
         st_lottie(lottie_coding2, height=300, key="DataS")


#------ Eduction-----
with st.container():
    st.write("---")
    left_column, mid_column, right_column = st.columns(3)
    with right_column:
        st.header("Educations")
        st.write("####")
        st.subheader("SSC Education")
        st.write("""
            St. James English High School.
            - with 80.40%
            - completion year 2017
            """)
    with right_column:
         st.subheader("Diploma in computer engineering")
         st.write("""
            Bhausaheb Vartak Polytechnic , Vasai .
            - with 88.74%
            - completion year 2021
            """)
    with mid_column:
         st.header("Experience")
         st.write("####")
         st.subheader("Data Entry Specialist")
         st.write("""
         Ankur pediatric multispeciality hospital LLP
         - Three months
          """)
    with mid_column:
          st.subheader("Floor manager")
          st.write("""
          Ankur pediatric multispeciality hospital LLP
          - six months
           """)
    with mid_column:
          st.subheader("Software Tester")
          st.write("""
         vervali systems pvt ltd
          - Three months
           """)

    #---- Lottie image------
    with left_column:
        st_lottie(lottie_coding1, height=400, key="coding")


st.write("---")

#------Projects-------

st.header("My Projects")
#------Project 1-------
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Data science salary Estimator")
        st.markdown("[Code](https://github.com/Kunnalpatil/Data-science-salary-)")
        st.markdown("[Test Project](https://datascience-salary-estimator.herokuapp.com)")
    with right_column:
        st.write("""
        Created a salary Estimator for data science job roles using data from glassdoor.
        - Engineered features from the text of each job description to quantify the salaries companies put on python, excel, aws, and spark.
        - Optimized Lasso Regession and RandomForestRegressors using RandomsearchCV to reach the best model
        """)

#------Project 2-------
# st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("BlackFriday sales")
        st.markdown("[Code](https://github.com/Kunnalpatil/BlackFriday-sales)")
    with right_column:
        st.write("""
        This project is more about exploring the data and cleaning it for use.
        - Analysed the data and capture insigits.
        - Checking missing values and handeling them.
        - Conclusion of analysis.
        - Model training.
        """)

#------Project 3-------
# st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Car price Estimator")
        st.markdown("[Code](https://github.com/Kunnalpatil/Car_price_Prediction)")
    with right_column:
        st.write("""
        Created a tool that estimates Car price (MAE ~ $ 1334 ) to help car owners to calculate value of their car for selling.
        - Performed EDA and feature enginnering on dataset.
        - Analyzed categorical features which were converted to numerical later.
        - Optimized Random Forest Regressors using RandomsearchCV (Hyperparameters tuning) to reach the best model.
        """)

#------Project 4-------
# st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Machine Learning Projects")
        st.markdown("[Code](https://github.com/Kunnalpatil/ML-Projects)")
    with right_column:
        st.write("""
        These are some other machine learning projects listed on my github
        Do Check them out
        """)
