# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan - Jaya Jaya Maju

## Business Understanding
Jaya Jaya Maju merupakan perusahaan besar yang memiliki ribuan karyawan. Namun, perusahaan menghadapi tantangan besar berupa tingginya tingkat **Employee Attrition** (pengunduran diri karyawan). Kehilangan karyawan bertalenta tidak hanya mengganggu operasional perusahaan, tetapi juga meningkatkan biaya rekrutmen dan pelatihan bagi karyawan baru. Proyek ini bertujuan untuk mengidentifikasi faktor-faktor kunci yang menyebabkan karyawan meninggalkan perusahaan.

### Permasalahan Bisnis
1. Berapa persentase tingkat *attrition* karyawan saat ini?
2. Departemen dan jabatan (*Job Role*) mana yang memiliki tingkat *attrition* paling tinggi?
3. Apakah faktor lembur (*Overtime*) dan tingkat kepuasan kerja berkorelasi signifikan terhadap keputusan karyawan untuk *resign*?
4. Bagaimana profil pendapatan (*Monthly Income*) karyawan yang cenderung melakukan *attrition*?

### Cakupan Proyek
1. Melakukan pembersihan data (*Data Cleaning*) untuk menangani nilai kosong (*NaN*) dan duplikat.
2. Melakukan Analisis Data Eksploratif (EDA) untuk menemukan pola keberhentian karyawan.
3. Membangun *Business Dashboard* interaktif untuk memonitor KPI kepegawaian secara *real-time*.
4. Memberikan rekomendasi strategis bagi tim HR untuk menurunkan tingkat *attrition*.

### Persiapan
**Sumber data:** Dataset Employee Attrition (IBM HR Analytics) yang disediakan oleh Dicoding.

**Setup environment:**
```python
# Library yang digunakan dalam analisis (Google Colab/Jupyter Notebook)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tool Visualisasi: 
# Google Looker Studio (Cloud-based Dashboard)
```

## Business Dashboard
Dashboard ini dirancang untuk memberikan gambaran menyeluruh mengenai kesehatan retensi karyawan di Jaya Jaya Maju. Fokus utama dashboard adalah membandingkan kelompok karyawan yang bertahan (*Stay*) dan yang keluar (*Resign*) berdasarkan variabel-variabel kunci.

**Komponen Utama Dashboard:**
- **4 Scorecards:** Menampilkan Total Employees (1,058), Attrition Rate (~16%), serta rata-rata Job & Environment Satisfaction.
- **Attrition by Overtime:** Menunjukkan korelasi kuat antara kebijakan lembur dengan pengunduran diri.
- **Attrition by Job Role:** Mengidentifikasi jabatan berisiko tinggi seperti *Sales Representative* dan *Laboratory Technician*.
- **Attrition by Income Group:** Menganalisis stabilitas karyawan berdasarkan rentang gaji.

**Link Dashboard:** [https://lookerstudio.google.com/reporting/69f7eef0-f412-4664-b078-50596e295b84]


## Conclusion
Dari analisis yang dilakukan, dapat disimpulkan bahwa:
1. **Lembur adalah pemicu utama:** Karyawan yang sering bekerja lembur (*Overtime*) memiliki rasio *attrition* yang jauh lebih tinggi dibandingkan yang tidak.
2. **Jabatan Spesifik:** Jabatan *Sales Representative* dan *Lab Technician* memiliki tingkat *turnover* paling fluktuatif, kemungkinan karena tekanan kerja atau kompensasi yang kurang kompetitif.
3. **Faktor Finansial:** Karyawan dengan pendapatan bulanan rendah (*Low Income*) lebih rentan untuk meninggalkan perusahaan demi peluang yang lebih baik.
4. **Kepuasan Lingkungan:** Terdapat korelasi antara rendahnya skor *Environment Satisfaction* dengan keinginan karyawan untuk mencari lingkungan kerja baru.

### Rekomendasi Action Items (Optional)
- **Review Kebijakan Lembur:** Melakukan evaluasi beban kerja pada departemen yang memiliki jam lembur tinggi dan memberikan kompensasi atau waktu istirahat tambahan.
- **Retention Program untuk High-Risk Roles:** Memberikan insentif khusus atau jalur karier yang lebih jelas bagi jabatan *Sales Representative* dan *Laboratory Technician*.
- **Salary Benchmarking:** Melakukan penyesuaian gaji untuk karyawan di kelompok *Low Income* agar sesuai dengan standar pasar industri.
- **Perbaikan Lingkungan Kerja:** Mengadakan survei kepuasan internal secara berkala untuk memperbaiki fasilitas atau budaya kerja di departemen dengan skor kepuasan rendah.

---

