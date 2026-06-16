import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="Classification",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>

/* الخلفية */
.stApp {
    background-color: #FDF8FB;
}

/* الكروت */
.box-card {
    width: 280px;
    text-align: center;
    padding: 16px 0;
    border-radius: 20px;
    font-size: 20px;
    font-weight: bold;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* ABNORMAL */
.box-abnormal {
    background-color: #C73B8A;
    color: black;
    border: 3px solid #C73B8A;
}

/* BENIGN */
.box-benign {
    background-color: white;
    color: black;
    border: 3px solid #C73B8A;
}

/* MALIGNANT */
.box-malignant {
    background-color: #C73B8A;
    color: black;
    border: 3px solid #C73B8A;
}

/* الأزرار */
div.stButton > button {
    background-color: #E91E8C !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 12px 40px !important;
    width: 140px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

div.stButton > button:hover {
    background-color: #A32D6F !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================= النتائج =================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex; flex-direction:column; align-items:center;">

    <!-- ABNORMAL بالنص -->
    <div class="box-card box-abnormal">
        ABNORMAL
    </div>

    <!-- BENIGN و MALIGNANT -->
    <div style="
        display:flex;
        justify-content:space-between;
        width:650px;
        margin-top:40px;
    ">

        <div class="box-card box-benign">
            BENIGN
        </div>

        <div class="box-card box-malignant">
            MALIGNANT
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# ================= مسافة =================

st.markdown("<br><br><br>", unsafe_allow_html=True)

# ================= أزرار التنقل =================

col1, col2, col3, col4 = st.columns([1.3, 1, 1, 1.3])

with col2:
    if st.button("« Back"):
        pass

with col3:
    if st.button("Next »"):
        pass
