import os
from PIL import Image, ImageDraw, ImageOps

def make_transparent_circle(img_path, output_path, bg_color=None, target_size=(96, 96)):
    print(f"Processing {img_path}...")
    img = Image.open(img_path).convert("RGBA")
    
    # 1. Create a transparent canvas of the target size
    canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    
    # 2. Draw the background circle with a white border
    radius = target_size[0] // 2
    center = target_size[0] // 2
    
    if bg_color:
        # Draw base colored circle
        draw.ellipse([2, 2, target_size[0]-3, target_size[1]-3], fill=bg_color, outline=(255, 255, 255, 255), width=3)
    
    # 3. Process the source image based on category
    basename = os.path.basename(img_path)
    
    if "a53cf084" in basename: # CAV (Already a pink circle on a white background)
        # We just need to mask the white corners into a perfect circle
        mask = Image.new("L", img.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse([0, 0, img.size[0], img.size[1]], fill=255)
        
        # Apply mask
        img.putalpha(mask)
        # Resize to fit the canvas perfectly
        img_resized = img.resize((target_size[0]-4, target_size[1]-4), Image.Resampling.LANCZOS)
        canvas.paste(img_resized, (2, 2), img_resized)
        
    elif "105f40af" in basename: # Hospital (Building on white background)
        # Convert white background to transparent
        datas = img.getdata()
        new_data = []
        for item in datas:
            # If pixel is near white, make it transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        img.putdata(new_data)
        
        # Crop to contents
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        # Resize to fit inside the red circle badge (about 65% of the canvas size)
        inner_size = int(target_size[0] * 0.65)
        img_resized = img.resize((inner_size, inner_size), Image.Resampling.LANCZOS)
        
        # Paste centered
        offset = (target_size[0] - inner_size) // 2
        canvas.paste(img_resized, (offset, offset), img_resized)
        
    elif "67650648" in basename: # Police (Officer silhouette)
        # Convert white background to transparent
        datas = img.getdata()
        new_data = []
        for item in datas:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        img.putdata(new_data)
        
        # Crop
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        # Resize to fit inside the blue circle badge (about 65% of the canvas size)
        inner_size = int(target_size[0] * 0.65)
        img_resized = img.resize((inner_size, inner_size), Image.Resampling.LANCZOS)
        
        # Paste centered
        offset = (target_size[0] - inner_size) // 2
        canvas.paste(img_resized, (offset, offset), img_resized)

    # Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas.save(output_path, "PNG")
    print(f"Saved unified marker to {output_path}")

def run_unification():
    cav_in = '/Users/zava/.openclaw/media/inbound/a53cf084-729b-4400-be4f-b0fad4f44bc4.jpg'
    hospital_in = '/Users/zava/.openclaw/media/inbound/105f40af-436f-4b60-9838-6bbffdafa8e2.jpg'
    police_in = '/Users/zava/.openclaw/media/inbound/67650648-e36c-439b-942f-f7d6554abfbc.png'
    
    out_dir = '/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/'
    
    # 1. Unify CAV (Pink circle is already built into the image)
    make_transparent_circle(cav_in, os.path.join(out_dir, 'marker_cav.png'))
    
    # 2. Unify Hospital (Red circle background #FF0000)
    make_transparent_circle(hospital_in, os.path.join(out_dir, 'marker_hospital.png'), bg_color=(255, 0, 0, 255))
    
    # 3. Unify Police (Create four color-coded circles matching the specific force types)
    # Carabinieri (Dark blue: #00008B)
    make_transparent_circle(police_in, os.path.join(out_dir, 'marker_police_carabinieri.png'), bg_color=(0, 0, 139, 255))
    # Polizia di Stato (Dodger blue: #1E90FF)
    make_transparent_circle(police_in, os.path.join(out_dir, 'marker_police_stato.png'), bg_color=(30, 144, 255, 255))
    # Polizia Locale (Steel blue: #4682B4)
    make_transparent_circle(police_in, os.path.join(out_dir, 'marker_police_locale.png'), bg_color=(70, 130, 180, 255))
    # Generico (Blue: #0000FF)
    make_transparent_circle(police_in, os.path.join(out_dir, 'marker_police_generico.png'), bg_color=(0, 0, 255, 255))

if __name__ == "__main__":
    run_unification()
