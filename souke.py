import streamlit as st
st.set_page_config(page_title="سوق سوس ماسة", page_icon="🛍️")
st.title("🛍️ سوق سوس ماسة")
try:
    NUMERO_ORANGE = st.secrets["NUMERO_Orange"]
    CODE_ADMIN = st.secrets["CODE_ADMIN"]
except:
    NUMERO_ORANGE = "0631943706"
    CODE_ADMIN = "fati246"
if "produits" not in st.session_state:
    st.session_state.produits = []
if "en_attente" not in st.session_state:
    st.session_state.en_attente = []
params = st.query_params
is_admin = params.get("admin") == "1"
if is_admin:
    st.title("🔒 لوحة الإدارة")
    mot = st.text_input("دخلي الكود السري", type="password")
    if mot == CODE_ADMIN:
        st.success("مرحبا مولات السوق!")
        st.write(f"عندك {len(st.session_state.en_attente)} طلبات في الانتظار")
        for i, p in enumerate(st.session_state.en_attente):
            st.image(p["image"], width=250, caption="تصويرة المنتوج")
            st.image(p["preuve"], width=250, caption="تصويرة الخلاص 40 درهم")
            st.write(f"البائع: {p['vendeur']} - {p['tel']} - {p['ville']}")
            st.write(f"المنتوج: {p['produit']} - {p['prix']} درهم")
            st.write(p['desc'])
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"✅ نوافق و ننشر - {p['produit']}", key=f"ok{i}"):
                    st.session_state.produits.append(p)
                    st.session_state.en_attente.pop(i)
                    st.rerun()
            with col2:
                if st.button(f"❌ نرفض - {p['produit']}", key=f"no{i}"):
                    st.session_state.en_attente.pop(i)
                    st.rerun()
            st.write("---")
    elif mot != "":
        st.error("الكود غالط!")
    st.stop()
choix = st.sidebar.radio("القائمة", ["🛍️ السوق", "📦 بيع سلعتك - 40 درهم"])
if choix == "🛍️ السوق":
    st.success("سوق سوس ماسة - البائع كيربح 100%")
    st.write("عرض البداية: 40 درهم للشهر باش تنشر منتوجك")
    if len(st.session_state.produits) == 0:
        st.write("لا توجد منتجات بعد. كن أول من ينشر!")
    else:
        for p in st.session_state.produits:
            if p.get("image") is not None:
                st.image(p["image"], width=300)
            st.write(f"### {p['produit']} - {p['prix']} درهم")
            st.write(f"البائع: {p['vendeur']} | المدينة: {p['ville']} | 📱 {p['tel']}")
            st.write(p['desc'])
            st.write("---")
else:
    st.title("بيع سلعتك - 40 درهم للشهر")
    st.info(f"1. صيفط 40 درهم لـ Orange Money: {NUMERO_ORANGE} - 2. عمر الاستمارة و حط التصويرة ديال السلعة + تصويرة التحويل - 3. ملي نتأكدو من الخلاص، غادي ننشرو ليك سلعتك")
    nom = st.text_input("سميتك")
    tel = st.text_input("نمرة التيليفون ديالك")
    ville = st.text_input("مدينتك")
    produit = st.text_input("سميت المنتوج")
    prix = st.number_input("الثمن بالدرهم", value=100)
    desc = st.text_area("وصف المنتوج")
    photo = st.file_uploader("تصويرة المنتوج", type=["jpg","png","jpeg"])
    preuve = st.file_uploader("تصويرة التحويل ديال 40 درهم - Orange Money", type=["jpg","png","jpeg"])
    if photo:
        st.image(photo, width=200)
    if preuve:
        st.image(preuve, width=200)
    if st.button("صيفط الطلب"):
        if nom and tel and produit and photo and preuve:
            st.session_state.en_attente.append({"vendeur": nom, "tel": tel, "ville": ville, "produit": produit, "prix": prix, "desc": desc, "image": photo, "preuve": preuve})
            st.success("تم! الطلب ديالك وصل. ملي نتأكدو من 40 درهم غادي ننشروه!")
        else:
            st.error("عافاك عمر كلشي و حط التصاور بجوج!")
