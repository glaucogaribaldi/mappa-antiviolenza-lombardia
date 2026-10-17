import os
from PIL import Image, ImageDraw

def generate_cav_white(output_path, target_size=(96, 96)):
    print("Generating updated CAV marker (White background, pink house)...")
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    
    pink = (255, 20, 147, 255) # DeepPink #FF1493
    white = (255, 255, 255, 255)
    
    # Draw a perfect white circle with a pink border
    draw.ellipse([4, 4, target_size[0]-5, target_size[1]-5], fill=white, outline=pink, width=6)
    
    # Draw a beautiful, solid pink house in the center
    # Coordinates centered at (48, 48) on 96x96 canvas
    # House roof: triangle from (48, 22) to (24, 44) to (72, 44)
    draw.polygon([(48, 24), (26, 44), (70, 44)], fill=pink)
    # House body: rectangle from (31, 44) to (65, 72)
    draw.rectangle([32, 44, 64, 72], fill=pink)
    
    # Draw a white heart inside the house
    # Center of the house body is at (48, 58). Let's draw a white heart there.
    draw.polygon([(48, 64), (41, 57), (48, 50), (55, 57)], fill=white)
    draw.ellipse([41, 51, 48, 58], fill=white)
    draw.ellipse([48, 51, 55, 58], fill=white)
    
    canvas.save(output_path, "PNG")
    print(f"Saved update CAV marker to {output_path}")

def generate_hospital_white(output_path, target_size=(96, 96)):
    print("Generating updated Hospital marker (White background, bold red cross)...")
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    
    red = (255, 0, 0, 255) # Red #FF0000
    white = (255, 255, 255, 255)
    
    # Draw a perfect white circle with a red border
    draw.ellipse([4, 4, target_size[0]-5, target_size[1]-5], fill=white, outline=red, width=6)
    
    # Draw a massive, bold, highly visible solid Red Cross centered at (48, 48)
    # Vertical bar: width 20px, height 52px
    draw.rectangle([38, 22, 58, 74], fill=red)
    # Horizontal bar: width 52px, height 20px
    draw.rectangle([22, 38, 74, 58], fill=red)
    
    canvas.save(output_path, "PNG")
    print(f"Saved updated Hospital marker to {output_path}")

def generate_police_shield(output_path, bg_color, target_size=(96, 96)):
    print(f"Generating police shield marker for {output_path}...")
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    
    white = (255, 255, 255, 255)
    
    # Draw a perfect circle badge matching the specific force color
    draw.ellipse([4, 4, target_size[0]-5, target_size[1]-5], fill=bg_color, outline=white, width=5)
    
    # Draw a clean, thick white Shield in the center
    draw.polygon([
        (32, 26), (48, 22), (64, 26), 
        (64, 48), (48, 70), (32, 48)
    ], fill=white)
    
    # Draw a small inner shield or star in the center matching the background color
    draw.polygon([
        (36, 30), (48, 27), (60, 30), 
        (60, 46), (48, 64), (36, 46)
    ], fill=bg_color)
    
    # Add a tiny white star in the center of the shield for extra UX clarity!
    draw.polygon([(48, 36), (50, 41), (55, 41), (51, 44), (53, 49), (48, 46), (43, 49), (45, 44), (41, 41), (46, 41)], fill=white)
    
    canvas.save(output_path, "PNG")
    print(f"Saved police shield marker to {output_path}")

def run_generation():
    out_dir = '/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/'
    
    # 1. Generate updated CAV marker (White circle with pink house)
    generate_cav_white(os.path.join(out_dir, 'marker_cav.png'))
    
    # 2. Generate updated Hospital marker (White circle with red border + bold red cross)
    generate_hospital_white(os.path.join(out_dir, 'marker_hospital.png'))
    
    # 3. Generate 4 updated Police Shield markers in various shades of blue
    # Carabinieri (Dark blue: #00008B)
    generate_police_shield(os.path.join(out_dir, 'marker_police_carabinieri.png'), bg_color=(0, 0, 139, 255))
    # Polizia di Stato (Dodger blue: #1E90FF)
    generate_police_shield(os.path.join(out_dir, 'marker_police_stato.png'), bg_color=(30, 144, 255, 255))
    # Polizia Locale (Steel blue: #4682B4)
    generate_police_shield(os.path.join(out_dir, 'marker_police_locale.png'), bg_color=(70, 130, 180, 255))
    # Generico (Blue: #0000FF)
    generate_police_shield(os.path.join(out_dir, 'marker_police_generico.png'), bg_color=(0, 0, 255, 255))

if __name__ == "__main__":
    run_generation()
