import streamlit as st

# إعدادات الصفحة الأساسية لتتوسط الشاشة
st.set_page_config(page_title="Classification", layout="centered")

# الستايل السحري لتثبيت الألوان والسنترة الكاملة على خط واحد عدل
st.markdown("""
    <style>
    /* جعل الخلفية بيضاء تماماً */
    .stApp {
        background-color: #FDF8FB !important;
    }
    
    /* الحاوية الرئيسية الشاملة لضمان سنترة كل العناصر على خط عمودي واحد */
    .main-canvas {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        margin-top: 40px;
    }
    
    /* تنسيق الكروت الموحد (العرض والارتفاع والحواف) */
    .box-card {
        width: 280px; /* عرض موحد لكل الكروت لتبدو متناسقة جداً */
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        padding: 14px 0;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 25px; /* مسافة عمودية ثابتة بين كل كارت والتاني */
    }
    
    /* كارت ABNORMAL الأساسي (وردي صارخ صلب) */
    .box-abnormal {
        background-color: #C73B8A !important;
        color: #000000 !important;
        border: 3.5px solid #C73B8A !important;
        margin-bottom: 45px; /* مسافة إضافية لفصله عن التصنيفات الفرعية */
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
    
    /* --- إجبار أزرار التحكم السفلي على نفس التصميم الوردي المعتمد --- */
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
        color: #FFFFFF !important;
    }
    
    /* عند الضغط الفعلي */
    div.stButton > button:focus, div.stButton > button:active {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- 1. عرض كروت النتائج متسلسلة عمودياً بالوسط تماماً ---
st.markdown('<div class="main-canvas">', unsafe_allow_html=True)

# كارت الـ ABNORMAL فوق بالوسط
st.markdown('<div class="box-card box-abnormal">ABNORMAL</div>', unsafe_allow_html=True)

# كارت الـ BENIGN تحته مباشرة ومسنتر
st.markdown('<div class="box-card box-benign">BENIGN</div>', unsafe_allow_html=True)

# كارت الـ MALIGNANT بالأسفل ومسنتر تماماً
st.markdown('<div class="box-card box-malignant">MALIGNANT</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# مسافة منسقة قبل أزرار التحكم السفلي
st.write("<br><br>", unsafe_allow_html=True)


# --- 2. أزرار التحكم (Back & Next) متقاربة بالوسط تماماً أسفل الكروت ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.3, 1, 1, 1.3])

with nav_col2:
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.write("")  # الأكشن للعودة
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.write("")  # الأكشن للتالي
    st.markdown('</div>', unsafe_allow_html=True)
