import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Abnormal Classification Result", layout="centered")

# إضافة الستايل الخاص (CSS) لتوحيد الألوان والمسافات بدقة
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بأكمله إلى الأبيض */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* حاوية مخصصة لتوسط العناصر عمودياً */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 40px;
    }
    
    /* ستايل الكارت الرئيسي بالأعلى ABNORMAL */
    .main-status {
        width: 260px;
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: 3.5px solid #C73B8A !important;
        border-radius: 20px;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding: 12px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.08);
        margin-bottom: 40px; /* مسافة واضحة تحت الكارت الرئيسي */
    }
    
    /* ستايل كروت التصنيف الفرعية (حميد / خبيث) */
    .sub-status {
        width: 220px;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 12px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* كارت BENIGN (خلفية بيضاء وحدود وردية صارخة) */
    .benign-style {
        border: 3.5px solid #C73B8A !important;
        background-color: #FFFFFF !important;
        color: #C73B8A !important;
    }
    
    /* كارت MALIGNANT (خلفية وردية صارخة كاملة) */
    .malignant-style {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: 3.5px solid #C73B8A !important;
    }
    
    /* --- إجبار أزرار التحكم السفلي على اللون الوردي الصارخ ومنع البنفسجي --- */
    div.stButton > button {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 140px !important;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button:hover {
        background-color: #A32D6F !important;
        color: #FFFFFF !important;
    }
    
    div.stButton > button:focus {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- 1. عرض الكارت الرئيسي المرتفع (ABNORMAL) ---
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.markdown('<div class="main-status">ABNORMAL</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- 2. عرض الكارتين الفرعيين متجاورين بمسافة متناسقة لأسفل ---
col_sub1, col_sub2 = st.columns([1, 1])

with col_sub1:
    # محاذاة الكارت لليمين ليقترب من المنتصف
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    st.markdown('<div class="sub-status benign-style">BENIGN</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_sub2:
    # محاذاة الكارت لليسار ليقترب من المنتصف
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    st.markdown('<div class="sub-status malignant-style">MALIGNANT</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# مسافة عزل عمودية ناعمة قبل الأزرار السفلية
st.write("<br><br><br>", unsafe_allow_html=True)


# --- 3. أزرار التحكم (Back و Next) متقاربة باللون الوردي الصارخ بالمنتصف ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.3, 1, 1, 1.3])

with nav_col2:
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.write("") # الأكشن المخصص للرجوع للوراء
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.write("") # الأكشن المخصص للذهاب للواجهة التالية
    st.markdown('</div>', unsafe_allow_html=True)