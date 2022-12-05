# Function Value of Detection
def valDetect(lnp):
    lnp_detect = lnp.split(" ")
    lnp_front = lnp_detect[0]
    lnp_number = lnp_detect[1]
    lnp_back = lnp_detect[2][0]
    lnp_country = ""
    lnp_region = ""

    # Back - Front
    # Plat nomor akhir yang diawali huruf tertentu dan diikuti plat nomor awal
    # Contoh "AA": "A": "Kota Magelang" menunjukkan plat nomor AA 123 A**, tanda bintang berarti huruf setelahnya bebas
    lnp_dict = {
        "A": {
            "A": "Kota Serang",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kota Bogor",
            "G": "Kota Pekalongan",
            "H": "Kota Semarang",
            "K": "Kabupaten Pati",
            "M": "Kabupaten Pamekasan",
            "N": "Kota Malang",
            "P": "Kabupaten Bondowoso",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Bojonegoro",
            "T": "Kabupaten Purwakarta",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Sumedang",
            "AA": "Kota Magelang",
            "AB": "Kota Yogyakarta",
            "AD": "Kota Surakarta",
            "AE": "Kota Madiun",
            "AG": "Kota Kediri",
            "BA": "Kota Padang",
            "BB": "Kota Sibolga",
            "BD": "Kota Bengkulu",
            "BK": "Kota Medan",
            "BL": "Kota Banda Aceh",
            "BM": "Kota Pekanbaru",
            "BN": "Kota Pangkal Pinang",
            "BP": "Kota Tanjung Pinang",
            "DB": "Kota Manado",
            "DC": "Kabupaten Mamuju",
            "DD": "Kota Makassar",
            "DE": "Kota Ambon",
            "DG": "Kota Ternate",
            "DH": "Kabupaten/Kota Kupang",
            "DK": "Kabupaten Denpasar",
            "DL": "Kabupaten Kepulauan Sangihe",
            "DM": "Kota Gorontalo",
            "DN": "Kota Palu",
            "DR": "Kota Mataram",
            "DT": "Kabupaten Konawe",
            "EA": "Kabupaten Sumbawa",
            "EB": "Kabupaten Ende",
            "ED": "Kabupaten Sumba Barat",
            "KB": "Kota Pontianak",
            "KH": "Kota Palangkaraya",
            "KT": "Kota Balikpapan",
            "PA": "Kota Jayapura",
        },
        "B": {
            "A": "Kota Serang",
            "B": "Kota Jakarta Barat",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kota Bogor",
            "G": "Kabupaten Pekalongan",
            "H": "Kota Salatiga",
            "K": "Kabupaten Kudus",
            "M": "Kabupaten Pamekasan",
            "N": "Kota Malang",
            "P": "Kabupaten Bondowoso",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Bojonegoro",
            "T": "Kabupaten Purwakarta",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Sumedang",
            "AA": "Kabupaten Magelang",
            "AB": "Kabupaten Bantul",
            "AD": "Kabupaten Sukoharjo",
            "AE": "Kota Madiun",
            "AG": "Kota Kediri",
            "BA": "Kota Padang",
            "BB": "Kabupaten Tapanuli",
            "BD": "Kabupaten Bengkulu Selatan",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Besar",
            "BM": "Kabupaten Indragiri Hulu",
            "BN": "Kabupaten Bangka",
            "BP": "Kabupaten Bintan",
            "DB": "Kabupaten Minahasa",
            "DC": "Kabupaten Majene",
            "DD": "Kabupaten Gowa",
            "DE": "Kabupaten Maluku Tengah",
            "DG": "Kota Tidore Kepulauan",
            "DH": "Kabupaten//Kota Kupang ",
            "DK": "Kabupaten Denpasar",
            "DL": "Kabupaten Kepulauan Talaud",
            "DM": "Kabupaten Gorontalo",
            "DN": "Kabupaten Donggala",
            "DR": "Kota Mataram",
            "DT": "Kabupaten Kolaka Utara",
            "EB": "Kabupaten Sikka",
            "ED": "Kabupaten Sumba Timur",
            "KB": "Kabupaten Mempawah",
            "KH": "Kabupaten Kapuas",
            "KT": "Kota Samarinda",
            "PA": "Kabupaten Jayawijaya",
            "PB": "Kabupaten Teluk Bintuni",
        },
        "C": {
            "A": "Kota Serang",
            "B": "Kota Tangerang",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kota Bogor",
            "G": "Kabupaten Batang",
            "H": "Kabupaten Semarang",
            "K": "Kabupaten Jepara",
            "M": "Kabupaten Pamekasan",
            "N": "Kota Malang",
            "P": "Kabupaten Bondowoso",
            "R": "Kabupaten Purbalingga",
            "S": "Kabupaten Bojonegoro",
            "T": "Kabupaten Purwakarta",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Sumedang",
            "AA": "Kabupaten Purworejo",
            "AB": "Kabupaten Kulon Progo",
            "AD": "Kabupaten Klaten",
            "AE": "Kota Madiun",
            "AG": "Kota Kediri",
            "BA": "Kabupaten Lima Puluh Kota",
            "BB": "Kabupaten Samosir",
            "BD": "Kota Bengkulu",
            "BE": "Kota Bandar Lampung",
            "BG": "Kota Prabumulih",
            "BH": "Kabupaten Tebo",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Barat Daya",
            "BM": "Kabupaten Pelalawan",
            "BN": "Kabupaten Bangka Tengah",
            "BP": "Kota Batam",
            "DB": "Kota Bitung",
            "DC": "Kabupaten Polewali Mandar",
            "DD": "Kabupaten Takalar",
            "DH": "Kabupaten/Kota Kupang",
            "DK": "Kabupaten Denpasar",
            "DL": "Kabupaten Kepulauan Sitaro",
            "DM": "Kabupaten Boalemo",
            "DN": "Kabupaten Banggai",
            "DR": "Kota Mataram",
            "DT": "Kabupaten Wakatobi",
            "EB": "Kabupaten Ngada",
            "KB": "Kota Singkawang",
            "KT": "Kabupaten Kutai Kartanegara",
            "PA": "Kabupaten Paniai",
        },
        "D": {
            "A": "Kota Serang",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kota Bogor",
            "G": "Kabupaten Pemalang",
            "H": "Kabupaten Kendal",
            "K": "Kabupaten Rembang",
            "M": "Kabupaten Pamekasan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Bondowoso",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Bojonegoro",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Garut",
            "AA": "Kabupaten Kebumen",
            "AB": "Kabupaten Gunung Kidul",
            "AD": "Kabupaten Boyolali",
            "AE": "Kabupaten Madiun",
            "AG": "Kabupaten Kediri",
            "BA": "Kabupaten Pasaman",
            "BB": "Kabupaten Humbang Hasundutan",
            "BD": "Kabupaten Bengkulu Utara",
            "BE": "Kabupaten Lampung Selatan",
            "BG": "Kabupaten Muara Enim",
            "BH": "Kabupaten Kerinci",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Timur",
            "BM": "Kabupaten Bengkalis",
            "BN": "Kabupaten Bangka Barat",
            "BP": "Kota Batam",
            "DB": "Kota Bolaang Mongondow",
            "DC": "Kabupaten Minahasa",
            "DD": "Kabupaten Maros",
            "DE": "Kabupaten Buru",
            "DG": "Kabupaten Halmahera Timur",
            "DH": "Kabupaten Timor Tengah Utara",
            "DK": "Kabupaten Denpasar",
            "DM": "Kabupaten Pohuwato",
            "DN": "Kabupaten Toli-Toli",
            "DR": "Kota Mataram",
            "DT": "Kabupaten Muna",
            "EB": "Kabupaten Flores Timur",
            "KB": "Kabupaten Sanggau",
            "KH": "Kabupaten Barito Selatan",
            "KT": "Kota Bontang",
            "PA": "Kabupaten Mimika",
        },
        "E": {
            "A": "Kabupaten Serang",
            "B": "Kota Depok",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kota Bogor",
            "G": "Kota Tegal",
            "H": "Kabupaten Demak",
            "K": "Kabupaten Blora",
            "M": "Kabupaten Pamekasan",
            "N": "Kota Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Tuban",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Garut",
            "AA": "Kabupaten Temanggung",
            "AB": "Kabupaten Sleman",
            "AD": "Kabupaten Sragen",
            "AE": "Kabupaten Madiun",
            "AG": "Kabupaten Kediri",
            "BA": "Kabupaten Tanah Datar",
            "BB": "Kabupaten Toba Samosir",
            "BD": "Kota Bengkulu",
            "BE": "Kabupaten Lampung Selatan",
            "BG": "Kabupaten Lahat",
            "BH": "Kabupaten Tanjung Jabung Barat",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Barat",
            "BM": "Kabupaten Bengkalis",
            "BN": "Kabupaten Bangka Selatan",
            "BP": "Kota Batam",
            "DB": "Kabupaten Minahasa Selatan",
            "DC": "Kabupaten Mamuju Utara",
            "DD": "Kabupaten Pangkajene Kepulauan",
            "DE": "Kabupaten Maluku Tenggara",
            "DG": "Kabupaten Kepulauan Sula",
            "DH": "Kabupaten Timor Tengah Selatan",
            "DK": "Kabupaten Denpasar",
            "DM": "Kabupaten Bone Bolango",
            "DN": "Kabupaten Poso",
            "DR": "Kota Mataram",
            "DT": "Kabupaten Kendari",
            "EB": "Kabupaten Manggarai Barat",
            "KB": "Kabupaten Sintang",
            "KH": "Kabupaten Barito Utara",
            "KT": "Kabupaten Paser",
            "PA": "Kabupaten Nabire",
        },
        "F": {
            "A": "Kabupaten Serang",
            "B": "Kabupaten Bekasi",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Tegal",
            "H": "Kota Semarang",
            "K": "Kabupaten Grobogan",
            "M": "Kabupaten Pamekasan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Tuban",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Garut",
            "AA": "Kabupaten Wonosobo",
            "AB": "Kota Yogyakarta",
            "AD": "Kabupaten Karanganyar",
            "AE": "Kabupaten Madiun",
            "AG": "Kabupaten Kediri",
            "BA": "Kabupaten Padang Pariaman",
            "BB": "Kota Padang Sidempuan",
            "BE": "Kota Metro",
            "BG": "Kabupaten Ogan Komering Ulu",
            "BH": "Kabupaten Merangin",
            "BK": "Kota Medan",
            "BL": "Kota Langsa",
            "BM": "Kabupaten Kampar",
            "BN": "Kabupaten Belitung",
            "BP": "Kota Batam",
            "DB": "Kabupaten Minahasa Utara",
            "DD": "Kabupaten Bantaeng",
            "DE": "Kabupaten Buru Selatan",
            "DH": "Kabupaten Alor",
            "DK": "Kabupaten Badung",
            "DM": "Kabupaten Gorontalo Utara",
            "DN": "Kabupaten Buol",
            "DT": "Kabupaten Buton Utara",
            "EB": "Kabupaten Lembata",
            "KB": "Kabupaten Kapuas",
            "KH": "Kabupaten Kotawaringin Timur",
            "PB": "Kabupaten Fakfak",
        },
        "G": {
            "A": "Kabupaten Serang",
            "B": "Kabupaten Tangerang",
            "D": "Kota Bandung",
            "E": "Kota Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Brebes",
            "H": "Kota Semarang",
            "K": "Kabupaten Pati",
            "M": "Kabupaten Pamekasan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Tuban",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Garut",
            "AA": "Kabupaten Magelang",
            "AB": "Kabupaten Bantul",
            "AD": "Kabupaten Wonogiri",
            "AE": "Kabupaten Madiun",
            "AG": "Kabupaten Kediri",
            "BA": "Kabupaten Pesisir Selatan",
            "BB": "Kabupaten Tapanuli Selatan",
            "BD": "Kabupaten Kepahiang",
            "BE": "Kabupaten Lampung Tengah",
            "BG": "Kabupaten Musi Rawas",
            "BH": "Kabupaten Muaro Jambi",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Tengah",
            "BM": "Kabupaten Indragiri Hilir",
            "BN": "Kabupaten Belitung Timur",
            "BP": "Kota Batam",
            "DB": "Kota Tomohon",
            "DD": "Kabupaten Jeneponto",
            "DH": "Kabupaten Belu",
            "DK": "Kabupaten Tabanan",
            "DN": "Kabupaten Morowali",
            "DT": "Kabupaten Buton",
            "EB": "Kabupaten Manggarai",
            "KB": "Kabupaten Ketapang",
            "KH": "Kabupaten Kotawaringin Barat",
            "KT": "Kabupaten Berau",
            "PA": "Kabupaten Merauke",
        },
        "H": {
            "A": "Kabupaten Serang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kota Pekalongan",
            "H": "Kota Semarang",
            "K": "Kabupaten Pati",
            "M": "Kabupaten Bangkalan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Tuban",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kota Tasikmalaya",
            "AA": "Kota Magelang",
            "AB": "Kota Yogyakarta",
            "AD": "Kota Surakarta",
            "AE": "Kabupaten Ngawi",
            "AG": "Kabupaten Kediri",
            "BA": "Kabupaten Solok",
            "BB": "Kota Padang Sidempuan",
            "BD": "Kabupaten Lebong",
            "BE": "Kabupaten Lampung Tengah",
            "BG": "Kota Lubuk Linggau",
            "BH": "Kabupaten Muaro Jambi",
            "BK": "Kota Medan",
            "BL": "Kabupaten Gayo Lues",
            "BM": "Kota Dumai",
            "BP": "Kota Batam",
            "DB": "Kabupaten Bolaang Mongondow Utara",
            "DD": "Kabupaten Bulukumba",
            "DK": "Kabupaten Tabanan",
            "DN": "Kabupaten Banggai Kepulauan",
            "DR": "Kabupaten Lombok Barat",
            "DT": "Kabupaten Konawe Selatan",
            "EA": "Kabupaten Sumbawa Barat",
            "KB": "Kabupaten Melawi",
            "KH": "Kabupaten Gunung Mas",
        },
        "I": {
            "A": "Kabupaten Serang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Pemalang",
            "H": "Kabupaten Semarang",
            "K": "Kabupaten Rembang",
            "M": "Kabupaten Bangkalan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Lamongan",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kota Tasikmalaya",
            "AB": "Kota Yogyakarta",
            "AD": "Kabupaten Wonogiri",
            "AE": "Kabupaten Ngawi",
            "AG": "Kabupaten Blitar",
            "BA": "Kabupaten Pesisir Selatan",
            "BE": "Kabupaten Lampung Tengah",
            "BG": "Kota Palembang",
            "BK": "Kota Medan",
            "BL": "Kota Subulussalam",
            "BM": "Kabupaten Pelalawan",
            "BP": "Kota Batam",
            "DK": "Kabupaten Denpasar",
            "KT": "Kota Samarinda",
        },
        "J": {
            "A": "Kabupaten Pandeglang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Brebes",
            "H": "Kabupaten Demak",
            "K": "Kabupaten Grobogan",
            "M": "Kabupaten Bangkalan",
            "N": "Kabupaten Malang",
            "P": "Kabupaten Situbondo",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Lamongan",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kota Tasikmalaya",
            "AA": "Kabupaten Kebumen",
            "AB": "Kabupaten Bantul",
            "AD": "Kabupaten Klaten",
            "AE": "Kabupaten Ngawi",
            "AG": "Kabupaten Kediri",
            "BA": "Kota Sawahlunto",
            "BB": "Kabupaten Padang Lawas",
            "BE": "Kabupaten Lampung Utara",
            "BG": "Kabupaten Banyuasin",
            "BK": "Kabupaten Labuhanbatu Utara",
            "BL": "Kota Banda Aceh",
            "BM": "Kota Pekanbaru",
            "BP": "Kota Batam",
            "DB": "Kabupaten Minahasa Tenggara",
            "DD": "Kabupaten Selayar",
            "DE": "Kabupaten Maluku Tenggara Barat",
            "DK": "Kabupaten Badung",
            "DN": "Kabupaten Parigi Moutong",
            "DR": "Kabupaten Lombok Barat",
            "DT": "Kabupaten Kolaka",
            "KH": "Kabupaten Pulang Pisau",
            "PA": "Kabupaten Jayapura",
        },
        "K": {
            "A": "Kabupaten Pandeglang",
            "B": "Kota Bekasi",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Pekalongan",
            "H": "Kota Salatiga",
            "K": "Kabupaten Kudus",
            "M": "Kabupaten Bangkalan",
            "N": "Kota Batu",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Lamongan",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Magelang",
            "AB": "Kabupaten Bantul",
            "AD": "Kabupaten Sukoharjo",
            "AE": "Kabupaten Ngawi",
            "AG": "Kabupaten Blitar",
            "BA": "Kabupaten Sijunjung",
            "BB": "Kabupaten Padang Lawas",
            "BD": "Kabupaten Rejang Lebong",
            "BE": "Kabupaten Lampung Utara",
            "BG": "Kabupaten Ogan Komering Ilir",
            "BH": "Kabupaten Bungo",
            "BK": "Kota Medan",
            "BL": "Kabupaten Aceh Utara",
            "BM": "Kabupaten Kuantan Singingi",
            "BP": "Kabupaten Karimun",
            "DB": "Kota Kotamobagu",
            "DD": "Kota Makassar",
            "DE": "Kabupaten Maluku Barat Daya",
            "DG": "Kabupaten Halmahera Selatan",
            "DK": "Kabupaten Gianyar",
            "DN": "Kabupaten Parigi Moutong",
            "DR": "Kabupaten Lombok Barat",
            "DT": "Kabupaten Bombana",
            "KB": "Kabupaten Bengkayang",
            "KH": "Kabupaten Barito Timur",
            "KT": "Kota Balikpapan",
            "PA": "Kabupaten Biak Numfor",
            "PB": "Kabupaten Kaimana",
        },
        "L": {
            "A": "Kabupaten Pandeglang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Batang",
            "H": "Kabupaten Semarang",
            "K": "Kabupaten Jepara",
            "M": "Kabupaten Bangkalan",
            "N": "Kota Batu",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Purbalingga",
            "S": "Kabupaten Lamongan",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Purworejo",
            "AB": "Kabupaten Kulon Progo",
            "AD": "Kabupaten Klaten",
            "AE": "Kabupaten Ngawi",
            "AG": "Kabupaten Blitar",
            "BA": "Kota Bukittinggi",
            "BB": "Kota Sibolga",
            "BD": "Kota Bengkulu",
            "BE": "Kabupaten Mesuji",
            "BG": "Kota Palembang",
            "BH": "Kota Jambi",
            "BK": "Kota Medan",
            "BL": "Kota Banda Aceh",
            "BM": "Kota Pekanbaru",
            "DB": "Kota Manado",
            "DD": "Kabupaten Gowa",
            "DE": "Kabupaten Seram Bagian Timur",
            "DG": "Kabupaten Halmahera Tengah",
            "DK": "Kabupaten Gianyar",
            "DN": "Kabupaten Tojo Una-Una",
            "DR": "Kabupaten Lombok Timur",
            "KB": "Kabupaten Landak",
            "KT": "Kota Balikpapan",
            "PA": "Kabupaten Kepualuan Yapen",
        },
        "M": {
            "A": "Kabupaten Pandeglang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Pemalang",
            "H": "Kabupaten Kendal",
            "K": "Kabupaten Rembang",
            "M": "Kabupaten Bangkalan",
            "N": "Kabupaten Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Gresik",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Kebumen",
            "AB": "Kabupaten Gunung Kidul",
            "AD": "Kabupaten Boyolali",
            "AE": "Kabupaten Magetan",
            "AG": "Kabupaten Blitar",
            "BA": "Kota Payakumbuh",
            "BB": "Kota Sibolga",
            "BD": "Kabupaten Bengkulu Selatan",
            "BE": "Kabupaten Lampung Barat",
            "BG": "Kota Palembang",
            "BH": "Kota Jambi",
            "BK": "Kabupaten Deli Serdang",
            "BL": "Kota Sabang",
            "BM": "Kabupaten Rokan Hulu",
            "BP": "Kota Batam",
            "DB": "Kota Manado",
            "DG": "Kabupaten Halmahera Barat",
            "DK": "Kabupaten Klungkung",
            "DN": "Kabupaten Sigi",
            "DT": "Kabupaten Konawe Utara",
            "KB": "Kabupaten Kubu Raya",
            "KH": "Kabupaten Murung Raya",
            "KT": "Kota Samarinda",
            "PB": "Kabupaten Manokwari",
        },
        "N": {
            "A": "Kabupaten Pandeglang",
            "B": "Kabupaten Tangerang",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kota Tegal",
            "H": "Kabupaten Demak",
            "K": "Kabupaten Blora",
            "M": "Kabupaten Bangkalan",
            "N": "Kabupaten Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Temanggung",
            "AB": "Kabupaten Sleman",
            "AD": "Kabupaten Sragen",
            "AE": "Kabupaten Magetan",
            "AG": "Kabupaten Blitar",
            "BA": "Kota Padang Panjang",
            "BB": "Kabupaten Tapanuli Tengah",
            "BD": "Kabupaten Muko Muko",
            "BE": "Kabupaten Lampung Timur",
            "BG": "Kota Palembang",
            "BH": "Kota Jambi",
            "BK": "Kota Tebing Tinggi",
            "BL": "Kota Lhokseumawe",
            "BM": "Kota Pekanbaru",
            "BP": "Kabupaten Natuna",
            "DB": "Kabupaten Bolaang Mongondow Timur",
            "DE": "Kabupaten Kepulauan Aru",
            "DG": "Kabupaten Halmahera Utara",
            "DK": "Kabupaten Klungkung",
            "KH": "Kabupaten Katingan",
            "KT": "Kota Samarinda",
        },
        "O": {
            "A": "Kota Cilegon",
            "D": "Kota Bandung",
            "E": "Kabupaten Cirebon",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Pekalongan",
            "H": "Kota Salatiga",
            "K": "Kabupaten Kudus",
            "N": "Kabupaten Pasuruan",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Magelang",
            "AD": "Kabupaten Sukoharjo",
            "AE": "Kabupaten Magetan",
            "AG": "Kabupaten Tulungagung",
            "BA": "Kota Padang",
            "BE": "Kabupaten Lampung Selatan",
            "BG": "Kabupaten Penukal Abab Lematang Ilir",
            "BK": "Kabupaten Batubara",
            "BL": "Kabupaten Pidie Jaya",
            "BM": "Kabupaten Kampar",
            "BP": "Kabupaten Lingga",
            "DE": "Kabupaten Seram Bagian Barat",
            "DK": "Kabupaten Badung",
            "KT": "Kabupaten Kutai Kartanegara",
        },
        "P": {
            "A": "Kabupaten Lebak",
            "B": "Kota Jakarta Pusat",
            "D": "Kota Bandung",
            "E": "Kabupaten Indramayu",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Tegal",
            "H": "Kota Semarang",
            "K": "Kabupaten Grobogan",
            "N": "Kabupaten Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Wonosobo",
            "AB": "Kabupaten Kulon Progo",
            "AD": "Kabupaten Karanganyar",
            "AE": "Kabupaten Magetan",
            "AG": "Kota Blitar",
            "BA": "Kota Solok",
            "BD": "Kabupaten Seluma",
            "BE": "Kabupaten Lampung Timur",
            "BG": "Kota Palembang",
            "BH": "Kabupaten Merangin",
            "BK": "Kabupaten Langkat",
            "BL": "Kabupaten Pidie",
            "BM": "Kabupaten Rokan Hilir",
            "BP": "Kota Batam",
            "DB": "Kabupaten Bolaang Mongondow Selatan",
            "DK": "Kabupaten Bangli",
            "KB": "Kabupaten Sambas",
            "KH": "Kabupaten Seruyan",
            "KT": "Kabupaten Kutai Barat",
            "PA": "Kabupaten Puncak Jaya",
        },
        "Q": {
            "E": "Kabupaten Indramayu",
            "F": "Kabupaten Sukabumi",
            "G": "Kabupaten Tegal",
            "H": "Kota Semarang",
            "K": "Kabupaten Jepara",
            "N": "Kota Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Purbalingga",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kabupaten Purworejo",
            "AB": "Kabupaten Sleman",
            "AD": "Kabupaten Klaten",
            "AE": "Kabupaten Magetan",
            "AG": "Kota Blitar",
            "BA": "Kota Padang",
            "BB": "Kabupaten Nias Utara",
            "BE": "Kabupaten Tulang Bawang Barat",
            "BG": "Kota Palembang",
            "BH": "Kota Jambi",
            "BK": "Kota Tanjung Balai",
            "BL": "Kabupaten Aceh Utara",
            "BM": "Kota Pekanbaru",
            "BP": "Kota Batam",
            "DK": "Kabupaten Denpasar",
            "DN": "Kabupaten Banggai Laut",
            "KT": "Kota Bontang",
        },
        "R": {
            "A": "Kabupaten Lebak",
            "D": "Kota Bandung",
            "E": "Kabupaten Indramayu",
            "F": "Kabupaten Bogor",
            "G": "Kabupaten Brebes",
            "H": "Kota Semarang",
            "K": "Kabupaten Kudus",
            "N": "Kota Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Cilacap",
            "S": "Kabupaten Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AD": "Kabupaten Wonogiri",
            "AE": "Kabupaten Magetan",
            "AG": "Kabupaten Tulungagung",
            "BA": "Kota Padang",
            "BB": "Kabupaten Mandailing",
            "BE": "Kabupaten Pesawaran",
            "BG": "Kota Palembang",
            "BH": "Kota Sungai Penuh",
            "BK": "Kota Binjai",
            "BL": "Kabupaten Aceh Singkil",
            "BM": "Kota Dumai",
            "BP": "Kota Batam",
            "DB": "Kota Manado",
            "DK": "Kabupaten Bangli",
            "DN": "Kabupaten Banggai",
            "EA": "Kabupaten Dompu",
            "KH": "Kabupaten Lamandau",
            "KT": "Kabupaten Kutai Timur",
        },
        "S": {
            "A": "Kabupaten Lebak",
            "B": "Kota Jakarta Selatan",
            "D": "Kota Cimahi",
            "E": "Kabupaten Indramayu",
            "F": "Kota Sukabumi",
            "G": "Kota Pekalongan",
            "H": "Kota Semarang",
            "K": "Kabupaten Pati",
            "N": "Kota Probolinggo",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Banyumas",
            "S": "Kota Mojokerto",
            "T": "Kabupaten Karawang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Tasikmalaya",
            "AA": "Kota Magelang",
            "AB": "Kota Yogyakarta",
            "AD": "Kota Surakarta",
            "AE": "Kabupaten Ponorogo",
            "AG": "Kabupaten Tulungagung",
            "BA": "Kabupaten Pasaman Barat",
            "BD": "Kabupaten Bengkulu Utara",
            "BE": "Kabupaten Tulang Bawang",
            "BG": "Kabupaten Empat Lawang",
            "BH": "Kabupaten Sarolangun",
            "BK": "Kabupaten Karo",
            "BL": "Kabupaten Simeulue",
            "BM": "Kabupaten Siak",
            "BP": "Kabupaten Kepulauan Anambas",
            "DK": "Kabupaten Karangasem",
            "DR": "Kabupaten Lombok Tengah",
            "EA": "Kota Bima",
            "KH": "Kabupaten Sukamara",
            "PB": "Kabupaten Sorong Selatan",
        },
        "T": {
            "A": "Kabupaten Lebak",
            "B": "Kota Jakarta Timur",
            "D": "Kota Cimahi",
            "E": "Kabupaten Indramayu",
            "F": "Kota Sukabumi",
            "G": "Kabupaten Pekalongan",
            "H": "Kota Salatiga",
            "K": "Kabupaten Kudus",
            "N": "Kabupaten Pasuruan",
            "P": "Kabupaten Jember",
            "R": "Kabupaten Cilacap",
            "S": "Kota Mojokerto",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Ciamis",
            "AA": "Kabupaten Magelang",
            "AB": "Kabupaten Bantul",
            "AD": "Kabupaten Sukoharjo",
            "AE": "Kabupaten Ponorogo",
            "AG": "Kabupaten Tulungagung",
            "BA": "Kabupaten Agam",
            "BB": "Kota Gunungsitoli",
            "BE": "Kabupaten Tulang Bawang",
            "BG": "Kabupaten Ogan Ilir",
            "BH": "Kabupaten Tanjung Jabung Timur",
            "BK": "Kabupaten Simalungun",
            "BL": "Kabupaten Aceh Selatan",
            "BM": "Kota Pekanbaru",
            "BP": "Kota Tanjung Pinang",
            "DE": "Kota Tual",
            "DK": "Kabupaten Karangasem",
            "KH": "Kota Palangkaraya",
        },
        "U": {
            "A": "Kota Cilegon",
            "B": "Kota Jakarta Utara",
            "D": "Kabupaten Bandung Barat",
            "E": "Kabupaten Majalengka",
            "F": "Kabupaten Sukabumi",
            "G": "Kabupaten Brebes",
            "H": "Kabupaten Kendal",
            "K": "Kabupaten Pati",
            "N": "Kabupaten Lumajang",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Purbalingga",
            "S": "Kota Mojokerto",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Ciamis",
            "AA": "Kota Magelang",
            "AB": "Kabupaten Sleman",
            "AD": "Kota Surakarta",
            "AE": "Kabupaten Ponorogo",
            "AG": "Kabupaten Nganjuk",
            "BA": "Kabupaten Kepulauan Mentawai",
            "BB": "Kabupaten Nias Barat",
            "BE": "Kabupaten Pringsewu",
            "BG": "Kota Palembang",
            "BH": "Kabupaten Bungo",
            "BK": "Kabupaten Simalungun",
            "BL": "Kabupaten Aceh Tamiang",
            "BM": "Kabupaten Rokan Hulu",
            "DG": "Kabupaten Pulau Morotai",
            "DH": "Kabupaten Rote Ndao",
            "DK": "Kabupaten Buleleng",
            "DN": "Kabupaten Morowali Utara",
            "KT": "Kabupaten Kutai Kartanegara",
        },
        "V": {
            "A": "Kota Cilegon",
            "B": "Kota Tangerang",
            "D": "Kabupaten Bandung",
            "E": "Kabupaten Majalengka",
            "F": "Kabupaten Sukabumi",
            "G": "Kabupaten Batang",
            "H": "Kabupaten Semarang",
            "K": "Kabupaten Jepara",
            "N": "Kota Pasuruan",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Purbalingga",
            "S": "Kota Mojokerto",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Ciamis",
            "AA": "Kabupaten Purworejo",
            "AB": "Kabupaten Kulon Progo",
            "AD": "Kabupaten Klaten",
            "AE": "Kabupaten Ponorogo",
            "AG": "Kabupaten Nganjuk",
            "BA": "Kabupaten Dharmasraya",
            "BB": "Kabupaten Nias",
            "BE": "Kabupaten Tanggamus",
            "BG": "Kabupaten Ogan Komering Ulu Selatan",
            "BK": "Kabupaten Asahan",
            "BL": "Kabupaten Nagan Raya",
            "BM": "Kabupaten Indragiri Hulu",
            "DK": "Kabupaten Buleleng",
            "DN": "Kota Palu",
            "KB": "Kabupaten Sekadau",
            "KT": "Kabupaten Penajam Paser Utara",
            "PB": "Kabupaten Maybrat",
        },
        "W": {
            "A": "Kabupaten Tangerang",
            "B": "Kota Tangerang Selatan",
            "D": "Kabupaten Bandung Barat",
            "E": "Kabupaten Majalengka",
            "F": "Kabupaten Cianjur",
            "G": "Kabupaten Pemalang",
            "H": "Kota Semarang",
            "K": "Kabupaten Rembang",
            "N": "Kabupaten Pasuruan",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Jombang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kabupaten Pangandaran",
            "AA": "Kabupaten Kebumen",
            "AB": "Kabupaten Gunung Kidul",
            "AD": "Kabupaten Boyolali",
            "AE": "Kabupaten Pacitan",
            "AG": "Kabupaten Nganjuk",
            "BA": "Kota Pariaman",
            "BB": "Kabupaten Nias Selatan",
            "BD": "Kabupaten Kaur",
            "BE": "Kabupaten Way Kanan",
            "BG": "Kota Pagaralam",
            "BH": "Kabupaten Tebo",
            "BK": "Kota Pematang Siantar",
            "BL": "Kabupaten Aceh Jaya",
            "BM": "Kabupaten Rokan Hilir",
            "DK": "Kabupaten Jembrana",
            "KT": "Kota Samarinda",
            "PB": "Kabupaten Teluk Wondama",
        },
        "X": {
            "A": "Kabupaten Tangerang",
            "D": "Kabupaten Bandung Barat",
            "E": "Kabupaten Majalengka",
            "F": "Kabupaten Cianjur",
            "G": "Kabupaten Batang",
            "H": "Kota Semarang",
            "K": "Kabupaten Blora",
            "N": "Kota Pasuruan",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Banyumas",
            "S": "Kabupaten Jombang",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kota Banjar",
            "AE": "Kabupaten Pacitan",
            "AG": "Kabupaten Nganjuk",
            "BA": "Kabupaten Lima Puluh Kota",
            "BE": "Kabupaten Pesisir Barat",
            "BG": "Kota Palembang",
            "BK": "Kabupaten Serdang Bedagai",
            "BL": "Kabupaten Aceh Tenggara",
            "BM": "Kabupaten Kuantan Singingi",
            "BM": "Kabupaten Kepulauan Meranti",
            "DK": "Kabupaten Denpasar",
            "EA": "Kabupaten Bima",
            "KT": "Kota Samarinda",
        },
        "Y": {
            "A": "Kabupaten Tangerang",
            "D": "Kabupaten Bandung",
            "E": "Kabupaten Kuningan",
            "F": "Kabupaten Cianjur",
            "G": "Kota Tegal",
            "H": "Kota Semarang",
            "K": "Kabupaten Blora",
            "N": "Kabupaten Lumajang",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Banjarnegara",
            "S": "Kabupaten Jombang",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kota Banjar",
            "AA": "Kabupaten Temanggung",
            "AB": "Kabupaten Sleman",
            "AD": "Kabupaten Sragen",
            "AE": "Kabupaten Pacitan",
            "AG": "Kabupaten Trenggalek",
            "BA": "Kabupaten Solok Selatan",
            "BB": "Kabupaten Dairi",
            "BD": "Kabupaten Bengkulu Tengah",
            "BE": "Kota Bandar Lampung",
            "BG": "Kabupaten Ogan Komering Ulu Timur",
            "BH": "Kota Jambi",
            "BK": "Kabupaten Labuhanbatu",
            "BL": "Kabupaten Bener Meriah",
            "BM": "Kabupaten Siak",
            "DN": "Kota Palu",
            "EA": "Kabupaten Bima",
            "KT": "Kota Balikpapan",
        },
        "Z": {
            "A": "Kabupaten Tangerang",
            "B": "Kota Depok",
            "D": "Kabupaten Bandung",
            "E": "Kabupaten Kuningan",
            "F": "Kabupaten Cianjur",
            "G": "Kabupaten Tegal",
            "H": "Kota Semarang",
            "K": "Kabupaten Grobogan",
            "N": "Kabupaten Lumajang",
            "P": "Kabupaten Banyuwangi",
            "R": "Kabupaten Purbalingga",
            "S": "Kabupaten Jombang",
            "T": "Kabupaten Subang",
            "W": "Kabupaten Sidoarjo",
            "Z": "Kota Banjar",
            "AA": "Kabupaten Wonosobo",
            "AB": "Kabupaten Sleman",
            "AD": "Kabupaten Karanganyar",
            "AE": "Kabupaten Pacitan",
            "AG": "Kabupaten Trenggalek",
            "BA": "Kabupaten Agam",
            "BB": "Kabupaten Pakpak Bharat",
            "BE": "Kabupaten Tanggamus",
            "BG": "Kota Palembang",
            "BH": "Kabupaten Muaro Jambi",
            "BK": "Kabupaten Labuhanbatu Selatan",
            "BL": "Kabupaten Bireuen",
            "BM": "Kabupaten Kampar",
            "BP": "Kota Batam",
            "DK": "Kabupaten Jembrana",
            "KB": "Kabupaten Kayong Utara",
            "KT": "Kota Balikpapan",
        },
    }

    if lnp_back in lnp_dict.keys():

        if lnp_front == "L":
            lnp_region = "Kota Surabaya"
            lnp_country = "Indonesia"
        elif lnp_front in lnp_dict[lnp_back]:
            lnp_region = lnp_dict[lnp_back][lnp_front]
            lnp_country = "Indonesia"
        else:
            lnp_region = "-"
            lnp_country = "-"
    else:
        lnp_region = "Tidak diketahui"
        lnp_country = "Luar Negara"

    return lnp_country, lnp_region, lnp_number