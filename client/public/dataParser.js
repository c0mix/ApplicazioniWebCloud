/**
 * Created by Lory on 12/03/17.
 */


function dataParser(x) {
    //document.write(x);
    var x2 = new Date(x);
    //document.write(x2);
    var d = new Date(x2);
    //document.write(d);
    var month = new Array();
        month[0] = "Gennaio";
        month[1] = "Febbraio";
        month[2] = "Marzo";
        month[3] = "Aprile";
        month[4] = "Maggio";
        month[5] = "Giugno";
        month[6] = "Luglio";
        month[7] = "Agosto";
        month[8] = "Settembre";
        month[9] = "Ottobre";
        month[10] = "Novembre";
        month[11] = "Dicembre";

    var weekday = new Array(7);
        weekday[0] = "Domenica";
        weekday[1] = "Lunedì";
        weekday[2] = "Martedì";
        weekday[3] = "Mercoledì";
        weekday[4] = "Giovedì";
        weekday[5] = "Venerdì";
        weekday[6] = "Sabato";

    var giorno = weekday[d.getDay()];
    var numero = d.getDate();
    var mese = month[d.getMonth()];
    var anno = d.getFullYear();

    return [numero, giorno, mese, anno];
    /*
    document.getElementById("mese").innerHTML = mese;
    document.getElementById("anno").innerHTML = anno;
    document.getElementById("giorno").innerHTML = giorno;
    document.getElementById("numero").innerHTML = numero;
    */
}
