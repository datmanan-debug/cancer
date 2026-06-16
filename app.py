import streamlit as st

# إعدادات الصفحة الأساسية لتتوسط الشاشة
st.set_page_config(page_title="Classification", layout="centered")

# الستايل السحري والإجباري لكسر أي لون بنفسجي وتثبيت الدرجة الوردية الصارخة مالتك
st.markdown("""
    <style>
    /* جعل الخلفية بيضاء تماماً */
    .stApp {
        background-color: #FDF8FB !important;
    }
    
    /* حاوية مخصصة لضمان التوسط الحقيقي والكامل لـ ABNORMAL في السنتر */
    .hierarchy-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        margin-top: 40px;
    }
    
    /* الكارت العلوي الرئيسي ABNORMAL بالوسط تماماً */
    .box-abnormal {
        width: 250px;
        background-color: #C73B8A !important;
        color: #000000 !important;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        padding: 15px 0;
        border-radius: 20px;
        border: 3.5px solid #C73B8A !important;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin: 0 auto 40px auto; /* الحواف التلقائية تضمن السنترة الكاملة */
    }
    
    /* الكروت الفرعية بالأسفل */
    .box-sub {
        width: 200px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 12px 0;
        border-radius: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    /* كارت BENIGN (حدود وردية وخلفية بيضاء) */
    .box-benign {
        border: 3.5px solid #C73B8A !important;
        background-color: #FDF8FB !important;
        color: #000000 !important;
    }
    
    /* كارت MALIGNANT (وردي صارخ صلب كامل) */
    .box-malignant {
        background-color: #C73B8A !important;
        color: #000000 !important;
        border: 3.5px solid #C73B8A !important;
    }
    
    /* --- إجبار أزرار Streamlit (Back & Next) على اللون الوردي الموحد وطرد البنفسجي --- */
    div.stButton > button {
        background-color: #E91E8C !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 140px !important;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    /* عند تمرير الماوس */
    div.stButton > button:hover {
        background-color: #A32D6F !important;
        color: #AD1457 !important;
    }
    
    /* عند الضغط الفعلي لإلغاء الوميض البنفسجي */
    div.stButton > button:focus, div.stButton > button:active {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- 1. بناء الهيكل الهرمي المرتب (العنصر الرئيسي بالوسط تماماً) ---
st.markdown('<div class="hierarchy-container">', unsafe_allow_html=True)
st.markdown('<div class="box-abnormal">ABNORMAL</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- 2. صف العناصر الفرعية (BENIGN و MALIGNANT) متباعدين بشكل متناظر حول السنتر ---
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown('<div style="display: flex; justify-content: flex-end; padding-right: 30px;">', unsafe_allow_html=True)
    st.markdown('<div class="box-sub box-benign">BENIGN</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div style="display: flex; justify-content: flex-start; padding-left: 30px;">', unsafe_allow_html=True)
    st.markdown('<div class="box-sub box-malignant">MALIGNANT</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# مسافة منسقة قبل أزرار التحكم السفلي
st.write("<br><br><br>", unsafe_allow_html=True)


# --- 3. أزرار التحكم المتقاربة باللون الوردي الصارخ في المنتصف السفلي ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.3, 1, 1, 1.3])

with nav_col2:
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.write("")  # الأكشن للعودة للوراء
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.write("")  # الأكشن للذهاب للواجهة التالية
    st.markdown('</div>', unsafe_allow_html=True)
