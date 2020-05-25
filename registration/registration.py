from django.db import connection

class Registration(object):
    """
    Sebuah class yang bertugas untuk mendaftarkan hasil
    input dari form perndaftaran ke dalam database postgre Heroku.
    """
    def __init__(self):
        super().__init__()

    def register_admin(self, email:str, password:str, **data):
        """
        function untuk mendaftarkan input ke tabel ADMIN_APOTEK.
        """
        status = self.__register_pengguna(email, password, data['nama'], data['telp'])
        status = status and self.__register_apoteker(email)
        
        if status:
            cursor = connection.cursor()
            cursor.execute("SET SEARCH_PATH TO farmakami;")

            query = f"""
            INSERT INTO admin_apotek
            VALUES ('{email}', NULL);
            """
            cursor.execute(query)
            print("REGISTRASI ADMIN APOTEK SUKSES")
        
        else:
            print("REGISTRASI ADMIN APOTEK GAGAL")


    def __register_pengguna(self, email:str, password:str, nama:str, telp:str) -> bool:
        """
        function untuk mendaftarkan input ke tabel PENGGUNA.
        function ini wajib dieksekusi pertama kali.
        """
        query = f"""
        INSERT INTO pengguna
        VALUES ('{email}', '{telp}', '{password}', '{nama}');
        """

        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        
        try:
            cursor.execute(query)
            print("REGISTRASI PENGGUNA SUKSES")
            return True
            
        except:
            print("REGISTRASI PENGGUNA GAGAL")
        
        return False


    def __register_apoteker(self, email:str) -> bool:
        """
        function untuk mendaftarkan orang menjadi Apoteker.
        Sebelum menjalankan function register admin atau cs, function ini wajib
        dieksekusi terlebih dahulu.
        """
        query = f"""
        INSERT INTO apoteker
        VALUES ('{email}');
        """

        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")

        try:
            cursor.execute(query)
            print("REGISTRASI APOTEKER SUKSES")
            return True

        except:
            print("REGISTRASI APOTEKER GAGAL")

        return False

    def __fetch(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
