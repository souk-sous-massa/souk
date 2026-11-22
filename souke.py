import streamlit as st
import base64
from supabase import create_client
if "en_attente" not in st.session_state:
    st.session_state.en_attente =[ ]
st.set_page_config(page_title="سوق سوس ماسة", page_icon="🛍️")
st.title("🛍️ سوق سوس ماسة")

# --- الربط مع Supabase ---
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except:
    SUPABASE_URL = "https://dyuquatmafabwghlaafb.supabase.co"
    SUPABASE_KEY = "sb_publishable_pUdIHoY7Uwsj3dYRtncaYA_4trTSdEw"

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except:
    supabase = None

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

# جبد الطلبات و المنتجات من Supabase باش كلشي يبقى مسجل
if supabase is not None and len(st.session_state.en_attente) == 0 and len(st.session_state.produits) == 0:
    try:
        res = supabase.table("demandes").select("*").eq("statut", "en_attente").execute()
        for r in res.data:
            st.session_state.en_attente.append({
                "vendeur": r.get("vendeur",""), "tel": r.get("tel",""),
                "ville": r.get("ville",""), "produit": r.get("produit",""),
                "prix": r.get("prix",0), "description": r.get("description",""),
                "image": None, "preuve": None, "id_db": r.get("id")
            })
        res2 = supabase.table("demandes").select("*").eq("statut", "approuve").execute()
        for r in res2.data:
            st.session_state.produits.append({
                "vendeur": r.get("vendeur",""), "tel": r.get("tel",""),
                "ville": r.get("ville",""), "produit": r.get("produit",""),
                "prix": r.get("prix",0), "description": r.get("description",""),
                "image": None, "preuve": None, "id_db": r.get("id")
            })
    except Exception as e:
        pass

params = st.query_params
is_admin = params.get("admin") == "1"

if is_admin:
    st.title("🔒 لوحة الإدارة")
    mot = st.text_input("دخلي الكود السري", type="password")
if mot == CODE_ADMIN:
        st.success("مرحبا مولات السوق!")
        st.write(f"عندك {len(st.session_state.en_attente)} طلبات في الانتظار")
for i, p in enumerate(st.session_state.en_attente):
            photo_b64 = p.get("photo") or p.get("image")
            if p.get("preuve") is not None:
                st.image(p["preuve"], width=250, caption="الايصال")
                vendeur = p.get("vendeur")
                tel = p.get("tel")
                ville = p.get("ville")
                produit = p.get("produit")
                prix = p.get("prix")
                st.write(f"اسم البائع: {vendeur} - الهاتف: {tel} - المدينة: {ville}")
                st.write(f"المنتج: {produit} - {prix} درهم")
                st.write(p.get("description", ""))
                col1, col2 = st.columns(2)
            with col1:
                nom_p = p.get("vendeur", "")
            if st.button(f"توافق و نشر - {nom_p}", key=f"ok_{i}_{p.get('id')}"):
                supabase.table("demandes").update({"statut": "accepte"}).eq("vendeur", p.get("vendeur")).execute()
                del st.session_state.en_attente[i]
                st.success("تم القبول")
                st.rerun()
            with col2:
                vendeur_p = p.get("vendeur", "")
            if st.button(f"ترفض - {vendeur_p}", key=f"no_{i}_{p.get('id')}"):
                supabase.table("demandes").update({"statut": "refuse"}).eq("vendeur", p.get("vendeur")).execute()
                del st.session_state.en_attente[i]
                st.warning("تم الرفض")
                st.rerun()
            st.write("---")    
elif mot != "":
            st.error("الكود غالط!")
st.stop()
option1 = "اعرض منتجاتك -📦40 درهم"
option2 = "🛍️ السوق"
choix = st.sidebar.radio("القائمة الرئيسية", [option1, option2])

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
            st.write(p['description'])
            st.write("---")
else:
    st.title("اعرض منتجاتك - 40 درهم للشهر")
    st.info(f"1. ارسل 40درهم عبر  Orange Money الى : {NUMERO_ORANGE} 2. بعد التاكد من الدفع سيتم نشر منتجك")
    nom = st.text_input("الاسم الكامل")
    tel = st.text_input("رقم الهاتف")
    ville = st.text_input("المدينة")
    produit = st.text_input("اسم المنتج")
    prix = st.number_input("السعر بالدرهم", value=100)
    description = st.text_area("وصف المنتوج")
    photo = st.file_uploader("صورة المنتوج", type=["jpg","png","jpeg"])
    preuve = st.file_uploader("صورة ايصال التحويل 40درهم عبر  - Orange Money", type=["jpg","png","jpeg"])
    if photo:
        st.image(photo, width=200)
    if preuve:
        st.image(preuve, width=200)
    def to_b64(f):
         return "data:image/jpeg;base64," + base64.b64encode(f.getvalue()).decode() if f else None
    if st.button("ارسال الطلب"):
        if nom and tel and produit and photo and preuve:
            new_id = None
            if supabase is not None:
                try:
                    res = supabase.table("demandes").insert({
                        "vendeur": nom, "tel": tel, "ville": ville,
                        "produit": produit, "prix": prix, "description": description,
                        "image": to_b64(photo), "preuve": to_b64(preuve),
                        "statut": "en_attente"
                    }).execute()
                    if res.data: new_id = res.data[0].get("id")
                except Exception as e:
                    st.warning(f"تسجل فالسيت ولكن ما تسجلش ف Supabase: {e}")
            st.success("تم استلام طلبك بنجاح سيتم نشر منتجك بعد التاكد من دفع مبلغ 40 درهم")
        else:
            st.error("يرجى ملء جميع الحقول!")
