# --- عرض النتائج بشكل مثلث ---
st.markdown("""
<div style="display:flex; flex-direction:column; align-items:center;">

    <div class="box-card box-abnormal">
        ABNORMAL
    </div>

    <div style="
        display:flex;
        justify-content:space-between;
        width:700px;
        margin-top:20px;
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
