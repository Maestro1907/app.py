import streamlit as st
import google.generativeai as genai

# --- YAPILANDIRMA ---
API_KEY = "AIzaSyAxrlrmER5psHMfNGktfZISB3My81eN2ec"
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tasarım Modifikasyonları (Koyu Tema ve Renkler)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #4caf50; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi")
st.write("Premier Lig, La Liga ve Süper Lig için gelişmiş olasılık hesaplama.")

# --- GİRDİ PANELİ ---
with st.container():
    league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig"])
    match = st.text_input("Maç İsmi Yazın (Örn: Real Madrid - Getafe)", "")
    analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

# --- ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner('AI Oyuncu Verilerini ve Sakatlıkları İnceliyor...'):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Sen profesyonel bir futbol analiz uygulamasısın. {league} ligindeki {match} maçı için teknik analiz yap.
            
            Lütfen tam olarak şu yapıda cevap ver:
            
            ### 📊 Olasılık Hesaplamaları
            - **MS 1-X-2:** (Yüzdeleri belirt)
            - **2.5 Alt/Üst:** (Yüzde belirt)
            - **KG Var/Yok:** (Yüzde belirt)
            
            ### 🚑 Oyuncu Bazlı Etki & Sakatlıklar
            (Maçtaki kritik eksikleri ve bunların takımın kazanma ihtimalini nasıl etkilediğini teknik olarak açıkla.)
            
            ### ⚠️ Risk Uyarısı
            (Maçın en sürpriz açık yanını veya bahis riskini belirt.)
            
            ### 🎯 Tek Net Tahmin
            (Kısa ve net tek bir sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            # Sonucu göster
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_stdio=True)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
else:
    st.info("Yukarıdaki kutucuğa bir maç ismi yazıp butona basarak analizi görebilirsin.")

st.caption("Kağan'ın Özel AI Analiz Sistemi - 2026")
