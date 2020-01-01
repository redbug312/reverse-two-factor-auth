$(document).ready(function(e){
    $('#steps-step-1').addClass('active');
    $('#steps-step-2').removeClass('active');
    $('#segment-step-1').transition('show');
    $('#segment-step-2').transition('hide');

    $('#submit-step-1').click(function(){
        if($('form').form('is valid')){
            $('#steps-step-1').removeClass('active');
            $('#segment-step-1').transition('fade right', function(){
                $('#steps-step-2').addClass('active');
                $('#segment-step-2').transition('fade left');
            });
        }
    });

    $('#back-to-step-1').click(function(){
        $('#steps-step-2').removeClass('active');
        $('#segment-step-2').transition('fade left', function(){
            $('#steps-step-1').addClass('active');
            $('#segment-step-1').transition('fade right');
        });
    });
});
