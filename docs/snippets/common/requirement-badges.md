<!-- This has to be here instead of the snippet since they run before plugins (macros) -->
{% if page.meta.priority and page.meta.get('show_badges', true) != false %}
<div class="requirement-badges">
<span class="priority-badge priority-{{ page.meta.priority | lower }}">{{ page.meta.priority }}</span>
{% if page.meta.phase %}<span class="phase-badge">Phase {{ page.meta.phase }}</span>{% endif %}
{% if page.meta.status %}<span class="status-badge status-{{ page.meta.status | replace(' ', '-') | lower }}">{{ page.meta.status | replace('-', ' ') | title }}</span>{% endif %}
</div>

---
{% endif %}