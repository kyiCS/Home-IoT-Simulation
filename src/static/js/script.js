$(function() {
    console.log("We in here!")


    // outsideData = (api call data)
    // outsideTemperature.innerHTML = outsideData;

    let increase = document.getElementById('increase-temp');
    let decrease = document.getElementById('decrease-temp');
    let setTemperature = document.getElementById('set-temp');
    let outsideTemperature = document.getElementById('out-temp')

    increase.addEventListener('click', function(e){
    })

    decrease.addEventListener('click', function(e){
    })



    $('.devices')
    .bootstrapToggle('off')
    .change(function(e){
        let isChecked = $(this).prop('checked')
        console.log(`${e.target.id} is checked: ${isChecked}`);
    })

    $('.exits')
    .bootstrapToggle('off')
    .change(function(e){
        let isChecked = $(this).prop('checked')
        console.log(`${e.target.id} is checked: ${isChecked}`);

    })

    document.addEventListener('click', function(event){
        if (!event.target.closest('#main-room')) return;
	    console.log(event.target);
    })
})
