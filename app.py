import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- YAPILANDIRMA ---
# ÖNEMLİ: Eğer anahtarın hala hata veriyorsa AI Studio'dan "v1" anahtarı aldığından emin ol.
API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg" 
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tarihi sistemden otomatik alıyoruz
sistem_tarihi = datetime.now().strftime("%d %B %Y")

# Tasarım (CSS)
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
    with st.spinner(f'{match} için veriler taranıyor...'):
        try:
            # --- KRİTİK DÜZELTME BÖLGESİ ---
            # 404 hatasını aşmak için model ismini doğrudan 'gemini-1.5-flash' (slash olmadan) 
            # veya 'models/gemini-1.5-flash-latest' olarak denemeliyiz.
            # En güncel SDK'lar için 'gemini-1.5-flash' yeterlidir.
            
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash', # Başına models/ koymadan dene
                tools=[{"google_search_retrieval": {}}]
            )
            
            prompt = f"""
            Sen profesyonel bir futbol analistisin. Bugünün gerçek tarihi: {sistem_tarihi}.
            {league} ligindeki {match} maçı için internetten en güncel (2026) verileri tara. 
            
            Özellikle:
            - Teknik direktörlerin ve sakat oyuncuların GÜNCEL olduğundan emin ol.
            - Brighton başında Fabian Hürzeler, Liverpool başında Arne Slot gibi 2026 güncel bilgilerini kullan.
            
            ### 📊 Olasılık Hesaplamaları
            - MS 1-X-2: (Yüzde Tahminleri)
            - 2.5 Alt/Üst: (Tahmin)
            
            ### 🚑 Güncel Kadro & Teknik Detaylar
            (Eksik oyuncu analizi ve güncel hoca bilgisi.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            # Eğer hala hata verirse, otomatik olarak alternatif isimlendirmeyi denetelim:
            st.error(f"Sistem hatası: {e}")
            st.warning("İpucu: Terminale 'pip install --upgrade google-generativeai' yazarak kütüphaneyi güncellemeyi dene.")
else:
    st.info("Maç ismini girip butona basarak analizi görebilirsin.")

st.caption(f"Kağan'ın Özel AI Sistemi - {sistem_tarihi}")
