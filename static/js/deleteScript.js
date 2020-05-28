/**
 * function untuk menghapus baris pada data balai.
 * @param id_balai Primary Key
 * @param token CSRF token
 */
function deleteRowBalai(id_balai, token) {
    console.log(id_balai)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/balai-pengobatan/tabel/delete/",
        data: { id_balai: id_balai },
        success: function () {
            console.log("Data sukses di kirim ke Django");
        },
    });
}

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
 * function untuk menghapus baris pada data obat.
 * @param id_apotek Primary Key
 * @param token CSRF token
 */
function deleteRowApotek(id_apotek, token) {
    console.log(id_apotek)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/apotek/tabel/delete/",
        data: {id_apotek : id_apotek},
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
        url: "/list-produk-dibeli/tabel/delete/",
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

/**
 * function untuk menghapus baris pada data obat.
 * @param id_pengantaran Primary Key
 * @param token CSRF token
 */
function deleteRowPengantaranFarmasi(id_pengantaran, token) {
    console.log(id_pengantaran)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/pengantaran-farmasi/tabel/delete/",
        data: { id_pengantaran: id_pengantaran },
        success: function () {
            console.log("Data sukses di kirim ke Django");
        },
    });
}





