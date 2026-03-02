import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- 1. YAPILANDIRMA ---
# Buraya Google AI Studio'dan aldığın YENİ anahtarı koymayı unutma Kağan.
API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg" 
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tarihi her gün otomatik günceller
sistem_tarihi = datetime.now().strftime("%d %B %Y")

# Tasarım (CSS)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; font-weight: bold; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #4caf50; color: white; white-space: pre-wrap; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi")
st.info(f"📅 Bugün: {sistem_tarihi}")

# --- 2. GİRDİ PANELİ ---
league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig", "Bundesliga"])
match = st.text_input("Maç İsmi Yazın (Örn: Brighton - Liverpool)", "")
analyze_btn = st.button("Analizi Başlat ve 2026 Verilerini Tara 🚀")

st.markdown("---")

# --- 3. ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner('AI İnternette güncel kadroları ve hocaları tarıyor...'):
        try:
            # En güncel ve hata vermeyen model tanımı
            model = genai.GenerativeModel(
                model_name='models/gemini-1.5-flash',
                tools=[{"google_search_retrieval": {}}]
            )
            
            prompt = f"""
            Bugünün tarihi {sistem_tarihi}. {league} ligindeki {match} maçı için internetten en güncel haberleri tara. 
            Eski verileri (De Zerbi gibi) kesinlikle kullanma. Brighton hocasının Hürzeler olduğunu unutma.
            
            Lütfen şu yapıda yanıt ver:
            ### 📊 Olasılık Hesaplamaları
            - MS 1-X-2: (Yüzde Tahminleri)
            
            ### 🚑 Güncel Kadro & Sakatlıklar
            (Takımların GÜNCEL hocasını ve eksiklerini belirt.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            # Hata devam ederse burası çalışır
            st.error(f"Hala hata alıyoruz Kağan. Hata mesajı: {e}")
else:
    st.info("Maç ismini girip butona basman yeterli.")

st.caption(f"Kağan'ın Özel AI Sistemi - {sistem_tarihi}")
