/**
 * function untuk menghapus baris pada data.
 * @param pk : Primary Key
 */
function deleteRowObat(pk, token) {
    console.log(pk)

    $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        url: "/obat/tabel/delete/",
        data: {id_target : pk},
        success: function () {
            console.log("Data sukses di kirim ke Django");
        },
        complete: function () {
            alert("Data Sukses Dihapus!");
        }
    });
};





