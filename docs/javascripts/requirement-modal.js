// ABOUTME: Modal popup handler for missing requirement files
// ABOUTME: Intercepts requirement link clicks and shows friendly message instead of 404

document.addEventListener('DOMContentLoaded', function() {
    // Create modal HTML structure
    const modalHTML = `
        <div id="req-not-available-modal" class="req-modal">
            <div class="req-modal-content">
                <span class="req-modal-close">&times;</span>
                <div class="req-modal-header">
                    <svg class="req-modal-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="12"></line>
                        <line x1="12" y1="16" x2="12.01" y2="16"></line>
                    </svg>
                    <h2>Requirement Not Available</h2>
                </div>
                <div class="req-modal-body">
                    <p>This requirement document is not currently available.</p>
                    <p class="req-modal-details">The requirement may be:</p>
                    <ul>
                        <li>Still being drafted</li>
                        <li>Under review</li>
                        <li>Scheduled for a future release</li>
                    </ul>
                    <p class="req-modal-footer-text">Please check back later or contact the project team for more information.</p>
                </div>
                <div class="req-modal-footer">
                    <button class="req-modal-button req-modal-button-primary">OK</button>
                </div>
            </div>
        </div>
    `;

    // Insert modal into page
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const modal = document.getElementById('req-not-available-modal');
    const closeBtn = modal.querySelector('.req-modal-close');
    const okBtn = modal.querySelector('.req-modal-button-primary');

    // Function to show modal
    function showModal() {
        modal.style.display = 'block';
        // Prevent body scroll when modal is open
        document.body.style.overflow = 'hidden';
    }

    // Function to hide modal
    function hideModal() {
        modal.style.display = 'none';
        document.body.style.overflow = '';
    }

    // Close modal on X click
    closeBtn.addEventListener('click', hideModal);

    // Close modal on OK button click
    okBtn.addEventListener('click', hideModal);

    // Close modal when clicking outside content
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            hideModal();
        }
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            hideModal();
        }
    });

    // Intercept clicks on requirement links
    document.addEventListener('click', function(event) {
        // Check if clicked element is a link to a requirement file
        const link = event.target.closest('a[href*="req-"]');

        if (!link) return;

        const href = link.getAttribute('href');

        // Only intercept links that look like requirement files
        if (!href || !href.match(/req-.*\.md$/)) return;

        // Prevent default navigation
        event.preventDefault();

        // Try to fetch the URL to check if it exists
        const fullUrl = new URL(href, window.location.href);

        fetch(fullUrl.pathname, { method: 'HEAD' })
            .then(response => {
                if (response.ok) {
                    // File exists, navigate normally
                    window.location.href = href;
                } else {
                    // File doesn't exist, show modal
                    showModal();
                }
            })
            .catch(() => {
                // Error fetching (likely 404), show modal
                showModal();
            });
    });
});
