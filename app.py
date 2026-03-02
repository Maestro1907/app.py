import streamlit as st
import google.generativeai as genai

# --- KRİTİK AYAR ---
# Buradaki anahtarı en son aldığın taze anahtarla değiştirdiğinden emin ol!
API_KEY = "AIzaSyAxrlrmER5psHMfNGktfZISB3My81eN2ec"

try:
    genai.configure(api_key=API_KEY)
    # En standart ve en stabil model ismini seçiyoruz
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Kurulum Hatası: {e}")

st.set_page_config(page_title="Kağan'ın AI Analiz", page_icon="⚽")

st.title("⚽ Kağan'ın AI Futbol Analizi")
st.write("Profesyonel Maç Tahmin Motoru")

# Giriş Alanı
match = st.text_input("Maç İsmi (Örn: Beşiktaş - Rizespor)", "")
analyze_btn = st.button("Analiz Et 🚀")

if analyze_btn and match:
    with st.spinner('Analiz yapılıyor...'):
        try:
            # En basit prompt ile testi başlatıyoruz
            prompt = f"{match} maçı için kısa bir sakatlık analizi ve skor tahmini yap."
            response = model.generate_content(prompt)
            
            st.success("Analiz Tamamlandı!")
            st.markdown(f"### 🏟️ {match} Raporu")
            st.write(response.text)
            
        except Exception as e:
            st.error("🚨 HATA DETAYI:")
            st.code(str(e)) # Hatayı tam olarak ekrana basar ki görelim
            st.info("Eğer 'API_KEY_INVALID' yazıyorsa anahtar yanlıştır. '404' yazıyorsa model ismi değişmiştir.")

st.caption("Kağan'ın Özel AI Sistemi")
