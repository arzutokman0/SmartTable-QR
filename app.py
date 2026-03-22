import streamlit as st
import time

# Sayfa Yapılandırması
st.set_page_config(page_title="SmartTable QR", page_icon="🍽️")

# 1. DİNAMİK MASA NUMARASI ALMA
# URL sonundaki ?masa=5 kısmını okur. Eğer yoksa 'Genel' kabul eder.
query_params = st.query_params
masa_no = query_params.get("masa", "Bilinmiyor")

st.title(f"🍽️ SmartTable - Masa {masa_no}")

# 2. MENÜ GÖRÜNÜMÜ
st.markdown("---")
st.subheader("🍕 Dijital Menü")
col1, col2 = st.columns(2)
with col1:
    st.info("**Ana Yemekler**\n\n🍔 Burger - 250 TL\n\n🍕 Pizza - 220 TL")
with col2:
    st.info("**İçecekler**\n\n🥤 Kola - 50 TL\n\n☕ Kahve - 60 TL")

# 3. MÜŞTERİ TALEPLERİ (GARSON ÇAĞIRMA)
st.markdown("---")
st.subheader("🛎️ Hizmet Çağır")
c1, c2 = st.columns(2)

if c1.button("🙋‍♂️ Garson Çağır"):
    st.toast(f"Masa {masa_no} garson çağırdı!", icon='🔔')
    # Veriyi geçici bir dosyaya yazıyoruz (Log tutma)
    with open("talepler.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} | Masa: {masa_no} | İşlem: Garson Çağırdı\n")
    st.success("Talebiniz iletildi.")

if c2.button("🧾 Hesap İste"):
    st.toast(f"Masa {masa_no} hesap istedi!", icon='💰')
    with open("talepler.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%H:%M:%S')} | Masa: {masa_no} | İşlem: Hesap İstedi\n")
    st.info("Hesabınız hazırlanıyor.")

# 4. YÖNETİCİ PANELİ (GİZLİ BÖLÜM)
st.markdown("---")
with st.expander("⚙️ Yönetici Paneli (Mutfak/Kasa İçin)"):
    st.write("### 📢 Gelen Son Talepler")
    try:
        with open("talepler.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Son 5 talebi tersten göster
            for line in reversed(lines[-5:]):
                st.text(line.strip())
    except FileNotFoundError:
        st.write("Henüz bir talep gelmedi.")