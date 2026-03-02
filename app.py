import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- YAPILANDIRMA ---
# NOT: Buraya Google AI Studio'dan aldığın YENİ anahtarı yapıştır.
API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg" 
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# O anki tarihi sistemden otomatik çekiyoruz
sistem_tarihi = datetime.now().strftime("%d %B %Y")

# Tasarım Modifikasyonları (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; font-weight: bold; height: 50px; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #4caf50; color: white; white-space: pre-wrap; font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi")
st.info(f"📅 Sistem Tarihi: {sistem_tarihi}")

# --- GİRDİ PANELİ ---
with st.container():
    league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig", "Şampiyonlar Ligi", "Bundesliga"])
    match = st.text_input("Maç İsmi Yazın (Örn: Brighton - Manchester City)", "")
    analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

# --- ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner(f'{match} için güncel veriler taranıyor...'):
        try:
            # İnternet tarama özellikli Gemini 1.5 Flash modeli
            model = genai.GenerativeModel(
                model_name='models/gemini-1.5-flash',
                tools=[{"google_search_retrieval": {}}]
            )
            
            prompt = f"""
            Sen profesyonel bir futbol analistisin. 
            Bugünün gerçek tarihi: {sistem_tarihi}.
            
            Lütfen {league} ligindeki {match} maçı için internetten EN GÜNCEL (2026) haberleri, 
            sakatlıkları, cezalıları ve teknik direktör bilgilerini tara. 
            
            Analizinde şunları kesinlikle belirt:
            1. Takımların başındaki MEVCUT teknik direktör kim? (Eski bilgileri kullanma).
            2. Sakat veya cezalı kritik oyuncular kimler?
            
            Lütfen şu yapıda cevap ver:
            ### 📊 Olasılık Hesaplamaları ({sistem_tarihi})
            - MS 1-X-2: (Yüzde Tahminleri)
            - 2.5 Alt/Üst: (Tahmin)
            
            ### 🚑 Güncel Kadro & Teknik Detaylar
            (Takımların güncel durumu ve teknik direktör analizi.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Sistem hatası: {e}")
else:
    st.info("Maç ismini girip butona basarak analizi görebilirsin, Kağan.")

st.caption(f"Kağan'ın Özel AI Sistemi - {sistem_tarihi}")
