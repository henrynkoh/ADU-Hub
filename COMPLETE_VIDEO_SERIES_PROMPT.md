# 🎬 Complete Real Estate Video Series Creation Prompt

## 📋 Copy-Paste This Complete Prompt to Create New Video Series

**Replace all placeholders with your specific content and use this prompt to generate complete video series:**

---

## 🎯 COMPLETE VIDEO SERIES CREATION REQUEST

Create a complete real estate investment video series with the following specifications:

### 📝 BASIC INFORMATION
- **Title**: [YOUR_TOPIC_TITLE] (e.g., "Rental Property Analysis From Start To Finish!")
- **Source URL**: [YOUR_YOUTUBE_SOURCE_URL]
- **Theme**: Real estate investment education
- **Voice**: Daniel (British accent - human-sounding)
- **Style**: Professional broadcast-ready with synchronized script display

### 🎬 PRODUCTION SPECIFICATIONS
- **Format**: YouTube Shorts (9:16 aspect ratio)
- **Resolution**: 1080x1920
- **Frame Rate**: 30 FPS
- **Background**: Dark reddish-brown gradient (#2c1810 to #4a1f1f)
- **Audio Quality**: Professional broadcast standard (AAC, 128k)
- **Duration Versions**: 15s, 25s, 50s, 75s, 90s, 100s, 120s

### 🐍 PYTHON SCRIPT REQUIREMENTS
Create `create_[topic]_shorts.py` with:
1. **Audio Content Arrays**: Define script content for each duration
2. **Daniel Voice**: Use macOS `say` command with Daniel voice
3. **FFmpeg Integration**: Combine audio and create video files
4. **File Naming**: `[topic]_shorts_[duration]s_[timestamp].mp4/m4a`
5. **Error Handling**: Graceful fallback for audio/video creation

### 📝 CONTENT REQUIREMENTS
Create 7 different script versions with increasing detail:

**15s Version (Ultra Quick):** 4 script segments - Core concept introduction
**25s Version (Quick Analysis):** 5 script segments - Basic breakdown
**50s Version (Detailed Analysis):** 6 script segments - Step-by-step process
**75s Version (Complete Analysis):** 8 script segments - Comprehensive breakdown
**90s Version (Extended Analysis):** 9 script segments - Market analysis
**100s Version (Advanced Strategy):** 10 script segments - Master techniques
**120s Version (Master Strategy):** 12 script segments - Complete masterclass

---

## 🌐 HTML LANDING PAGE REQUIREMENTS

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

---

## 🎮 INTERACTIVE HTML PAGE REQUIREMENTS

### 🎨 INTERACTIVE PAGE STRUCTURE

Create 7 individual HTML pages with this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[YOUR_TITLE] - [DURATION] Version | ADU-Hub</title>
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
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            width: 85%;
            max-width: 500px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 215, 0, 0.3);
            position: relative;
            overflow: hidden;
        }

        .floating-elements {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .floating-element {
            position: absolute;
            font-size: 2rem;
            opacity: 0.1;
            animation: float 6s ease-in-out infinite;
        }

        .floating-element:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
        .floating-element:nth-child(2) { top: 20%; right: 15%; animation-delay: 1s; }
        .floating-element:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 2s; }
        .floating-element:nth-child(4) { bottom: 20%; right: 10%; animation-delay: 3s; }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .content {
            position: relative;
            z-index: 2;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .title {
            font-size: 1.8rem;
            color: #ffd700;
            margin-bottom: 10px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }

        .subtitle {
            font-size: 1rem;
            color: #e6e6fa;
            opacity: 0.9;
        }

        .script-container {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid rgba(255, 215, 0, 0.2);
            min-height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .script-text {
            font-size: 1.8rem;
            color: #e6e6fa;
            text-align: center;
            font-style: italic;
            line-height: 1.4;
            transition: all 0.3s ease;
        }

        .script-text.highlight {
            color: #ffd700;
            transform: scale(1.05);
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }

        .progress-container {
            margin-bottom: 25px;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 10px;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4169e1, #6495ed);
            width: 0%;
            transition: width 0.3s ease;
            border-radius: 4px;
        }

        .progress-text {
            text-align: center;
            font-size: 0.9rem;
            color: #e6e6fa;
            font-weight: bold;
        }

        .controls {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .control-btn {
            background: linear-gradient(135deg, #4169e1, #6495ed);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(65, 105, 225, 0.3);
        }

        .control-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(65, 105, 225, 0.4);
        }

        .control-btn:disabled {
            background: linear-gradient(135deg, #666, #888);
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .audio-toggle {
            background: rgba(0, 0, 0, 0.5);
            color: #e6e6fa;
            border: 1px solid rgba(255, 215, 0, 0.3);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .audio-toggle:hover {
            background: rgba(255, 215, 0, 0.1);
        }

        .status {
            text-align: center;
            font-size: 1rem;
            color: #ffd700;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .branding {
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 1.1rem;
            color: #ffd700;
            font-weight: bold;
        }

        .logo {
            position: absolute;
            bottom: 20px;
            right: 20px;
            font-size: 0.9rem;
            color: #ffd700;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .container {
                width: 95%;
                padding: 20px;
            }
            
            .title {
                font-size: 1.5rem;
            }
            
            .script-text {
                font-size: 1.5rem;
            }
            
            .controls {
                flex-direction: column;
                align-items: center;
            }
            
            .control-btn {
                width: 100%;
                max-width: 200px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="floating-elements">
            <div class="floating-element">📖</div>
            <div class="floating-element">🎤</div>
            <div class="floating-element">✨</div>
            <div class="floating-element">🌿</div>
        </div>

        <div class="content">
            <!-- Audio element for narration -->
            <audio id="narrationAudio" preload="auto">
                <source src="[AUDIO_FILE]" type="audio/mp4">
                Your browser does not support the audio element.
            </audio>
            
            <div class="header">
                <h1 class="title">[YOUR_TITLE]</h1>
                <p class="subtitle">[DURATION_DESCRIPTION] - [DURATION] Seconds</p>
            </div>

            <div class="script-container">
                <div id="scriptText" class="script-text">Ready to start</div>
            </div>

            <div class="progress-container">
                <div class="progress-bar">
                    <div id="progressFill" class="progress-fill"></div>
                </div>
                <div id="progressText" class="progress-text">0% Complete</div>
            </div>

            <div id="status" class="status">Ready to start</div>

            <div class="controls">
                <button id="startBtn" class="control-btn">START</button>
                <button id="pauseBtn" class="control-btn" disabled>PAUSE</button>
                <button id="resetBtn" class="control-btn">RESET</button>
            </div>

            <button id="audioToggle" class="audio-toggle">🔊 Audio: ON</button>

        </div>

        <div class="branding">🏠 REI smart!</div>
        <div class="logo">📖 ADU-Hub</div>
    </div>

    <script>
        let currentIndex = 0;
        let isPlaying = false;
        let audioEnabled = true;
        let intervalId = null;

        const scriptText = document.getElementById('scriptText');
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');
        const status = document.getElementById('status');
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const resetBtn = document.getElementById('resetBtn');
        const audioToggle = document.getElementById('audioToggle');
        const narrationAudio = document.getElementById('narrationAudio');

        // SCRIPT CONTENT - REPLACE WITH YOUR CONTENT
        const scriptContent = [
            "[SCRIPT_SEGMENT_1]",
            "[SCRIPT_SEGMENT_2]",
            "[SCRIPT_SEGMENT_3]",
            "[SCRIPT_SEGMENT_4]",
            "[SCRIPT_SEGMENT_5]",
            "[SCRIPT_SEGMENT_6]",
            "[SCRIPT_SEGMENT_7]",
            "[SCRIPT_SEGMENT_8]"
        ];
        
        // SCRIPT DURATIONS - REPLACE WITH YOUR DURATIONS
        const scriptDurations = [4, 4, 4, 4, 4, 4, 4, 4]; // Total: [DURATION] seconds

        function updateProgress() {
            const totalDuration = scriptDurations.reduce((a, b) => a + b, 0);
            const elapsed = scriptDurations.slice(0, currentIndex).reduce((a, b) => a + b, 0);
            const currentElapsed = elapsed + (scriptDurations[currentIndex] || 0);
            const percentage = Math.min((currentElapsed / totalDuration) * 100, 100);
            
            progressFill.style.width = percentage + '%';
            progressText.textContent = Math.round(percentage) + '% Complete';
        }

        function highlightText() {
            scriptText.classList.add('highlight');
            setTimeout(() => {
                scriptText.classList.remove('highlight');
            }, 500);
        }

        function playScript() {
            if (currentIndex >= scriptContent.length) {
                stopScript();
                return;
            }

            scriptText.textContent = scriptContent[currentIndex];
            highlightText();
            updateProgress();

            if (audioEnabled) {
                status.textContent = `Playing: ${scriptContent[currentIndex]}`;
            }

            setTimeout(() => {
                currentIndex++;
                if (isPlaying) {
                    playScript();
                }
            }, scriptDurations[currentIndex] * 1000);
        }

        function startScript() {
            if (isPlaying) return;
            
            isPlaying = true;
            startBtn.disabled = true;
            pauseBtn.disabled = false;
            status.textContent = 'Playing...';
            
            // Start audio playback
            if (audioEnabled && narrationAudio) {
                narrationAudio.currentTime = 0;
                narrationAudio.play().catch(e => {
                    console.log('Audio play failed:', e);
                });
            }
            
            // Auto-start script after 2 seconds
            setTimeout(() => {
                playScript();
            }, 2000);
        }

        function pauseScript() {
            isPlaying = false;
            startBtn.disabled = false;
            pauseBtn.disabled = true;
            status.textContent = 'Paused';
            
            // Pause audio playback
            if (narrationAudio) {
                narrationAudio.pause();
            }
        }

        function resetScript() {
            isPlaying = false;
            currentIndex = 0;
            startBtn.disabled = false;
            pauseBtn.disabled = true;
            status.textContent = 'Ready to start';
            scriptText.textContent = scriptContent[0];
            progressFill.style.width = '0%';
            progressText.textContent = '0% Complete';
            
            // Reset audio
            if (narrationAudio) {
                narrationAudio.pause();
                narrationAudio.currentTime = 0;
            }
        }

        function toggleAudio() {
            audioEnabled = !audioEnabled;
            audioToggle.textContent = audioEnabled ? '🔊 Audio: ON' : '🔇 Audio: OFF';
            
            // Pause audio if turning off
            if (!audioEnabled && narrationAudio) {
                narrationAudio.pause();
            }
        }

        // Event listeners
        startBtn.addEventListener('click', startScript);
        pauseBtn.addEventListener('click', pauseScript);
        resetBtn.addEventListener('click', resetScript);
        audioToggle.addEventListener('click', toggleAudio);

        // Initialize
        resetScript();
    </script>
</body>
</html>
```

### 🎯 SCRIPT CONTENT TEMPLATES

**For 15s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]"
];
const scriptDurations = [4, 4, 4, 3]; // Total: 15 seconds
```

**For 25s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]"
];
const scriptDurations = [5, 5, 5, 5, 5]; // Total: 25 seconds
```

**For 50s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]",
    "[Your sixth script segment]"
];
const scriptDurations = [8, 8, 8, 8, 8, 10]; // Total: 50 seconds
```

**For 75s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]",
    "[Your sixth script segment]",
    "[Your seventh script segment]",
    "[Your eighth script segment]"
];
const scriptDurations = [8, 8, 8, 8, 8, 8, 8, 19]; // Total: 75 seconds
```

**For 90s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]",
    "[Your sixth script segment]",
    "[Your seventh script segment]",
    "[Your eighth script segment]",
    "[Your ninth script segment]"
];
const scriptDurations = [8, 8, 8, 8, 8, 8, 8, 8, 26]; // Total: 90 seconds
```

**For 100s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]",
    "[Your sixth script segment]",
    "[Your seventh script segment]",
    "[Your eighth script segment]",
    "[Your ninth script segment]",
    "[Your tenth script segment]"
];
const scriptDurations = [8, 8, 8, 8, 8, 8, 8, 8, 8, 28]; // Total: 100 seconds
```

**For 120s Version:**
```javascript
const scriptContent = [
    "[Your first script segment]",
    "[Your second script segment]",
    "[Your third script segment]",
    "[Your fourth script segment]",
    "[Your fifth script segment]",
    "[Your sixth script segment]",
    "[Your seventh script segment]",
    "[Your eighth script segment]",
    "[Your ninth script segment]",
    "[Your tenth script segment]",
    "[Your eleventh script segment]",
    "[Your twelfth script segment]"
];
const scriptDurations = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 32]; // Total: 120 seconds
```

---

## 🏠 MASTER HUB UPDATE REQUIREMENTS

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

### 📊 STATISTICS UPDATE

After adding the new series, update the statistics:

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

---

## 📁 REQUIRED FILE STRUCTURE

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
├── create_[topic]_shorts.py               # Generation script
└── MASTER_REAL_ESTATE_LANDING.html        # Master hub (updated)
```

