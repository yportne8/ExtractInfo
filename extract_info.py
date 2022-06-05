from youtube_dl import YoutubeDL


def parse_request(y: str):
    if not "http" in y:
        if len(y)==11:
            y=f"https://www.youtube.com/watch?v={y}"
        else:
            y=f"ytsearch:{y}"
    return y
        
        
def extract_info(x: any):
    y=parse_request(x)
    with YoutubeDL() as ydl:
        try:
            info=ydl.extract_info(y,
                    download=False)["entries"][0]
        except:
            info=ydl.extract_info(y,
                    download=False)
    print(info)
    return info            



if __name__ == "__main__":
    
    import sys
    
    if len(sys.argv) > 1:
        query = ""
        for arg in sys.argv[1:]:
            query += arg + " "
        extract_info(query)
        