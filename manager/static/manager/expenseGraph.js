
const data = {
    labels: {{ labels|safe }},
    datasets: [{
        label: 'Expense',
        data: {{ money|safe }},
        borderWidth: 1
}]
};

// config 
const config = {
    type: 'line',
    data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

// render init block
const myChart = new Chart(
    document.getElementById('myChart'),
    config
);

// Instantly assign Chart.js version
const chartVersion = document.getElementById('chartVersion');
chartVersion.innerText = Chart.version;
