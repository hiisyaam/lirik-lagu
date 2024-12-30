import sys
import time

def nyanyi_bro():
    lyrics = [
        ("Tapi tak perlu cemaskan aku", 0.1, [
            (0, 14, 0.08),
            (14, 15, 2),
            (15, 19, 0.1),
            (19, 20, 2.3)
        ]),
        ("Dan bertanya-tanya", 0.08, [
            (0,11,0.1),
            (11,15,0.3)
        ]),
        ("Siapa yang jadi bahu saat kau perlu", 0.09, [
            (0,3,0.08),
            (3,4,0.1),
            (4,20,0.2),
            (20,21,0.08)
        ]),
        ("Menangis terluka di payung rindu", 0.09, [
            (8,9,0.9),
            (16,17,0.9)

        ]),
        ("Apa ada yang bisa ambil peranku", 0.09, [
            (0,3,0.4),
            (17,18,1)
        ]),
        ("Menjaga dirimu yang kini tak di tanganku", 0.1, [
            (14,15,2),
            (21,30,0.1)
        ])
    ]

    jeda = [2, 0.5, 1, 1.2, 1.3, 1.5]
    
    print("\n=== Tak Di Tanganku ===")

    for i, (lirik, jeda_default, bagian_khusus_pajang_pendek) in enumerate(lyrics):
        posisi = 0
        for idx, huruf in enumerate(lirik):
            # Cek apakah huruf ini bagian dari segmen khusus
            delay_huruf = jeda_default
            for start, end, special_timing in bagian_khusus_pajang_pendek:
                if start <= idx < end:
                    delay_huruf = special_timing
                    break
            
            print(huruf, end='')
            sys.stdout.flush()
            time.sleep(delay_huruf)
        
        time.sleep(jeda[i])
        print('')
    
    print("=== Selesai ===")

nyanyi_bro()