/**
 * function untuk menghapus baris pada data obat.
 * @param id_obat Primary Key
 * @param token CSRF token
 */
function deleteRowObat(id_obat, token) {
    console.log(id_obat)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/obat/tabel/delete/",
        data: {id_target : id_obat},
        success: function () {
            console.log("Data sukses di kirim ke Django");
        },
    });
}

/**
 * function untuk menghapus baris pada data produk apotek.
 * @param id_produk Primary Key
 * @param id_apotek Primary key
 * @param token CSRF token
 */
function deleteRowProdukApotek(id_produk, id_apotek, token) {
    console.log(id_produk)
    console.log(id_apotek)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/produk-apotek/tabel/delete/",
        data: {
            id_produk : id_produk,
            id_apotek : id_apotek
        },
        success: function () {
            console.log("Data sukses dikirim ke Django");
        },
    });
}

/**
 * function untuk menghapus baris pada data transaksi pembelian.
 * @param id_transaksi Primary Key
 * @param token CSRF token
 */
function deleteRowTransaksi(id_transaksi, token) {
    console.log(id_transaksi)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/transaksi-pembelian/tabel/delete/",
        data: { id_transaksi: id_transaksi },
        success: function () {
            console.log("Data sukses dikirim ke Django");
        },
    });
}

/**
 * function untuk menghapus baris pada data produk apotek.
 * @param id_apotek Primary Key
 * @param id_produk Primary Key
 * @param id_transaksi Primary key
 * @param token CSRF token
 */
function deleteRowProdukDibeli(id_apotek, id_produk, id_transaksi, token) {
    console.log(id_apotek)
    console.log(id_produk)
    console.log(id_transaksi)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/produk-apotek/tabel/delete/",
        data: {
            id_apotek: id_apotek,
            id_produk: id_produk,
            id_transaksi: id_transaksi,
        },
        success: function () {
            console.log("Data sukses dikirim ke Django");
        },
    });
}






