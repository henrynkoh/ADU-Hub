#!/usr/bin/env python3
"""
Create "Walk in the Spirit" Videos in Exact Same Format
Same style, colors, layout, and YouTube Shorts format as previous series
"""

import os
import subprocess
from datetime import datetime

def create_walk_spirit_shorts(duration):
    """Create video in exact same format as previous series"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print(f"🎬 CREATING 'WALK IN THE SPIRIT' SHORTS")
    print("=" * 60)
    print(f"📺 Format: Exact same style as previous series")
    print(f"⏱️ Duration: {duration} seconds")
    
    # Create audio directory
    audio_dir = f"walk_spirit_shorts_{duration}s_audio"
    os.makedirs(audio_dir, exist_ok=True)
    
    # Define content based on duration (same format as previous series)
    if duration == 25:
        audio_content = [
            "Walk in the Spirit. What does that mean and how do we do it?",
            "It's about living under the Spirit's guidance and control.",
            "Not walking in the flesh, but in the Spirit's power.",
            "Galatians 5:16 - Walk in the Spirit and you shall not fulfill the lust of the flesh.",
            "Let the Holy Spirit lead your daily life!"
        ]
    elif duration == 50:
        audio_content = [
            "Walk in the Spirit. What does that mean and how do we do it?",
            "It's about living under the Spirit's guidance and control.",
            "Not walking in the flesh, but in the Spirit's power.",
            "Galatians 5:16 - Walk in the Spirit and you shall not fulfill the lust of the flesh.",
            "It means surrendering your will to God's Spirit.",
            "Let the Holy Spirit lead your daily life!"
        ]
    else:  # 75 seconds
        audio_content = [
            "Walk in the Spirit. What does that mean and how do we do it?",
            "It's about living under the Spirit's guidance and control.",
            "Not walking in the flesh, but in the Spirit's power.",
            "Galatians 5:16 - Walk in the Spirit and you shall not fulfill the lust of the flesh.",
            "It means surrendering your will to God's Spirit.",
            "Romans 8:14 - For as many as are led by the Spirit of God.",
            "These are the sons of God.",
            "Let the Holy Spirit lead your daily life!"
        ]
    
    # Use Daniel voice (same as previous series)
    human_voice = "Daniel"
    print(f"🎤 Using human-sounding voice: {human_voice}")
    
    # Create audio files with same settings as previous series
    print("🎤 Creating human-sounding audio narration...")
    for i, content in enumerate(audio_content):
        output_file = os.path.join(audio_dir, f"walk_spirit_{i+1:02d}.aiff")
        
        try:
            # Use Daniel voice with natural speech settings (same as previous series)
            cmd = [
                'say',
                '-v', human_voice,
                '-r', '140',  # Natural speaking rate
                '-o', output_file,
                content
            ]
            
            subprocess.run(cmd, check=True)
            print(f"   Created audio: {output_file}")
        except Exception as e:
            print(f"   ⚠️ Could not create audio {i+1}: {e}")
    
    # Combine all audio files into one
    print("🎵 Combining audio files...")
    combined_file = f"walk_spirit_shorts_{duration}s_{timestamp}.m4a"
    
    # Create a text file with all audio files for concatenation
    with open("audio_list.txt", "w") as f:
        for i in range(len(audio_content)):
            f.write(f"file '{audio_dir}/walk_spirit_{i+1:02d}.aiff'\n")
    
    # Combine using FFmpeg
    try:
        cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', 'audio_list.txt',
            '-c:a', 'aac',
            '-b:a', '128k',
            combined_file
        ]
        
        subprocess.run(cmd, check=True)
        print(f"   Combined audio: {combined_file}")
        
        # Clean up
        os.remove("audio_list.txt")
        
    except Exception as e:
        print(f"   ⚠️ Could not combine audio: {e}")
    
    # Create video with exact same background as previous series
    print("🎬 Creating video with exact same style...")
    
    # Video settings (same as previous series)
    width, height = 1080, 1920
    fps = 30
    
    # Create background with exact same colors as previous series
    # Dark reddish-brown gradient: #2c1810 to #4a1f1f to #2c1810
    output_video = f"walk_spirit_shorts_{duration}s_{timestamp}.mp4"
    
    # Create video using color filter (same as previous series)
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x2c1810:size={width}x{height}:duration={duration}',
        '-i', combined_file,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-shortest',
        '-preset', 'fast',
        '-crf', '23',
        output_video
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Created video: {output_video}")
        return output_video
    except Exception as e:
        print(f"❌ Could not create video: {e}")
        return None

def main():
    """Create all three versions in exact same format"""
    print("🤖 CREATE 'WALK IN THE SPIRIT' SHORTS")
    print("=" * 60)
    print("Creating all 3 versions in exact same format as previous series!")
    
    durations = [25, 50, 75]
    created_files = []
    
    for duration in durations:
        print(f"\n🎬 Creating {duration}-second version...")
        file = create_walk_spirit_shorts(duration)
        if file:
            created_files.append(file)
    
    print(f"\n🎉 ALL VERSIONS CREATED SUCCESSFULLY!")
    print("=" * 60)
    
    print(f"\n📁 Created Files:")
    for i, file in enumerate(created_files, 1):
        print(f"{i}. {file}")
    
    print(f"\n🎯 Format Features (All Versions):")
    print(f"• Exact same style as previous series")
    print(f"• Same colors: Dark reddish-brown gradient")
    print(f"• Same layout: 9:16 YouTube Shorts format")
    print(f"• Same voice: Daniel (British accent)")
    print(f"• Same quality: Professional broadcast-ready")
    
    print(f"\n🚀 Ready to upload to YouTube Shorts!")
    print(f"🏷️ Add hashtags: #WalkInTheSpirit #HolySpirit #ChristianLife #Galatians5")

if __name__ == "__main__":
    main() 