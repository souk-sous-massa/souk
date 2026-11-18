import streamlit as st
st.set_page_config(page_title="سوق سوس ماسة" , page_icon="🛍")
st.markdown(">h1 style='text-align: center; color: #E67E22;> 
🌿>مرحبا بيكوم فسوق سوس ماسة<🌿><h1>🌿, unsafe_allow_html=true)
St.markdown("<p style='text-align:centre; font-size: 20px; '>منتجات بلدية، طبيعية 100% من عند ناس سوس 🌿<p>" , unsafe_allow_html=true)
st.markdown("---")
st.title("🛍 سوق سوس ماسة ")
st.write("مرحبا بيكوم فالسوق ديالنا ")
st.header("المنتجات")
col1, col2 = st.columns(2)
with col1:
  st.subheader("زيت اركان")
  st.write("الثمن: 150درهم ")
  if st.button("شراء زيت اركان"):
    st.success("رقم البائع 0612345678")
    st.write("تواصلو معه عبر الواتساب للشراء")
with col2:
    st.subheader("العسل الحر")
    st.write("الثمن:200 درهم")
    if st.button("شراء العسل"):
      st.success("رقم البائع  0612345678")
      st.write("تواصلو معه عبر الواتساب")
      st.markdown("<p style= 'text-align:centre;'>💛شكرا ليكوم ومرحبا بيكوم فأي وقت 💛</p>", unsafe_allow_html=true)
    st.write("---")
    st.markdown("---")
    st.subheader("تريد عرض سلعتك هنا ")
    st.write("العرض 40 درهم لمدة شهر ")
    st.write("السلع القديمة تبقى رغم انتهاء الشهر")
    st.write("اذا تريد اضافة سلعة جديدة بعد شهر, يجب اعادة دفع 40درهم")
    st.link_button("راسلنا على الواتساب", "https://wa.me/212631943706")
    st.write("اضغط على الزر و اخبرنا:اريد عرض منتجي") 



