document.getElementById('hide-excluded').addEventListener('change', function() {
const hideExcluded = this.checked;
const rows = document.querySelectorAll('#requirements-table tbody tr');

rows.forEach(row => {
    const isExcluded = row.dataset.exclude === 'true';
    if (hideExcluded && isExcluded) {
    row.style.display = 'none';
    } else {
    row.style.display = '';
    }
});
});

// Run on page load to hide excluded items by default
document.addEventListener('DOMContentLoaded', function() {
document.getElementById('hide-excluded').dispatchEvent(new Event('change'));
});