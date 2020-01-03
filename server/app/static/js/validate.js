$(document).ready(function() {
    const recaptcha = {
        validated: false,
        validate: function(res) {
            this.validated = true;
            return this;
        },
        expired: function() {
            this.validated = false;
            return this;
        },
    };

    window.recaptcha_validate = recaptcha.validate.bind(recaptcha);
    window.recaptcha_expired = recaptcha.expired.bind(recaptcha);
    $.fn.form.settings.rules.recaptcha = function() {
        return recaptcha.validated;
    };

    $('.ui.form').form({
        inline: true,
        fields: {
            username: 'empty',
            password: ['empty', 'length[6]'],
            confirmed: 'match[password]',
            agreement: 'checked',
            recaptcha: 'recaptcha',
        }
    });
});
