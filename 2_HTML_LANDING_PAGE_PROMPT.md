# 🌐 HTML Landing Page Prompt Template

## 📋 Use This Prompt to Generate the Main Landing Page for Your Video Series

**Copy and paste this prompt, then replace the placeholder content with your specific topic:**

---

## 🎯 HTML LANDING PAGE CREATION REQUEST

Create an HTML landing page that is an EXACT TWIN of the BRRRR Investment Property series page, with identical styling, structure, colors, fonts, and functionality. Replace all content with your own topic while maintaining the exact same visual design and layout.

### 🎨 REQUIRED HTML STRUCTURE & STYLING

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[YOUR_TITLE] - Complete Series | ADU-Hub</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #2c1810 0%, #4a1f1f 50%, #2c1810 100%);
            color: #e6e6fa;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }
        
        .main-title {
            font-size: 2.5rem;
            color: #ffd700;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: #e6e6fa;
            margin-bottom: 20px;
        }
        
        .source-link {
            color: #4169e1;
            text-decoration: none;
            font-weight: bold;
        }
        
        .source-link:hover {
            text-decoration: underline;
        }
        
        .versions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .version-card {
            background: rgba(0,0,0,0.7);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }
        
        .version-card:hover {
            transform: translateY(-5px);
        }
        
        .version-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .version-icon {
            font-size: 2rem;
        }
        
        .version-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #ffd700;
        }
        
        .version-duration {
            font-size: 0.9rem;
            color: #e6e6fa;
            opacity: 0.8;
        }
        
        .version-description {
            margin-bottom: 20px;
            line-height: 1.6;
        }
        
        .version-features {
            margin-bottom: 20px;
        }
        
        .feature-list {
            list-style: none;
            padding: 0;
        }
        
        .feature-list li {
            padding: 5px 0;
            color: #e6e6fa;
            opacity: 0.9;
        }
        
        .feature-list li:before {
            content: "✓ ";
            color: #ffd700;
            font-weight: bold;
        }
        
        .version-links {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .version-btn {
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
        
        .version-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(65, 105, 225, 0.4);
        }
        
        .version-btn.secondary {
            background: linear-gradient(135deg, #666, #888);
        }
        
        .version-btn.secondary:hover {
            box-shadow: 0 6px 20px rgba(102, 102, 102, 0.4);
        }
        
        .content-summary-section {
            background: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            padding: 40px;
            margin: 40px 0;
            border: 1px solid rgba(255, 215, 0, 0.2);
        }
        
        .summary-header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .summary-header h2 {
            font-size: 2.2rem;
            color: #ffd700;
            margin-bottom: 10px;
            font-weight: bold;
        }
        
        .summary-subtitle {
            font-size: 1.1rem;
            color: #e6e6fa;
            opacity: 0.9;
        }
        
        .summary-content {
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .summary-section {
            margin-bottom: 35px;
            padding: 25px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 10px;
            border-left: 4px solid #4169e1;
        }
        
        .summary-section h3 {
            font-size: 1.5rem;
            color: #ffd700;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        .summary-section h4 {
            font-size: 1.2rem;
            color: #4169e1;
            margin: 20px 0 10px 0;
            font-weight: bold;
        }
        
        .summary-section p {
            font-size: 1rem;
            color: #e6e6fa;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .summary-section ul, .summary-section ol {
            margin-left: 20px;
            margin-bottom: 15px;
        }
        
        .summary-section li {
            font-size: 1rem;
            color: #e6e6fa;
            line-height: 1.6;
            margin-bottom: 8px;
        }
        
        .summary-section strong {
            color: #ffd700;
            font-weight: bold;
        }
        
        .summary-section ul li::before {
            content: '•';
            color: #4169e1;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .summary-section ol {
            counter-reset: item;
        }
        
        .summary-section ol li {
            counter-increment: item;
            list-style: none;
        }
        
        .summary-section ol li::before {
            content: counter(item) '.';
            color: #4169e1;
            font-weight: bold;
            margin-right: 8px;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }
        
        .footer-text {
            color: #ffd700;
            font-size: 1.1rem;
            margin-bottom: 10px;
        }
        
        .footer-subtext {
            color: #e6e6fa;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            .main-title {
                font-size: 2rem;
            }
            .versions-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            .version-card {
                padding: 20px;
            }
            .content-summary-section {
                padding: 20px;
                margin: 20px 0;
            }
            .summary-header h2 {
                font-size: 1.8rem;
            }
            .summary-section {
                padding: 15px;
                margin-bottom: 25px;
            }
            .summary-section h3 {
                font-size: 1.3rem;
            }
            .summary-section h4 {
                font-size: 1.1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="main-title">[YOUR_MAIN_TITLE_WITH_EMOJI]</h1>
            <p class="subtitle">[YOUR_SUBTITLE]</p>
            <p class="subtitle">Source: <a href="[YOUR_SOURCE_URL]" class="source-link" target="_blank">[YOUR_SOURCE_URL]</a></p>
        </div>

        <div class="versions-grid">
            <!-- Version Cards - Create 7 versions with different durations -->
            <div class="version-card">
                <div class="version-header">
                    <span class="version-icon">⚡</span>
                    <div>
                        <div class="version-title">[VERSION_1_TITLE]</div>
                        <div class="version-duration">[DURATION]</div>
                    </div>
                </div>
                <div class="version-description">
                    [VERSION_1_DESCRIPTION]
                </div>
                <div class="version-features">
                    <ul class="feature-list">
                        <li>[FEATURE_1]</li>
                        <li>[FEATURE_2]</li>
                        <li>[FEATURE_3]</li>
                        <li>[FEATURE_4]</li>
                    </ul>
                </div>
                <div class="version-links">
                    <a href="[HTML_FILE]" class="version-btn">🎬 View Interactive</a>
                    <a href="[VIDEO_FILE]" class="version-btn secondary" download>📥 Download Video</a>
                </div>
            </div>
            <!-- Repeat for all 7 versions -->
        </div>

        <!-- Content Summary Section -->
        <div class="content-summary-section">
            <div class="summary-header">
                <h2>[SUMMARY_TITLE]</h2>
                <p class="summary-subtitle">[SUMMARY_SUBTITLE]</p>
            </div>
            <div class="summary-content">
                <!-- Create multiple summary sections with your content -->
                <div class="summary-section">
                    <h3>[SECTION_1_TITLE]</h3>
                    <p>[SECTION_1_CONTENT]</p>
                    <h4>[SUBSECTION_1_TITLE]</h4>
                    <p>[SUBSECTION_1_CONTENT]</p>
                    <ul>
                        <li><strong>[BULLET_POINT_1]</strong> - [DESCRIPTION]</li>
                        <li><strong>[BULLET_POINT_2]</strong> - [DESCRIPTION]</li>
                        <!-- Add more bullet points -->
                    </ul>
                </div>
                <!-- Repeat for all sections -->
            </div>
        </div>

        <div class="footer">
            <div class="footer-text">🏠 ADU-Hub - Real Estate Investment Education</div>
            <div class="footer-subtext">Transforming real estate knowledge into actionable investment strategies</div>
        </div>
    </div>
</body>
</html>
```

### 🎯 CONTENT STRUCTURE REQUIREMENTS

#### Header Section
- Main title with emoji (🏠 for real estate)
- Subtitle describing the series
- Source URL link

#### Version Cards (7 total)
Create 7 different duration versions:
1. **15 seconds** - Ultra Quick (⚡ icon)
2. **25 seconds** - Quick Analysis (⚡ icon)
3. **50 seconds** - Detailed Analysis (📚 icon)
4. **75 seconds** - Complete Analysis (⛪ icon)
5. **90 seconds** - Extended Analysis (📊 icon)
6. **100 seconds** - Advanced Strategy (🏗️ icon)
7. **120 seconds** - Master Strategy (🚀 icon)

Each card must include:
- Icon and title
- Duration
- Description (2 sentences)
- 4 feature bullet points
- Two buttons: "🎬 View Interactive" and "📥 Download Video"

#### Content Summary Section
Create a comprehensive content summary with:
- Main summary title with emoji
- Multiple sections with h3 headings
- Subsections with h4 headings
- Bullet points and numbered lists
- Rich content with bold formatting

### 🎨 COLOR SCHEME (EXACT MATCH)
- **Background**: Linear gradient from #2c1810 to #4a1f1f to #2c1810
- **Text**: #e6e6fa (light purple/blue)
- **Gold accents**: #ffd700
- **Blue accents**: #4169e1
- **Card backgrounds**: rgba(0,0,0,0.7)
- **Borders**: rgba(255, 215, 0, 0.3)

### 📝 TYPOGRAPHY (EXACT MATCH)
- **Font family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Main title**: 2.5rem, gold color
- **Section headings**: 1.5rem, gold color
- **Subsection headings**: 1.2rem, blue color
- **Body text**: 1rem, light purple/blue

### 📁 FILE NAMING CONVENTION
- HTML files: `[topic]_[duration]s_shorts.html`
- Main landing page: `[topic]_all_versions.html`
- Video files: `[topic]_shorts_[duration]s_[timestamp].mp4`
- Audio files: `[topic]_shorts_[duration]s_[timestamp].m4a`

---

**Replace all placeholder content with your topic while maintaining 100% visual and functional similarity to the original BRRRR landing page.** 