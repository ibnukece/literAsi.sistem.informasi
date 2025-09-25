import json
import pandas as pd

# Baca file JSON
with open("Sumber_Data_SIKAT_Konoha.ibnu.TIA.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Buat file Excel
with pd.ExcelWriter("Sumber_Data_SIKAT_Konoha.xlsx", engine="openpyxl") as writer:
    for kategori in data:
        nama_sheet = kategori["Kategori"][:31]  # max 31 karakter untuk nama sheet Excel
        df = pd.DataFrame(kategori["Data"])
        df.to_excel(writer, sheet_name=nama_sheet, index=False)

print("Konversi selesai! File Excel sudah dibuat: Sumber_Data_SIKAT_Konoha.xlsx")
