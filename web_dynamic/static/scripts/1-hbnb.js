$(document).ready(function () {
    const amenityIds = {};

    $('input[type=checkbox]').change(function () {
        if (this.checked) {
            amenityIds[$(this).data('id')] = $(this).data('name');
        } else {
            delete amenityIds[$(this).data('id')];
        }

        const amenitiesList = Object.values(amenityIds).join(', ');
        $('div.Amenities h4').text(amenitiesList);
    });
});
