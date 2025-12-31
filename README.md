# AI Web Parser

Yapay zeka destekli, web sitelerinden yapılandırılmış veri çıkarmak için geliştirilmiş bir Python aracı. Bu proje, belirtilen bir URL'den web sayfasını kazır ve içeriği anlamsallaştırmak, temizlemek ve yapılandırmak için OpenAI veya Ollama gibi büyük dil modellerini (LLM) kullanır.

##  Proje Hakkında

Web'den veri çıkarma (web scraping) işlemleri genellikle karmaşık ve kırılgandır. Sık sık değişen HTML yapıları, CSS seçicilerinin bakımını zorlaştırır. AI Web Parser, bu soruna modern bir yaklaşım getirir. Ham HTML içeriğini doğrudan yapay zeka modellerine göndererek, insan benzeri bir anlama süreciyle istenen verileri akıllıca çıkarmasını sağlar. Bu sayede, sitenin yapısı değişse bile veri çıkarma işlemi daha esnek ve dayanıklı hale gelir.

Bu proje **Baran Can Ercan** tarafından geliştirilmiştir.

## ✨ Özellikler

- **Esnek Kazıyıcılar**:
  - **Selenium/Chrome**: Dinamik JavaScript içeriğine sahip siteler için tam tarayıcı otomasyonu.
  - **BrightData**: Büyük ölçekli ve engellemelere karşı dayanıklı kazıma işlemleri için entegrasyon (planlanıyor).
- **Yapay Zeka Destekli Ayrıştırma (Parsing)**:
  - **OpenAI**: `gpt-4`, `gpt-3.5-turbo` gibi güçlü modellere erişim.
  - **Ollama**: Yerel olarak çalıştırılan açık kaynaklı modellerle (örn. Llama 3, Mistral) uyumluluk.
- **Modüler Tasarım**: Yeni kazıyıcıların veya yapay zeka modellerinin sisteme kolayca entegre edilebilmesi için tasarlanmıştır.
- **Komut Satırı Arayüzü (CLI)**: Kolay ve otomatize edilebilir kullanım.

## 🚀 Kurulum ve Kullanım

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/barancanercan/ai-web-parser.git
cd ai-web-parser
```

### 2. Sanal Ortam Oluşturun ve Aktive Edin

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS için
# .venv\Scripts\activate  # Windows için
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Ortam Değişkenlerini Ayarlayın

Projenin çalışması için API anahtarları gibi hassas bilgileri içeren bir `.env` dosyası oluşturmanız gerekmektedir. Ana dizinde `.env` adında bir dosya oluşturun ve içine aşağıdaki gibi gerekli bilgileri ekleyin:

```
OPENAI_API_KEY="sk-..."
```

### 5. Kullanım

Proje, bir komut satırı arayüzü (CLI) üzerinden çalışır. Aşağıda temel bir kullanım örneği bulunmaktadır:

```bash
python -m interfaces.cli.main --url "https://www.ornek-hedef-site.com" --parser openai
```

- `--url`: Veri çıkarmak istediğiniz hedef web sayfasının adresi.
- `--parser`: Kullanmak istediğiniz yapay zeka modelini belirtir (`openai` veya `ollama`).

## 🔮 Gelecek Planları

- [ ] **Streamlit Arayüzü**: Kullanıcıların işlemleri daha kolay yapabilmesi için interaktif bir web arayüzü geliştirme.
- [ ] **Farklı Veri Çıktı Formatları**: Sonuçları JSON, CSV veya XML olarak dışa aktarma seçeneği ekleme.
- [ ] **Daha Fazla LLM Desteği**: Anthropic (Claude), Google (Gemini) gibi diğer popüler modellere destek.
- [ ] **Docker Desteği**: Projeyi ve bağımlılıklarını bir Docker konteyneri içinde çalıştırma imkanı.
- [ ] **Gelişmiş Hata Yönetimi ve Tekrar Deneme Mekanizmaları**: Ağ hatalarına veya LLM API sorunlarına karşı daha dayanıklı hale getirme.

## 🤝 Katkıda Bulunma

Katkılarınız projeyi daha iyi hale getirecektir! Lütfen bir "issue" açarak veya "pull request" göndererek katkıda bulunun.

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına göz atın.