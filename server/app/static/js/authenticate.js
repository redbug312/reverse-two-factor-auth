$(document).ready(function(e) {
    const $form = $('.ui.form');
    $form.attr('onsubmit', 'return false;');

    const $steps = [, $('.step.step-1'), $('.step.step-2') ];
    const $segments = [, $('.segment.step-1'), $('.segment.step-2') ];
    $steps[1].addClass('active');
    $steps[2].removeClass('active');
    $segments[1].transition('show');
    $segments[2].transition('hide');

    $('#forward-step-2').click(function() {
        if(!$form.form('is valid')) { return; }
        $steps[1].removeClass('active');
        $segments[1].transition('fade right', function() {
            $steps[2].addClass('active');
            $segments[2].transition('fade left');
            $form.form('add rule', 'broker', 'checked');
            $form.form('add rule', 'badges', 'empty');
            $form.form('remove rule', 'recaptcha', 'recaptcha');
            $form.attr('onsubmit', null);
        });
    });

    $('#backward-step-1').click(function() {
        $steps[2].removeClass('active');
        $segments[2].transition('fade left', function() {
            $steps[1].addClass('active');
            $segments[1].transition('fade right');
            $form.form('add rule', 'recaptcha', 'recaptcha');
            $form.form('remove rule', 'broker', 'checked');
            $form.form('remove rule', 'badges', 'empty');
            $form.attr('onsubmit', 'return false;');
        });
    });

    $('#broker-select .button').click(function() {
        const $broker_button = $(this);
        const $broker_each_button = $('#broker-select .button');
        const $badges_menu = $('#badges-select .menu');
        $broker_button.addClass('loading');

        $.ajax({
            url: $(this).attr('data-auth-url'),
            crossDomain: true,
            dataType: 'json',
            timeout: 5000
        }).done(function(res) {
            $broker_each_button.removeClass('positive');
            $broker_button.addClass('positive');
            $broker_button.children('i.icon').addClass('check');
            $broker_button.next().attr('checked', 'checked');
            $broker_button.attr('data-tooltip', null);
            $badges_menu.parent().removeClass('disabled').transition('glow');
            $badges_menu.empty();
            $.each(res.auths, function(_, auth) {
                $badges_menu.append(`
                    <div class='item' data-value='${auth.badges.join(' ')}'>
                        <i class='${auth.badges[0]} icon'></i>
                        <i class='${auth.badges[1]} icon'></i>
                        <i class='${auth.badges[2]} icon'></i>
                        <b>${auth.expired}</b>
                    </div>
                `);
            });
        }).fail(function() {
            $broker_button.children('i.icon').addClass('close');
            $broker_button.attr('data-tooltip',
                                'Broker is offline. Click to retry.')
        }).always(function() {
            $broker_button.removeClass('loading');
            $broker_button.children('i.icon').removeClass('search');
        });
    });

    $('.dropdown').dropdown();
    $('#broker-select .button').popup();
});
