/**
 * Created by emanuelziga on 31/7/16.
 */

(function($) {

$( document ).ready(function($){

    $('html').on('click','.pdfBtn', function () {
        event.preventDefault();
        var id=$(this).closest('tr')[0].cells[1].outerText;

        window.open(`/orderpdf/${id}/`)

    });

    $('html').on('click','.editBtn', function () {

        var id=$(this).closest('tr')[0].cells[1].outerText;

        console.log(`El id de salida es ${id}`);

        localStorage.order_to_edit=JSON.stringify({id:id});


    });


});

})(django.jQuery);