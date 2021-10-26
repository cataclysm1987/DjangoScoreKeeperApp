function ToggleTeams() {
    let teamnum = document.getElementById('id_number_of_teams').value;
    if (teamnum === '3') {
        document.querySelectorAll('.team-three').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
        document.querySelectorAll('.team-four').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
        document.querySelectorAll('.team-five').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
    } else if (teamnum === '4') {
        document.querySelectorAll('.team-three').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
        document.querySelectorAll('.team-four').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
        document.querySelectorAll('.team-five').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
    } else if (teamnum === '5') {
        document.querySelectorAll('.team-three').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
        document.querySelectorAll('.team-four').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
        document.querySelectorAll('.team-five').forEach(function (el) {
            el.style.display = 'block';
            el.required = true;
        });
    } else {
        document.querySelectorAll('.team-three').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
        document.querySelectorAll('.team-four').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
        document.querySelectorAll('.team-five').forEach(function (el) {
            el.style.display = 'none';
            el.required = false;
        });
    }
}