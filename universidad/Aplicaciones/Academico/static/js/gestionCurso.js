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
    const dataOptions={
        columnDefs:[
            {className:"centered", targets:[0,1,2,3,4]},
            {orderable:false, targets:[4]},
            {searchable:false, targets:[4]},
        ],
        pageLength:5,
        lengthMenu: [
            [5,10, 25, -1],
            [5, 10, 25, 'All'],
        ],
        destroy:true,
    };

    jQuery('#example').DataTable(dataOptions);
});