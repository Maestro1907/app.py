import streamlit as st
import google.generativeai as genai

# --- YAPILANDIRMA ---
API_KEY = "AIzaSyAxrlrmER5psHMfNGktfZISB3My81eN2ec"
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tasarım Modifikasyonları
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d32f2f; color: white; font-weight: bold; border: none; height: 3em; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #d32f2f; color: white; white-space: pre-wrap; font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi")

# --- GİRDİ PANELİ ---
league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig"])
match = st.text_input("Maç İsmi Yazın", "")
analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

if analyze_btn and match:
    with st.spinner('Sistem Uygun Modeli Arıyor ve Analiz Ediyor...'):
        # Denenecek model isimleri listesi (En yeni nesilden eskiye)
        model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
        success = False
        
        for m_name in model_names:
            try:
                model = genai.GenerativeModel(m_name)
                
                prompt = f"{league} ligindeki {match} maçı için skor tahmini, sakatlık analizi ve % olasılık içeren detaylı bir analiz yap."
                
                response = model.generate_content(prompt)
                
                st.subheader(f"🏟️ {match} Raporu ({m_name})")
                st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
                success = True
                break # Başarılı olursa döngüden çık
            except Exception:
                continue # Hata verirse bir sonraki modeli dene
        
        if not success:
            st.error("Maalesef şu an hiçbir AI modeliyle bağlantı kurulamadı. Lütfen API anahtarınızın aktifliğini Google AI Studio'dan kontrol edin.")

st.caption("Kağan'ın Özel AI Analiz Sistemi")
