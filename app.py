import streamlit as st
import google.generativeai as genai

# --- YAPILANDIRMA ---
API_KEY = "AIzaSyAxrlrmER5psHMfNGktfZISB3My81eN2ec"
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz (v3.0)", page_icon="⚽", layout="centered")

# Tasarım Modifikasyonları
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #d32f2f; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #b71c1c; color: white; }
    .result-box { padding: 20px; border-radius: 15px; background-color: #1e1e1e; border: 1px solid #d32f2f; color: white; white-space: pre-wrap; font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ Kağan'ın AI Futbol Analiz Merkezi v3.0")
st.write("Gemini 3.0 Flash Motoru ile Profesyonel Maç Analizi")

# --- GİRDİ PANELİ ---
with st.container():
    league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig"])
    match = st.text_input("Maç İsmi Yazın (Örn: Beşiktaş - Rizespor)", "")
    analyze_btn = st.button("Gemini 3.0 ile Analiz Et 🚀")

st.markdown("---")

# --- ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner('Gemini 3.0 Verileri İşliyor...'):
        try:
            # MODEL GÜNCELLEMESİ: gemini-3.0-flash
            model = genai.GenerativeModel('gemini-3.0-flash')
            
            prompt = f"""
            Sen dünyanın en iyi futbol analiz yapay zekasısın. {league} ligindeki {match} maçı için teknik analiz yap.
            
            Lütfen tam olarak şu yapıda cevap ver:
            
            ### 📊 Gemini 3.0 Olasılık Hesapları
            - MS 1-X-2: (Yüzdeleri belirt)
            - 2.5 Alt/Üst: (Yüzde belirt)
            - KG Var/Yok: (Yüzde belirt)
            
            ### 🚑 Kritik Oyuncu ve Sakatlık Analizi
            (Maçtaki en önemli eksikleri ve bu eksiklerin takımların taktiksel gücünü nasıl etkilediğini detaylıca açıkla.)
            
            ### ⚠️ Risk Seviyesi ve Sürpriz Uyarısı
            (Maçın en tehlikeli yanını belirt.)
            
            ### 🎯 Tek Net Tahmin (Master Prediction)
            (Kısa ve net tek bir sonuç önerisi.)
            """
            
            response = model.generate_content(prompt)
            
            # Sonucu göster
            st.markdown(f"### 🏟️ {match} Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
else:
    st.info("Bir maç ismi girin ve analizi başlatın.")

st.caption("Kağan'ın Özel AI Analiz Sistemi - Gemini 3.0 Edition")
