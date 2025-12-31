import streamlit as st

from infrastructure.scraping.chrome_scraper import srape_with_chreme
from infrastructure.scraping.brightdata_scraper import scrape_with_brightdata
from infrastructure.scraping.utils import clean_html, split_content

from app.use_case.parsing.ollama_parser import parse_with_ollama
from app.use_case.parsing.openai_parser import parse_with_openai



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Streamlit UI Configuration
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("AI Destekli Web Scraper")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Input: Target URL
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

url = st.text_input("Web sitesinin URL'ini giriniz.")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Select Scraping Method
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

scraper_option = st.selectbox(
    "Hangi scraping yöntemini kullanmak istersiniz.",
    ["Chrome Driver (FREE)", "Bright Data (Professional)"]
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Select LLM Model
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

model_option = st.selectbox(
    "Hangi LLM Modelini Kullanmak istersiniz.",
    ["oLLAMA", "OpenAI"]
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Trigger Scraping
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if st.button("Siteyi tara ve içeriği hazırla."):
    if not url:
        st.warning("Lütfen bir web sitesinin URL'ini giriniz.")
    else:
        with st.spinner("Website scrape ediliyor..."):

            if scraper_option == "Chrome Driver (FREE)":
                raw_html = srape_with_chreme(url=url)
            else:
                raw_html = scrape_with_brightdata(url=url)

            cleaned = clean_html(raw_html)
            st.session_state.cleaned_content = cleaned
            st.success("İçerik başarıyla çekildi ve temizlendi.")

        with st.expander("Temizlenmiş veriyi gör"):
            st.text_area("Cleaned Content", cleaned, height=300)

if "cleaned_content" in st.session_state:
    parse_instructions = st.text_area(
        "Hangi bilgilere bilgilere istiyorsun? (Ürün Başlıkları, e-opsta adresleri vs.)"
    )

    if st.button("AI ile Parse Et"):
        if not parse_instructions:
            st.warning("Lütfen hangi bilgilere erişmek istediğinizi belirtin")
        else:
            chunks = split_content(st.session_state.cleaned_content)

            with st.spinner("LLM ile içerik analiz ediliyor..."):
                if model_option == "oLLAMA":
                    result = parse_with_ollama(chunks=chunks,parse_instructions=parse_instructions)
                else:
                    result = parse_with_openai(chunks=chunks,parse_instructions=parse_instructions)

            st.success("İşlem Tamamlandı")
            st.subheader("Elde edilen bilgi:")
            st.markdown(result, unsafe_allow_html=True)

