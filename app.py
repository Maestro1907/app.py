import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- 1. GÜVENLİK VE YAPILANDIRMA ---
# GitHub'a yüklerken anahtarı buraya yazma! 
# Streamlit Cloud'da "Settings > Secrets" kısmına şunu ekle: gemini_api_key = "ANAHTARIN"
try:
    API_KEY = st.secrets["gemini_api_key"]
except:
    # Yerelde (kendi bilgisayarında) çalışırken buraya yazabilirsin:
    API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg"

genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tarihi sistemden otomatik çek (İleri tarihlerde hata yapmaz)
sistem_tarihi = datetime.now().strftime("%d %B %Y")

# Tasarım (CSS)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; font-weight: bold; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #4caf50; color: white; white-space: pre-wrap; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi")
st.info(f"📅 Sistem Tarihi: {sistem_tarihi}")

# --- 2. GİRDİ PANELİ ---
league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig", "Bundesliga", "Şampiyonlar Ligi"])
match = st.text_input("Maç İsmi Yazın (Örn: Brighton - Fulham)", "")
analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

# --- 3. ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner('AI 2026 güncel verilerini internetten tarıyor...'):
        try:
            # KRİTİK: 404 hatasını önleyen en stabil tanımlama
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash',
                tools=[{"google_search_retrieval": {}}] # İNTERNET TARAMASI AKTİF
            )
            
            prompt = f"""
            Sen profesyonel bir futbol analistisin. Bugünün gerçek tarihi: {sistem_tarihi}.
            {league} ligindeki {match} maçı için internetten en güncel (2026) verileri tara. 
            Brighton başında Fabian Hürzeler, Liverpool başında Arne Slot olduğunu doğrula. 
            Eski verileri (De Zerbi dönemi gibi) kesinlikle kullanma.
            
            Analiz Raporu:
            ### 📊 Olasılık Hesaplamaları
            - MS 1-X-2: (Yüzde Tahminleri)
            
            ### 🚑 Güncel Kadro & Teknik Detaylar
            (Takımların başındaki MEVCUT hocayı belirt ve sakatları listele.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Bir sorun oluştu: {e}")
            st.warning("Eğer 404 alıyorsan terminale 'pip install -U google-generativeai' yazmalısın.")
else:
    st.info("Maç ismini girip butona basman yeterli, Kağan.")

st.caption(f"Kağan'ın Özel Sistemi - {sistem_tarihi}")
