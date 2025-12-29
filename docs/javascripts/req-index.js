// ABOUTME: Interactive requirements index with filtering and sorting
// ABOUTME: Provides search, phase filter, priority filter, and sortable columns

document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('requirements-table');
    if (!table) return; // Only run on requirements index page

    const searchInput = document.getElementById('req-search');
    const phaseFilter = document.getElementById('phase-filter');
    const priorityFilter = document.getElementById('priority-filter');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    // Sorting state
    let currentSort = { column: null, direction: 'asc' };

    // Priority order for sorting
    const priorityOrder = { 'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3 };

    // Filter function
    function filterTable() {
        const searchTerm = searchInput.value.toLowerCase();
        const phaseValue = phaseFilter.value;
        const priorityValue = priorityFilter.value;

        rows.forEach(row => {
            const phase = row.dataset.phase;
            const priority = row.dataset.priority;
            const docnum = row.dataset.docnum.toLowerCase();
            const title = row.dataset.title.toLowerCase();

            const matchesSearch = !searchTerm || docnum.includes(searchTerm) || title.includes(searchTerm);
            const matchesPhase = !phaseValue || phase === phaseValue;
            const matchesPriority = !priorityValue || priority === priorityValue;

            if (matchesSearch && matchesPhase && matchesPriority) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    // Sort function
    function sortTable(column) {
        // Toggle direction if clicking same column
        if (currentSort.column === column) {
            currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
        } else {
            currentSort.column = column;
            currentSort.direction = 'asc';
        }

        // Sort rows
        const sortedRows = rows.slice().sort((a, b) => {
            let aVal, bVal;

            switch(column) {
                case 'priority':
                    aVal = priorityOrder[a.dataset.priority] || 99;
                    bVal = priorityOrder[b.dataset.priority] || 99;
                    break;
                case 'phase':
                    aVal = parseInt(a.dataset.phase);
                    bVal = parseInt(b.dataset.phase);
                    break;
                case 'docnum':
                    aVal = a.dataset.docnum.toLowerCase();
                    bVal = b.dataset.docnum.toLowerCase();
                    break;
                case 'title':
                    aVal = a.dataset.title.toLowerCase();
                    bVal = b.dataset.title.toLowerCase();
                    break;
                default:
                    return 0;
            }

            if (aVal < bVal) return currentSort.direction === 'asc' ? -1 : 1;
            if (aVal > bVal) return currentSort.direction === 'asc' ? 1 : -1;
            return 0;
        });

        // Clear and re-append sorted rows
        tbody.innerHTML = '';
        sortedRows.forEach(row => tbody.appendChild(row));

        // Update sort icons
        document.querySelectorAll('.sortable').forEach(th => {
            const icon = th.querySelector('.sort-icon');
            if (th.dataset.sort === column) {
                icon.textContent = currentSort.direction === 'asc' ? '↑' : '↓';
                th.classList.add('sorted');
            } else {
                icon.textContent = '⇅';
                th.classList.remove('sorted');
            }
        });
    }

    // Event listeners
    searchInput.addEventListener('input', filterTable);
    phaseFilter.addEventListener('change', filterTable);
    priorityFilter.addEventListener('change', filterTable);

    document.querySelectorAll('.sortable').forEach(th => {
        th.addEventListener('click', () => sortTable(th.dataset.sort));
        th.style.cursor = 'pointer';
    });
});
