(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Seguro que desea eliminar el curso?');
            if (!confirmacion)
                e.preventDefault();
        })

    });

})();

jQuery(document).ready(function () {

    

//Spanish

    const dataOptions={
        columnDefs:[
            {className:"centered", targets:[0,1,2,3,4]},
            {orderable:false, targets:[0,4]},
            {searchable:false, targets:[4]},
        ],
        pageLength:5,
        lengthMenu: [
            [5,10, 25, -1],
            [5, 10, 25, 'Todos'],
        ],
        destroy:true,
        language: {
            "sProcessing":    "Procesando...",
            "sLengthMenu":    "Mostrar _MENU_ registros",
            "sZeroRecords":   "No se encontraron resultados",
            "sEmptyTable":    "Ningún dato disponible en esta tabla",
            "sInfo":          "Mostrando _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":     "Mostrando  0 de un total de 0 registros",
            /*"sInfoFiltered":  "(filtrado de un total de _MAX_ registros)",*/
            "sInfoFiltered":  "",
            "sInfoPostFix":   "",
            "sSearch":        "Buscar:",
            "sUrl":           "",
            "sInfoThousands":  ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst":    "Primero",
                "sLast":    "Último",
                "sNext":    "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    };

    jQuery('#example').DataTable(dataOptions);
});