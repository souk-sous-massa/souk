import streamlit as st
st.set_page_config(page_title="سوق سوس ماسة" , page_icon="🛍")
st.title("🛍 سوق سوس ماسة ")
st.write("مرحبا بيكوم فالسوق ديالنا ")
st.header("المنتجات")
col1, col2 = st.columns(2)
with col1:
  st.subheader("زيت اركان")
  st.write("الثمن: 150درهم ")
  st.button("شراء زيت اركان")
  with col2:
    st.subheader("العسل الحر")
    st.write("الثمن:200 درهم")
    st.button("شراء العسل")
    st.write("---")
    st.markdown("---")
    st.subheade("تريد عرض سلعتك هنا ")
    st.write("العرض 40 درهم لمدة شهر ")
    st.write("السلع القديمة تبقى رغم انتهاء الشهر")
    st.write("اذا تريد اضافة سلعة جديدة بعد شهر, يجب اعادة دفع 40درهم")
    st.link_button("راسلنا على الواتساب", "https://wa.me/212631943706")
    st.write("اضغط على الزر و اخبرنا:اريد عرض منتجي") 



