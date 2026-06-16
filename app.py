import streamlit as st

# إعدادات الصفحة الأساسية لتتوسط الشاشة
st.set_page_config(page_title="Classification", layout="centered")

# الستايل السحري لتوزيع الكروت (واحد فوق بالوسط، واثنين جوه يمين ويسار) باللون الوردي
st.markdown("""
    <style>
    /* جعل الخلفية بيضاء تماماً */
    .stApp {
        background-color: #FDF8FB !important;
    }
    
    /* حاوية مخصصة لضمان توسط كارت ABNORMAL بالوسط تماماً */
    .top-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 40px;
        margin-bottom: 40px; /* مسافة واضحة تفصله عن الصف السفلي */
    }
    
    /* تنسيق كارت ABNORMAL الرئيسي */
    .box-abnormal {
        width: 260px;
        background-color: #C73B8A !important;
        color: #000000 !important;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        padding: 15px 0;
        border-radius: 20px;
        border: 3.5px solid #C73B8A !important;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    }
    
    /* التنسيق الأساسي للكروت الفرعية السفلية */
    .box-sub {
        width: 210px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 14px 0;
        border-radius: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    /* كارت BENIGN اللي راح يصير على اليسار (حدود وردية وخلفية بيضاء) */
    .box-benign {
        border: 3.5px solid #C73B8A !important;
        background-color: #FDF8FB !important;
        color: #000000 !important;
    }
    
    /* كارت MALIGNANT اللي راح يصير على اليمين (وردي صارخ صلب كامل) */
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


# --- 1. عرض كارت ABNORMAL فوق بالوسط تماماً ---
st.markdown('<div class="top-container">', unsafe_allow_html=True)
st.markdown('<div class="box-abnormal">ABNORMAL</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- 2. عرض الصف السفلي: BENIGN على اليسار و MALIGNANT على اليمين متناظرين ---
# استخدمنا 3 أعمدة (العمود الوسطي فارغ ليعمل كـ مسافة عادلة بين اليمين واليسار)
col_left, col_space, col_right = st.columns([1, 0.2, 1])

with col_left:
    # محاذاة لليمين ليقترب الكارت من السنتر بشكل متناسق
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    st.markdown('<div class="box-sub box-benign">BENIGN</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # محاذاة لليسار ليقترب الكارت من السنتر بشكل متناسق
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    st.markdown('<div class="box-sub box-malignant">MALIGNANT</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# مسافة منسقة ومريحة للعين قبل أزرار التحكم السفلية
st.write("<br><br><br>", unsafe_allow_html=True)


# --- 3. أزرار التحكم (Back & Next) متقاربة بالوسط تماماً بالأسفل ---
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
    import streamlit as st

# إعدادات الصفحة الأساسية لتتوسط الشاشة
st.set_page_config(page_title="Classification", layout="centered")

# الستايل النهائي لضبط السنترة الهندسية المتوازنة تماماً
st.markdown("""
    <style>
    /* جعل الخلفية بيضاء تماماً */
    .stApp {
        background-color: #FDF8FB !important;
    }
    
    /* حاوية لتوسط كارت ABNORMAL بالوسط الحقيقي */
    .top-block {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 40px;
        margin-bottom: 30px;
    }
    
    /* كارت ABNORMAL الرئيسي */
    .box-abnormal {
        width: 260px;
        background-color: #C73B8A !important;
        color: #000000 !important;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        padding: 15px 0;
        border-radius: 20px;
        border: 3.5px solid #C73B8A !important;
        box-shadow: 0px 4px
