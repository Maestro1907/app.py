import streamlit as st
import google.generativeai as genai
from datetime import datetime  # <-- Tarihi otomatik çekmek için ekledik

# --- YAPILANDIRMA ---
API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg" 
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# O anki tarihi sistemden çekiyoruz (Örn: 2026-03-02)
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
st.info(f"📅 Sistem Tarihi: {sistem_tarihi} - Analizler bu tarihe göre güncellenir.")

# --- GİRDİ PANELİ ---
with st.container():
    league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig", "Şampiyonlar Ligi", "Bundesliga"])
    match = st.text_input("Maç İsmi Yazın", "")
    analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

# --- ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner(f'{match} için internet verileri taranıyor...'):
        try:
            # İnternet erişimi yetkisi verilmiş model
            model = genai.GenerativeModel(
                model_name='models/gemini-1.5-flash',
                tools=[{"google_search_retrieval": {}}]
            )
            
            # PROMPT: Tarihi sistemden otomatik alıyoruz
            prompt = f"""
            Sen profesyonel bir futbol analistisin. 
            Bugünün gerçek tarihi: {sistem_tarihi}.
            
            Lütfen {league} ligindeki {match} maçı için internetten en güncel (bugüne ait) haberleri, 
            sakatlıkları, cezalıları ve teknik direktör bilgilerini tara. 
            
            Lütfen şu yapıda cevap ver:
            ### 📊 Olasılık Hesaplamaları ({sistem_tarihi})
            - MS 1-X-2: (İnternet verilerine dayalı yüzdeler)
            - 2.5 Alt/Üst & KG: (Tahminler)
            
            ### 🚑 Güncel Kadro & Teknik Detaylar
            (Takımların başındaki mevcut teknik direktörü belirt. Eksik oyuncuların etkisini açıkla.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net bir sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Hata: {e}")
else:
    st.info("Maç ismini girip butona basarak anal
