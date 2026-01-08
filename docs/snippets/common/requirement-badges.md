<!-- This has to be here instead of the snippet since they run before plugins (macros) -->
{% if page.meta.get('priority') and page.meta.get('show_badges', true) != false %}
<div class="requirement-badges">
<span class="priority-badge priority-{{ page.meta.get('priority') | lower }}">{{ page.meta.get('priority') }}</span>
{% if page.meta.get('phase') is not none %}<span class="phase-badge">Phase {{ page.meta.get('phase') }}</span>{% endif %}
{% if page.meta.get('status') %}<span class="status-badge status-{{ page.meta.get('status') | replace(' ', '-') | lower }}">{{ page.meta.get('status') | replace('-', ' ') | title }}</span>{% endif %}
</div>

---
{% endif %}