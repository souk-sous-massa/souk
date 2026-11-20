import streamlit as st
st.set_page_config(page_title="سوق سوس ماسة", page_icon="🛍️")
st.title("🛍️ سوق سوس ماسة")
try:
    NUMERO_ORANGE = st.secrets["NUMERO_ORANGE"]
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
            st.image(p["image"], width=250, caption="صورة المنتوج")
            st.image(p["preuve"], width=250, caption="ايصال الدفع - المبلغ الاجمالي = 40درهم")
            st.write(f"اسم البائع: {p['vendeur']} -الهاتف: {p['tel']} -المدينة: {p['ville']}")
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
choix = st.sidebar.ra("["القائمة الرئيسية, ["🛍️ السوق" , "📦اعرض منتجاتك- 40 درهم")
if choix == "🛍️ السوق":
    st.success("سوق سوس ماسة - يحصل البائع على 100% من الارباح")
    st.write("عرض البداية: 40 درهم للشهر لنشر منتجاتك")
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
    st.title("اعرض منتجاتك - 40 درهم للشهر")
    st.info(f"1. ارسل 40درهم عبر  Orange Moneyالى : {NUMERO_ORANGE} 2. بعد التاكد من الدفع سيتم نشر منتجك")
    nom = st.text_input("الاسم الكامل")
    tel = st.text_input("رقم الهاتف")
    ville = st.text_input("المدينة")
    produit = st.text_input("اسم المنتج")
    prix = st.number_input("السعر بالدرهم", value=100)
    desc = st.text_area("وصف المنتوج")
    photo = st.file_uploader("صورة المنتوج", type=["jpg","png","jpeg"])
    preuve = st.file_uploader("صورة ايصال التحويل 40درهم عبر  - Orange Money", type=["jpg","png","jpeg"])
    if photo:
        st.image(photo, width=200)
    if preuve:
        st.image(preuve, width=200)
    if st.button("ارسال الطلب"):
        if nom and tel and produit and photo and preuve:
            st.session_state.en_attente.append({"vendeur": nom, "tel": tel, "ville": ville, "produit": produit, "prix": prix, "desc": desc, "image": photo, "preuve": preuve})
            st.success("تم استلام طلبك بنجاح سيتم نشر منتجك بعد التاكد من دفع مبلغ 40 درهم")
        else:
            st.error("يرجى ملء جميع الحقول!")
