# 🎮 Interactive HTML Page Prompt Template

## 📋 Use This Prompt to Generate Individual Interactive Video Pages

**Copy and paste this prompt, then replace the placeholder content with your specific topic and duration:**

---

## 🎯 INTERACTIVE HTML PAGE CREATION REQUEST

Create an interactive HTML page for the [DURATION] version of your video series with script synchronization, audio playback, and progress tracking. This page should be an EXACT TWIN of the BRRRR Investment Property interactive pages.

### 🎨 REQUIRED HTML STRUCTURE & STYLING

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

### 🎯 CONTENT REQUIREMENTS

#### Script Content Arrays
Replace the placeholder arrays with your actual content:

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

### 🎨 FEATURES INCLUDED

1. **Audio Integration**: Full audio playback with Daniel voice narration
2. **Script Synchronization**: Real-time script display synchronized with audio
3. **Progress Tracking**: Visual progress bar with percentage completion
4. **Interactive Controls**: Start, pause, reset, and audio toggle buttons
5. **Visual Effects**: Text highlighting, floating elements, and smooth animations
6. **Responsive Design**: Mobile-optimized layout and controls
7. **Branding**: "🏠 REI smart!" and "📖 ADU-Hub" branding elements

### 📁 FILE NAMING CONVENTION
- HTML file: `[topic]_[duration]s_shorts.html`
- Audio file: `[topic]_shorts_[duration]s_[timestamp].m4a`

---

**Replace all placeholder content with your specific topic, duration, script segments, and audio file path while maintaining 100% functionality.** 