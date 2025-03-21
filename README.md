how to run:
python3 update_go_images.py [path]

example
python3 update_go_images.py /Users/bytedance/Documents


capability : 

Recursive Scanning – Reads all files in the folder and subfolders.
Supports Multiple File Types – Works with .go, .template, .txt, .json, .csv, etc.
Image URL Transformation – Converts images.tokopedia.net & ecs7.tokopedia.net to p16-images-comn-sg.tokopedia-static.net and adds suffix ~tplv-zr7vqa5nfb-image.image.
File URL Transformation – Converts assets.tokopedia.net to p16-assets-sg.tokopedia-static.net with a prefix only.
Smart Filtering – Ignores binary files like .png, .mp4, .exe.
In-Place Editing – Updates files without creating new ones.
