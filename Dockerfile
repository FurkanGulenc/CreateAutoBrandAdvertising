# Uygulamanın çalıştırılacağı temel imaj
FROM python:3.9

# Uygulamanın kaynak kodunun kopyalanacağı dizin
WORKDIR /app

# requirements.txt dosyasını ve diğer gerekli dosyaları kopyala
COPY requirements.txt ./

# Bağımlılıkları kur
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamanın geri kalanını kopyala
COPY . .

# Uygulamanın bağlanacağı portu belirt
EXPOSE 8007

# Uygulamayı çalıştır
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8007", "--reload"]