---

## 🎨 BRANDING AND STYLING STANDARDS

### **Color Scheme**
- **Background**: Linear gradient from #2c1810 to #4a1f1f to #2c1810
- **Text**: #e6e6fa (light purple/blue)
- **Gold accents**: #ffd700
- **Blue accents**: #4169e1
- **Card backgrounds**: rgba(0,0,0,0.7)
- **Borders**: rgba(255, 215, 0, 0.3)

### **Typography**
- **Font family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Main title**: 2.5rem, gold color
- **Section headings**: 1.5rem, gold color
- **Subsection headings**: 1.2rem, blue color
- **Body text**: 1rem, light purple/blue

### **Branding Elements**
- **Top Left**: "🏠 REI smart!"
- **Bottom Right**: "📖 ADU-Hub"
- **Footer**: "🏠 ADU-Hub - Real Estate Investment Education"

---

## 🚀 COMPLETE WORKFLOW

### **Step 1: Video Generation**
1. Use Python script to create all video and audio files
2. Verify all 7 MP4 and 7 M4A files are created
3. Test video playback and audio quality

### **Step 2: Create Landing Page**
1. Use HTML template to create main landing page
2. Replace all placeholders with your content
3. Add comprehensive content summary sections
4. Test all links and functionality

### **Step 3: Create Interactive Pages**
1. Create 7 individual HTML pages using template
2. Replace script content and durations for each version
3. Update audio file paths
4. Test script synchronization and audio playback

### **Step 4: Update Master Hub**
1. Add new series card to existing grid
2. Update statistics to reflect new totals
3. Verify all links point to correct files
4. Test responsive design and functionality

### **Step 5: Quality Assurance**
1. Test all video files play correctly
2. Verify audio works in interactive pages
3. Test script synchronization and controls
4. Check mobile compatibility
5. Verify all navigation links work

---

**Replace all placeholder content with your specific topic, content, and file paths while maintaining 100% visual and functional similarity to the original BRRRR Investment Property series.** 