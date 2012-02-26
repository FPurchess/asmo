(function ($) {

    $(document).ready(function () {

        var pre = $('pre');
        var html = pre.html();

        function write(data, send) {
            html = html
                + (send ? '<span class="out">' : '<span class="in">')
                + (new Date()).toTimeString().substr(0, 9)
                + data + '</span>' + "\n";
            pre.html(html).scrollTop(html.length);
        }

        $('form').live('submit', function (e) {
            e.preventDefault();

            var data = $('#serial').val();
            write(data, true);
            $.post('/serial', {serial:data});

            return false;
        });

        window.setInterval(function () {
            $.get('/serial', function (data) {
                write(data, false);
            });
        }, speed);

    });
})(jQuery);

