# 🏠 Master Real Estate Investment Hub Update Prompt

## 📋 Use This Prompt to Add New Video Series to Your Master Hub

**Copy and paste this prompt, then replace the placeholder content with your specific new video series:**

---

## 🎯 MASTER HUB UPDATE REQUEST

Add a new video series card to the Master Real Estate Investment Hub. The new series should be added to the existing grid of video series cards, maintaining the exact same styling, structure, and functionality.

### 🎨 NEW SERIES CARD STRUCTURE

Add this new card to the existing `.series-grid` section:

```html
<div class="series-card">
    <div class="series-header">
        <span class="series-icon">[YOUR_ICON]</span>
        <div class="series-info">
            <h3 class="series-title">[YOUR_SERIES_TITLE]</h3>
            <p class="series-subtitle">[YOUR_SERIES_SUBTITLE]</p>
        </div>
    </div>
    
    <div class="series-description">
        [YOUR_SERIES_DESCRIPTION]
    </div>
    
    <div class="series-meta">
        <span class="created-date">Created: [CREATION_DATE]</span>
        <span class="version-count">7 Video Versions</span>
    </div>
    
    <div class="duration-buttons">
        <span class="duration-btn">15s</span>
        <span class="duration-btn">25s</span>
        <span class="duration-btn">50s</span>
        <span class="duration-btn">75s</span>
        <span class="duration-btn">90s</span>
        <span class="duration-btn">100s</span>
        <span class="duration-btn">120s</span>
    </div>
    
    <div class="series-actions">
        <a href="[YOUR_LANDING_PAGE_URL]" class="action-btn primary">Watch All Versions</a>
        <a href="[YOUR_SOURCE_URL]" class="action-btn secondary" target="_blank">Source Video</a>
    </div>
</div>
```

### 🎯 CONTENT REQUIREMENTS

#### Series Header
- **Icon**: Choose appropriate emoji for your topic (e.g., 🏠, 📈, 💲, 🆓, 🏡, ⚖️, 🚀, 📊)
- **Title**: Your main series title (e.g., "Rental Property Analysis")
- **Subtitle**: Brief descriptive subtitle (e.g., "From Start to Finish")

#### Series Description
Write a 2-3 sentence description that explains:
- What the series covers
- Key benefits or outcomes
- Target audience or skill level

#### Series Meta
- **Created Date**: Use current date format (e.g., "July 27, 2025")
- **Version Count**: Always "7 Video Versions" (standard across all series)

#### Duration Buttons
Include all 7 duration options:
- 15s, 25s, 50s, 75s, 90s, 100s, 120s

#### Series Actions
- **Watch All Versions**: Link to your main landing page (`[topic]_all_versions.html`)
- **Source Video**: Link to your original YouTube source video

### 🎨 STYLING SPECIFICATIONS

The new card should use the existing CSS classes:

```css
.series-card {
    background: rgba(0, 0, 0, 0.7);
    border: 1px solid rgba(255, 215, 0, 0.3);
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
}

.series-card:hover {
    transform: translateY(-5px);
}

.series-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
}

.series-icon {
    font-size: 2.5rem;
}

.series-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: #ffd700;
    margin-bottom: 5px;
}

.series-subtitle {
    font-size: 0.9rem;
    color: #e6e6fa;
    opacity: 0.8;
}

.series-description {
    margin-bottom: 20px;
    line-height: 1.6;
    color: #e6e6fa;
}

.series-meta {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    font-size: 0.8rem;
    color: #e6e6fa;
    opacity: 0.7;
}

.duration-buttons {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.duration-btn {
    background: #4169e1;
    color: white;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.7rem;
    font-weight: bold;
}

.series-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.action-btn {
    background: linear-gradient(135deg, #4169e1, #6495ed);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(65, 105, 225, 0.3);
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(65, 105, 225, 0.4);
}

.action-btn.secondary {
    background: linear-gradient(135deg, #666, #888);
}

.action-btn.secondary:hover {
    box-shadow: 0 6px 20px rgba(102, 102, 102, 0.4);
}
```

