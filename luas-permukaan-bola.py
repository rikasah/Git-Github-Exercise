import math

def luas_permukaan_bola(jari_jari):
    """
    Menghitung luas permukaan bola berdasarkan jari-jari.

    Parameters:
    jari_jari (float): Jari-jari bola

    Returns:
    float: Luas permukaan bola
    """
    luas = 4 * math.pi * (jari_jari ** 2)
    return luas

# Contoh penggunaan fungsi
jari_jari = 5
luas = luas_permukaan_bola(jari_jari)
print(f"Luas permukaan bola dengan jari-jari {jari_jari} adalah {luas:.2f}")