import streamlit as st
st.markdown(" " "
<style>
header  {visibility: hidden; }
footer   {visibility: hidden; }
</style>
" " " , unsafe_allow_html=true)
st.set_page_config(page_title="سوق سوس ماسة" , page_icon="🛍") 
st.write("منتجات بلدية، طبيعية 100% من عند ناس سوس 🌿")
st.write(" مرحبا بيكوم قلبو واختارو لي بغيتو")
st.title("🛍 سوق سوس ماسة ")
st.write("مرحبا بيكوم فالسوق ديالنا ")
#NUMERO_ORANGE = "0631943706"
#CODE_ADMIN = "fati246"
try:
NUMERO_ORANGE = st.secrets["0631943706"]
CODE_ADMIN = st.secrets["fati246"]
except:
NUMERO_ORANGE = "0631943706"
CODE_ADMIN = "fati246"
if "produits" not in st.session_state: 
st.session_state.produits = [ ] 
if "en_attente" not in st.session_state:
st.session_state.en attente = [ ]
params = st.query_params
is_admin = params.get("admin") == "1"
if is_admin:
st.title("لوحة الإدارة🔒")
mot = st.text_input("دخلي الكود السري" ، type= " password ")
if mot == CODE_ADMIN:
st.success("مرحبا مولات السوق ")
st.write(f"عندك طلبات في الإنتظار {len(st.session_state.en_attente)}
for i , p in enumerate(st.session_state.en_attente):
st.image(p["image"] , width=250 , caption =" تصويرة المنتوج ")
st.image(p[" pruve "] , width=250 , caption = "تصويرة الخلاص 40 درهم ")
st.write(f"البائع : {p[ ' vendeur ' ] } - {p[ ' tel ' ] }  -  {p[' ville ' ] } ")
st.write(f"المنتوج : p[ ' produits ' ] }  -  {p[' prix ' ] } درهم ")
st.write (p[ 'desc' ]
st.header("المنتجات")
col1, col2 = st.columns(2)
with col1:
if st.button(f"نوافق و ننشر - p[ ' produits ' ] }" , key=f"ok{ i }"):
st.session_state.produits.append( p )
st.session_state.en_attente.pop( i )
st.rerun( )
st.write("---")
elif mot != "" :
st.error("الكود غالط")
st.stop( )

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
      st.divider()
      st.write("💛شكرا ليكوم ومرحبا بيكوم فأي وقت 💛")
    st.write("---")
    st.markdown("---")
    st.subheader("تريد عرض سلعتك هنا ")
    st.write("العرض 40 درهم لمدة شهر ")
    st.write("السلع القديمة تبقى رغم انتهاء الشهر")
    st.write("اذا تريد اضافة سلعة جديدة بعد شهر, يجب اعادة دفع 40درهم")
    st.link_button("راسلنا على الواتساب", "https://wa.me/212631943706")
    st.write("اضغط على الزر و اخبرنا:اريد عرض منتجي") 



