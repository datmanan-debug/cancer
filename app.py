import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="Classification",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp {
    background-color: #FDF8FB;
}

.box-card {
    width: 250px;
    text-align: center;
    padding: 18px 0;
    border-radius: 20px;
    font-size: 22px;
    font-weight: bold;
    margin: auto;
}

.box-abnormal {
    background-color: #C73B8A;
    color: black;
    border: 3px solid #C73B8A;
}

.box-benign {
    background-color: white;
    color: black;
    border: 3px solid #C73B8A;
}

.box-malignant {
    background-color: #C73B8A;
    color: black;
    border: 3px solid #C73B8A;
}

div.stButton > button {
    background-color: #E91E8C !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    width: 140px !important;
    height: 50px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# ================= النتائج =================

st.markdown("<br>", unsafe_allow_html=True)

# ABNORMAL بالنص
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(
        '<div class="box-card box-abnormal">ABNORMAL</div>',
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# BENIGN يسار و MALIGNANT يمين
left, center, right = st.columns([1.5,1,1.5])

with left:
    st.markdown(
        '<div class="box-card box-benign">BENIGN</div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        '<div class="box-card box-malignant">MALIGNANT</div>',
        unsafe_allow_html=True
    )

st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# ================= أزرار التنقل =================

c1, c2, c3, c4 = st.columns([1.2,1,1,1.2])

with c2:
    st.button("« Back")

with c3:
    st.button("Next »")
