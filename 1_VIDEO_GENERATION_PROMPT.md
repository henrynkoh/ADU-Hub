# 🎬 Video Generation Prompt Template

## 📋 Use This Prompt to Generate New Real Estate Investment Video Series

**Copy and paste this prompt, then replace the placeholder content with your specific topic:**

---

## 🎯 VIDEO SERIES CREATION REQUEST

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

### 📝 CONTENT REQUIREMENTS
Create 7 different script versions with increasing detail:

**15s Version (Ultra Quick):**
- 4 script segments
- Core concept introduction
- Quick profit highlight
- Essential strategy points

**25s Version (Quick Analysis):**
- 5 script segments
- Basic breakdown
- Key investment principles
- Simple profit calculation

**50s Version (Detailed Analysis):**
- 6 script segments
- Step-by-step process
- Cost analysis methods
- Return on investment focus

**75s Version (Complete Analysis):**
- 8 script segments
- Comprehensive breakdown
- Advanced strategies
- Detailed profit calculations

**90s Version (Extended Analysis):**
- 9 script segments
- Market analysis
- Financing options
- Portfolio building

**100s Version (Advanced Strategy):**
- 10 script segments
- Master techniques
- Market timing
- Risk management

**120s Version (Master Strategy):**
- 12 script segments
- Complete masterclass
- Advanced techniques
- Wealth building strategies

### 🐍 PYTHON SCRIPT REQUIREMENTS
Create a Python script named `create_[topic]_shorts.py` with:

1. **Audio Content Arrays**: Define script content for each duration
2. **Daniel Voice**: Use macOS `say` command with Daniel voice
3. **FFmpeg Integration**: Combine audio and create video files
4. **File Naming**: `[topic]_shorts_[duration]s_[timestamp].mp4/m4a`
5. **Error Handling**: Graceful fallback for audio/video creation
6. **Progress Tracking**: Print status updates during generation

### 📁 OUTPUT FILES REQUIRED
- 7 MP4 video files (one per duration)
- 7 M4A audio files (one per duration)
- Audio directories for each duration
- Python generation script

### 🎨 BRANDING SPECIFICATIONS
- **Top Left**: "🏠 REI smart!"
- **Bottom Right**: "📖 ADU-Hub"
- **Color Scheme**: Dark reddish-brown gradient background
- **Typography**: Professional, readable fonts

---

**Replace [YOUR_TOPIC_TITLE] and [YOUR_YOUTUBE_SOURCE_URL] with your specific content, then use this prompt to generate your video series.** 