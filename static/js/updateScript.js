/**
 * function untuk memeperbarui baris pada data obat.
 * @param id_obat Primary Key
 * @param token CSRF token
 */
function updateRowObat(id_obat, id_produk, id_merk, netto, dosis, aturan,
    kontraindikasi, kesediaan, token) {
    console.log(id_obat);

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: `/obat/update/${id_obat}`,
        data: {
            id_obat : id_obat,
            id_produk : id_produk,
            id_merk : id_merk,
            netto : netto,
            dosis : dosis,
            aturan : aturan,
            kontraindikasi : kontraindikasi,
            kesediaan : kesediaan,
        },
        success: function () {
            console.log("Data sukses di kirim ke Django");
        },
    });
}