### 📊 STATISTICS UPDATE

After adding the new series, update the statistics in the header:

```html
<div class="stats">
    <div class="stat-item">
        <div class="stat-number">[UPDATED_TOTAL_SERIES]</div>
        <div class="stat-label">Video Series</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">[UPDATED_TOTAL_VIDEOS]</div>
        <div class="stat-label">Total Videos</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">[UPDATED_TOTAL_MINUTES]</div>
        <div class="stat-label">Minutes of Content</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">7</div>
        <div class="stat-label">Duration Formats</div>
    </div>
</div>
```

### 📁 FILE STRUCTURE REQUIREMENTS

Ensure your new series has the following file structure:

```
wordsoftruth/
├── [topic]_all_versions.html              # Main landing page
├── [topic]_15s_shorts.html                # Interactive pages
├── [topic]_25s_shorts.html
├── [topic]_50s_shorts.html
├── [topic]_75s_shorts.html
├── [topic]_90s_shorts.html
├── [topic]_100s_shorts.html
├── [topic]_120s_shorts.html
├── [topic]_shorts_15s_[timestamp].mp4     # Video files
├── [topic]_shorts_25s_[timestamp].mp4
├── [topic]_shorts_50s_[timestamp].mp4
├── [topic]_shorts_75s_[timestamp].mp4
├── [topic]_shorts_90s_[timestamp].mp4
├── [topic]_shorts_100s_[timestamp].mp4
├── [topic]_shorts_120s_[timestamp].mp4
├── [topic]_shorts_15s_[timestamp].m4a     # Audio files
├── [topic]_shorts_25s_[timestamp].m4a
├── [topic]_shorts_50s_[timestamp].m4a
├── [topic]_shorts_75s_[timestamp].m4a
├── [topic]_shorts_90s_[timestamp].m4a
├── [topic]_shorts_100s_[timestamp].m4a
├── [topic]_shorts_120s_[timestamp].m4a
└── create_[topic]_shorts.py               # Generation script
```

### 🎯 INTEGRATION STEPS

1. **Add the new series card** to the existing grid
2. **Update statistics** to reflect the new totals
3. **Verify all links** point to correct files
4. **Test functionality** of all interactive elements
5. **Ensure responsive design** works on mobile devices

### 📋 EXAMPLE COMPLETED CARD

```html
<div class="series-card">
    <div class="series-header">
        <span class="series-icon">🏠</span>
        <div class="series-info">
            <h3 class="series-title">Rental Property Analysis</h3>
            <p class="series-subtitle">From Start to Finish</p>
        </div>
    </div>
    
    <div class="series-description">
        Complete guide to analyzing rental properties for maximum returns. Learn how to evaluate properties, calculate cash flow, and make informed investment decisions. Perfect for both beginners and experienced investors.
    </div>
    
    <div class="series-meta">
        <span class="created-date">Created: July 27, 2025</span>
        <span class="version-count">7 Video Versions</span>
    </div>
    
    <div class="duration-buttons">
        <span class="duration-btn">15s</span>
        <span class="duration-btn">25s</span>
        <span class="duration-btn">50s</span>
        <span class="duration-btn">75s</span>
        <span class="duration-btn">90s</span>
        <span class="duration-btn">100s</span>
        <span class="duration-btn">120s</span>
    </div>
    
    <div class="series-actions">
        <a href="rental_analysis_all_versions.html" class="action-btn primary">Watch All Versions</a>
        <a href="https://www.youtube.com/watch?v=YOUR_SOURCE_VIDEO" class="action-btn secondary" target="_blank">Source Video</a>
    </div>
</div>
```

---

**Replace all placeholder content with your specific series information while maintaining the exact same styling and functionality as existing cards.** 