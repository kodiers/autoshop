/**
 * Created by ewgeniyscherbak on 19.02.15.
 */
$(document).ready(
    function() {
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        document.getElementById('sum').value = parseFloat($input.val())*parseFloat(document.getElementById('price').value)
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        var inp = $input.val(parseInt($input.val()) + 1);
        $input.change();

        document.getElementById('sum').value = parseFloat($input.val())*parseFloat(document.getElementById('price').value);

        return false;
    });
});
$(document).ready(
    function() {
        $('.btn-danger').click(
            function () {
                var table = document.getElementById('myTable');
                var thisrow = this.parentNode.parentNode.rowIndex;
                table.deleteRow(thisrow);
                if (table.rows.length == 1) {
                    table.deleteRow(0);
                    var p = document.createElement('div');
                    p.innerHTML = "<p>Ваша корзина пуста</p>";
                    table.appendChild(p);
                }

            });
    });