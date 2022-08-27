import streamlit as st
import pickle

#load pickle file
loaded_model=pickle.load(open('new_claim.pkl', 'rb'))

#
st.set_page_config(page_title="Claim prediction",layout="centered")


# front end elements of the web page
html_temp = """ 
    <div style ="background-color:gray;padding:10px"> 
    <h1 style ="color:black;text-align:center;">Claim prediction App</h1> 
    </div> 
    """

# display the front end aspect
st.markdown(html_temp, unsafe_allow_html=True)

# following lines create boxes in which user can enter data required to make prediction
age = st.slider("Age", 1,100)
#for sex
sex_display = ('Male','Female')
sex_options = list(range(len(sex_display)))
sex=st.selectbox("Gender",sex_options,format_func=lambda x:sex_display[x])

bmi = st.number_input('bmi')

children = st.selectbox('no. of childern', range(0,15,1))


smoker_display = ('Yes','No')
smoker_options = list(range(len(smoker_display)))
smoker = st.selectbox("Smoking",smoker_options,format_func=lambda x:smoker_display[x])

region_display = ('Northeast','Southwest','southeast','northwest')
region_options = list(range(len(region_display)))
region=st.selectbox("Region",region_options,format_func=lambda x:region_display[x])


if st.button("Predict"):
    pred = str(loaded_model.predict([[age,sex,bmi,children,smoker,region]]))
    st.success("Claim prediction : " + pred)

