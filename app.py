import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- YAPILANDIRMA ---
# Buraya Google AI Studio'dan aldığın YENİ anahtarı koy Kağan.
API_KEY = "AIzaSyCOAkFPIQq4v4Scz4I0WyO21CisGlxM2Zg" 
genai.configure(api_key=API_KEY)

# Sayfa Ayarları
st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽", layout="centered")

# Tarih Ayarı
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

# --- GİRDİ PANELİ ---
league = st.selectbox("Lig Seçin", ["Premier Lig", "La Liga", "Trendyol Süper Lig", "Bundesliga"])
match = st.text_input("Maç İsmi Yazın (Örn: Brighton - Fulham)", "")
analyze_btn = st.button("Analizi Başlat 🚀")

st.markdown("---")

# --- ANALİZ MOTORU ---
if analyze_btn and match:
    with st.spinner('AI Güncel Verileri Tarıyor...'):
        try:
            # KRİTİK DEĞİŞİKLİK: 
            # 404 hatasını aşmak için 'models/' ön ekini sildik ve sadece model adını yazdık.
            # Ayrıca internet arama (tools) özelliğini bu model için en kararlı yolla çağırdık.
            
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash', # Sadece ismi kullanıyoruz
                tools=[{"google_search_retrieval": {}}]
            )
            
            prompt = f"""
            Bugünün tarihi {sistem_tarihi}. {league} ligindeki {match} maçı için internetten en güncel (2026) verileri tara. 
            Brighton hocasının Hürzeler olduğunu, Liverpool hocasının Arne Slot olduğunu unutma. 
            Eski verileri (De Zerbi dönemi gibi) kesinlikle kullanma.
            
            Lütfen şu yapıda yanıt ver:
            ### 📊 Olasılık Hesaplamaları
            - MS 1-X-2: (Yüzde Tahminleri)
            
            ### 🚑 Güncel Kadro & Sakatlıklar
            (Takımların GÜNCEL hocasını ve kritik eksikleri belirt.)
            
            ### 🎯 Kağan'ın Net Tahmini
            (Kısa ve net bir sonuç önerisi.)
            """
            
            # Content üretimi
            response = model.generate_content(prompt)
            
            st.markdown(f"### 🏟️ {match} Analiz Raporu")
            st.markdown(f'<div class="result-box">{response.text}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            # EĞER HALA 404 VERİRSE BU ALTERNATİF MODELİ DENER:
            try:
                model_alt = genai.GenerativeModel(model_name='gemini-pro')
                response_alt = model_alt.generate_content(f"{match} maçı için kısa bir analiz yap.")
                st.warning("Flash modelinde sorun çıktı, alternatif modelle (Gemini Pro) yanıt veriliyor.")
                st.markdown(f'<div class="result-box">{response_alt.text}</div>', unsafe_allow_html=True)
            except:
                st.error(f"Hala hata alıyoruz Kağan. Hata mesajı: {e}")
else:
    st.info("Maç ismini girip butona basman yeterli.")

st.caption(f"Kağan'ın Özel AI Sistemi - {sistem_tarihi}")
