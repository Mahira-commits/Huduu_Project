const key = ("<%-num_keys%>");
var keys = key.split(',');
const value = ("<%-num_vals%>");
var values = value.split(',');

var ctx = document.getElementById('lineChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Earnings in $',
            data: [2050, 1900, 2100, 2800, 1800, 2000, 2500, 2600, 2450, 1950, 2300, 2900],
            backgroundColor: [
                'red'

            ],
            borderColor: 'black',

            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});